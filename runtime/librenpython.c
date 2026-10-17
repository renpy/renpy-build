#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "Python.h"
#ifdef MS_WINDOWS
#include <shlwapi.h>
#endif

void init_librenpy(void);

#ifdef MS_WINDOWS
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

typedef struct {
    PyConfig config;
    char *executable_dir;
    char *script_name;
    int python_home_found;
    int script_found;
} Runtime;

static Runtime runtime;

static void check_status(PyStatus status);
static void initialize_runtime(int isolated, int argc, char **argv);
static void initialize_python(void);
static void clear_runtime(void);
static void set_config_path(wchar_t **config_path, const char *path);
static void append_module_search_path(const char *path);
static char *format_runtime_path(const char *prefix, const char *suffix);
static void find_python_home(const char *path);
static void find_pyname(const char *path);

#ifdef MS_WINDOWS
/*
 * Windows applies MAX_PATH to the unresolved string, so "lib/py3-x/../.."
 * can push an otherwise short path over the limit. Collapse it here.
 * Takes ownership of path; returns it unchanged on failure.
 */
static char *normalize_path(char *path) {
    DWORD size = GetFullPathNameA(path, 0, NULL, NULL);
    char *full = size ? (char *) malloc(size) : NULL;
    if (full == NULL) {
        return path;
    }
    DWORD length = GetFullPathNameA(path, size, full, NULL);
    if (length == 0 || length >= size) {
        free(full);
        return path;
    }

    free(path);
    return full;
}
#else
static char *normalize_path(char *path) {
    return path;
}
#endif

int EXPORT renpython_main(int argc, char **argv) {
    initialize_runtime(0, argc, argv);

    runtime.config.user_site_directory = 0;
    runtime.config.parse_argv = 1;
    check_status(PyConfig_SetBytesArgv(&runtime.config, argc, argv));
    initialize_python();
    clear_runtime();

    return Py_RunMain();
}

int EXPORT launcher_main(int argc, char **argv) {
#ifdef WEB
    argv[0] = "./main";
#endif

    initialize_runtime(1, argc, argv);

    runtime.config.user_site_directory = 0;
    runtime.config.parse_argv = 1;
    runtime.config.install_signal_handlers = 1;
    // Search the project root and each platform's packaged project location.
#ifdef LINUX
    // Relative to the base directory.
    find_pyname("/");
    // Relative to lib/py3-linux-x86_64.
    find_pyname("/../../");
#endif
#ifdef MAC
    // Relative to the base directory.
    find_pyname("/");
    // Relative to lib/py3-mac-universal.
    find_pyname("/../../");
    // In the mac app - exe is in game.app/Contents/MacOS,
    // main.py is in game.app/Contents/MacOS/Resources/autorun.
    find_pyname("/../Resources/autorun/");
    // Relative to renpy.app/Contents/MacOS.
    find_pyname("/../../../");
#endif
#ifdef WINDOWS
    // Relative to the base directory.
    find_pyname("/");
    // Relative to lib/py3-windows-x86_64.
    find_pyname("/../../");
#endif
#ifdef IOS
    // Relative to the base directory.
    find_pyname("/base/");
#endif

    char **new_argv = (char **) alloca((argc + 1) * sizeof(char *));
    new_argv[0] = argv[0];
    new_argv[1] = runtime.script_name;

    for (int i = 1; i < argc; i++) {
        new_argv[i + 1] = argv[i];
    }

    check_status(PyConfig_SetBytesArgv(&runtime.config, argc + 1, new_argv));
    initialize_python();
    clear_runtime();

    return Py_RunMain();
}

static void check_status(PyStatus status) {
    if (PyStatus_Exception(status)) {
        Py_ExitStatusException(status);
    }
}

static void initialize_runtime(int isolated, int argc, char **argv) {
    const char *argv0 = argv[0];
    PyPreConfig preconfig;
    if (isolated) {
        PyPreConfig_InitIsolatedConfig(&preconfig);
    } else {
        PyPreConfig_InitPythonConfig(&preconfig);
    }

    preconfig.utf8_mode = 1;
    preconfig.use_environment = 0;
    check_status(Py_PreInitializeFromBytesArgs(&preconfig, argc, argv));

    if (isolated) {
        PyConfig_InitIsolatedConfig(&runtime.config);
    } else {
        PyConfig_InitPythonConfig(&runtime.config);
    }

    init_librenpy();
    if (!getenv("RENPY_PLATFORM")) {
        putenv("RENPY_PLATFORM=" PLATFORM "-" ARCH);
    }

    check_status(PyConfig_SetBytesString(&runtime.config, &runtime.config.program_name, argv0));

    // Split argv[0] into its executable directory and the corresponding .py name.
    const char *basename = argv0;
    const char *separator = NULL;
    for (const char *p = argv0; *p; p++) {
        if (*p == '\\' || *p == '/') {
            separator = p;
            basename = p + 1;
        }
    }

    size_t dir_length = separator ? (size_t) (separator - argv0) : 1;
    runtime.executable_dir = (char *) malloc(dir_length + 1);
    if (runtime.executable_dir == NULL) {
        Py_ExitStatusException(PyStatus_NoMemory());
    }

    if (separator) {
        memcpy(runtime.executable_dir, argv0, dir_length);
    } else {
        runtime.executable_dir[0] = '.';
    }
    runtime.executable_dir[dir_length] = '\0';

    size_t basename_length = strlen(basename);
    // On Windows, remove the .exe extension from the basename.
#ifdef MS_WINDOWS
    const char *extension = PathFindExtensionA(argv0);
    if (CompareStringA(LOCALE_INVARIANT, NORM_IGNORECASE, extension, -1, ".exe", -1) == CSTR_EQUAL) {
        basename_length = (size_t) (extension - basename);
    }
#endif

    runtime.script_name = (char *) malloc(basename_length + sizeof(".py"));
    if (runtime.script_name == NULL) {
        Py_ExitStatusException(PyStatus_NoMemory());
    }

    memcpy(runtime.script_name, basename, basename_length);
    memcpy(runtime.script_name + basename_length, ".py", sizeof(".py"));

    // Search the platform-specific locations for the packaged Python home.
#ifdef LINUX
    // Relative to the base directory.
    find_python_home("");
    find_python_home("/../..");
#endif
#ifdef MAC
    // Relative to the Resources directory.
    find_python_home("/../Resources");
    // Relative to the base directory.
    find_python_home("");
    // Relative to lib/py3-mac-universal.
    find_python_home("/../..");
    // Relative to game.app/Contents/MacOS.
    find_python_home("/../../..");
#endif
#ifdef WINDOWS
    // Relative to the base directory.
    find_python_home("");
    // Relative to lib/py3-windows-x86_64.
    find_python_home("/../..");
#endif
#ifdef IOS
    // Relative to the base directory.
    find_python_home("/base");
#endif
}

static void initialize_python(void) {
    check_status(Py_InitializeFromConfig(&runtime.config));
    PyConfig_Clear(&runtime.config);
}

static void clear_runtime(void) {
    free(runtime.executable_dir);
    free(runtime.script_name);
}

static void set_config_path(wchar_t **config_path, const char *path) {
    check_status(PyConfig_SetBytesString(&runtime.config, config_path, path));
}

static void append_module_search_path(const char *path) {
    wchar_t *wide_path = Py_DecodeLocale(path, NULL);
    if (wide_path == NULL) {
        Py_ExitStatusException(PyStatus_NoMemory());
    }

    PyStatus status = PyWideStringList_Append(&runtime.config.module_search_paths, wide_path);
    PyMem_RawFree(wide_path);
    check_status(status);
}

static char *format_runtime_path(const char *prefix, const char *suffix) {
    int length = snprintf(NULL, 0, "%s%s%s", runtime.executable_dir, prefix, suffix);
    if (length < 0) {
        Py_ExitStatusException(PyStatus_Error("Unable to format a Ren'Py runtime path."));
    }

    char *path = (char *) malloc((size_t) length + 1);
    if (path == NULL) {
        Py_ExitStatusException(PyStatus_NoMemory());
    }

    if (snprintf(path, (size_t) length + 1, "%s%s%s", runtime.executable_dir, prefix, suffix) != length) {
        free(path);
        Py_ExitStatusException(PyStatus_Error("Unable to format a Ren'Py runtime path."));
    }
    return normalize_path(path);
}

/*
 * Find the Python installation relative to the executable. The marker file
 * identifies a candidate home; the ZIP archive is checked as an alternate.
 */
static void find_python_home(const char *path) {
    if (runtime.python_home_found) {
        return;
    }

    char *site_path = format_runtime_path(path, "/lib/" PYTHONVER "/site.pyc");
    FILE *file = fopen(site_path, "rb");
    int has_site = file != NULL;
    if (file) {
        fclose(file);
    }
    free(site_path);

    int has_zip = 0;
    if (!has_site) {
        char *zip_path = format_runtime_path(path, "/lib/python" PYCVER ".zip");
        file = fopen(zip_path, "rb");
        has_zip = file != NULL;
        if (file) {
            fclose(file);
        }
        free(zip_path);
    }

    if (!has_site && !has_zip) {
        return;
    }

    runtime.python_home_found = 1;

    char *home = format_runtime_path(path, "");
    set_config_path(&runtime.config.home, home);
    set_config_path(&runtime.config.prefix, home);
    set_config_path(&runtime.config.exec_prefix, home);
    free(home);

    char *module_path = format_runtime_path(path, "/lib/" PYTHONVER);
    append_module_search_path(module_path);
    free(module_path);

    char *zip_path = format_runtime_path(path, "/lib/python" PYCVER ".zip");
    append_module_search_path(zip_path);
    free(zip_path);

    runtime.config.module_search_paths_set = 1;
}

/*
 * Find the launch script relative to the executable, preferring its matching
 * .py name and falling back to main.py in each candidate project directory.
 */
static void find_pyname(const char *path) {
    if (runtime.script_found) {
        return;
    }

    const char *candidate = NULL;
    char *candidate_path = format_runtime_path(path, runtime.script_name);
    FILE *file = fopen(candidate_path, "rb");
    int has_script = file != NULL;
    if (file) {
        fclose(file);
    }
    free(candidate_path);

    if (has_script) {
        candidate = runtime.script_name;
    } else {
        candidate_path = format_runtime_path(path, "main.py");
        file = fopen(candidate_path, "rb");
        int has_main = file != NULL;
        if (file) {
            fclose(file);
        }
        free(candidate_path);
        if (has_main) {
            candidate = "main.py";
        }
    }

    if (candidate) {
        char *script_path = format_runtime_path(path, candidate);
        free(runtime.script_name);
        runtime.script_name = script_path;
        runtime.script_found = 1;
    }
}
