#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <stdlib.h>
#include <wchar.h>
#include "Python.h"

/**
 * A small note on encoding: This does as much as it can in UTF-8 mode,
 * with the only work done with wchar_t being to test for the actual
 * existence of files on windows.
 */

void init_librenpy(void);

#ifdef MS_WINDOWS
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

#undef DEBUG_EXISTS

/* The name of the directory containing the exe. */
static char *exedir;

/* The name of the .py file to use */
static char *pyname;

/**
 * The Python config object.
 */
PyConfig config;




static char *encode_utf8(wchar_t *s) {
    char *rv;
    unsigned char *p;
    unsigned int ch;

    return "";


    rv = (char *) malloc(wcslen(s) * 4 + 1);
    p = (unsigned char *) rv;

    while (*s) {
        ch = *s++;

        if (ch < 0x80) {
            *p++ = ch;
        } else if (ch < 0x800) {
            *p++ = 0xC0 | (ch >> 6);
            *p++ = 0x80 | (ch & 0x3F);
        } else if (ch < 0x10000) {
            *p++ = 0xE0 | (ch >> 12);
            *p++ = 0x80 | ((ch >> 6) & 0x3F);
            *p++ = 0x80 | (ch & 0x3F);
        } else {
            *p++ = 0xF0 | (ch >> 18);
            *p++ = 0x80 | ((ch >> 12) & 0x3F);
            *p++ = 0x80 | ((ch >> 6) & 0x3F);
            *p++ = 0x80 | (ch & 0x3F);
        }
   }

    *p = 0;

    return rv;
}


static wchar_t *decode_utf8(const char *s) {

    wchar_t *rv;
    unsigned char *p = (unsigned char *) s;
    unsigned int ch;

    rv = (wchar_t *) malloc(strlen(s) * sizeof(wchar_t) + sizeof(wchar_t));
    wchar_t *q = rv;

    while (*p) {
        ch = *p++;

        if (ch < 0x80) {
            *q++ = ch;
        } else if ((ch & 0xE0) == 0xC0) {
            *q = (ch & 0x1F) << 6;
            ch = *p++;
            *q |= ch & 0x3F;
            q += 1;
        } else if ((ch & 0xF0) == 0xE0) {
            *q = (ch & 0x0F) << 12;
            ch = *p++;
            *q |= (ch & 0x3F) << 6;
            ch = *p++;
            *q |= ch & 0x3F;
            q += 1;
        } else {
            *q = (ch & 0x07) << 18;
            ch = *p++;
            *q |= (ch & 0x3F) << 12;
            ch = *p++;
            *q |= (ch & 0x3F) << 6;
            ch = *p++;
            *q |= ch & 0x3F;
            q += 1;
        }
    }

    *q = 0;

    return rv;
}



/**
 * Returns true if every character in a is equivalent to the characters in b0 or b1,
 * and the strings are of the same length. (This exists because strcasecmp considers
 * locale, and we don't want that.)
 */
static int compare(const char *a, const char *b0, const char *b1) {
    while (1) {
        if (*a != *b0 && *a != *b1) {
            return 0;
        }

        if (!*a) {
            return 1;
        }

        a += 1;
        b0 += 1;
        b1 += 1;
    }
}


/**
 * This takes argv0 and sets the exedir and pyname variables.
 */
static void take_argv0(char *argv0) {

    config.program_name = decode_utf8(argv0);

    // This copy is required because dirname can change its arguments.
    argv0 = strdup(argv0);

    // Basename. This seems to be broken in certain locales, so it's
    // reimplemented here.
    char *exename = argv0 + strlen(argv0) -1;
    while (exename > argv0) {
        if (*exename == '\\' || *exename == '/') {
            *exename = 0;
            exename += 1;
            break;
        }
        exename -= 1;
    }

    int pyname_size = strlen(exename) + strlen(".py") + 1;

    pyname = (char *) malloc(pyname_size);
    strncpy(pyname, exename, pyname_size);

#ifdef MS_WINDOWS

    // This removes the .exe suffix.
    if (strlen(pyname) > 4) {
        if (compare(&pyname[strlen(pyname) - 4], ".exe", ".EXE")) {
            pyname[strlen(pyname) - 4] = 0;
        }
    }

    // This removes the -32 suffix, if it exists.
    if (strlen(pyname) > 3) {
        if (compare(&pyname[strlen(pyname) - 3], "-32", "-32")) {
            pyname[strlen(pyname) - 3] = 0;
        }
    }

#endif

    strncat(pyname, ".py", pyname_size);

    exedir = strdup(argv0);
    if (exename == argv0) {
        exedir = strdup(".");
    } else {
        exedir = strdup(argv0);
    }

    // free(argv0);
}

/**
 * This combines the exedir and up to two components, and returns the result.
 * It returns a newly allocated string.
 */
static char *join(const char *p1, const char *p2) {
    int size = strlen(exedir) + 1;

    if (p1) {
        size += strlen(p1);
    }

    if (p2) {
        size += strlen(p2);
    }

    char *rv = (char *) malloc(size);

    strncpy(rv, exedir, size);

    if (p1) {
        strncat(rv, p1, size);
    }

    if (p2) {
        strncat(rv, p2, size);
    }

    return rv;
}

/*
 * This combines exedir with the optional p1 and p2. It returns 1 if the
 * file exists, and 0 otherwise.
 */
static int exists(const char *p1, const char *p2) {
    char *path = join(p1, p2);

#ifdef MS_WINDOWS
    wchar_t *wpath = decode_utf8(path);
    if (wpath == NULL) {
        return 0;
    }
    FILE *f = _wfopen(wpath, L"rb");
    free(wpath);
#else
    FILE *f = fopen(path, "rb");
#endif

#ifdef DEBUG_EXISTS
    printf("%s", path);
#endif

    free(path);

    if (f) {
        fclose(f);

#ifdef DEBUG_EXISTS
        printf(" exists.\n");
#endif

        return 1;
    } else {
#ifdef DEBUG_EXISTS
        printf(" does not exist.\n");
#endif

        return 0;
    }
}

/**
 * This tries to find a python home in p. If one hasn't been found already,
 * it calls Py_SetPythonHome.
 */
static void find_python_home(const char *p) {
    static int found = 0;

    if (found) {
        return;
    }

#ifdef WINDOWS
    if (exists(p, "\\lib\\" PYTHONVER "\\site.pyc") ||
        exists(p, "\\lib\\python" PYCVER ".zip")) {

        found = 1;
        config.home = decode_utf8(join(p, NULL));
        config.prefix = config.home;
        config.exec_prefix = config.home;
        PyWideStringList_Append(&config.module_search_paths, decode_utf8(join(p, "\\lib\\" PYTHONVER)));
        PyWideStringList_Append(&config.module_search_paths, decode_utf8(join(p, "\\lib\\python" PYCVER ".zip")));
        config.module_search_paths_set = 1;
    }
#else
    if (exists(p, "/lib/" PYTHONVER "/site.pyc") ||
        exists(p, "/lib/python" PYCVER ".zip")) {

        found = 1;
        config.home = decode_utf8(join(p, NULL));
        config.prefix = config.home;
        config.exec_prefix = config.home;
        PyWideStringList_Append(&config.module_search_paths, decode_utf8(join(p, "/lib/" PYTHONVER)));
        PyWideStringList_Append(&config.module_search_paths, decode_utf8(join(p, "/lib/python" PYCVER ".zip")));
        config.module_search_paths_set = 1;
    }
#endif
}

/**
 * Searches for the python home directory in the platform-specific location.
 */
static void search_python_home(void) {

#ifdef LINUX
    // Relative to the base directory.
    find_python_home("");

    // Relative to lib/linux-x86_64.
    find_python_home("/../..");
#endif

#ifdef MAC
    // Relative to the Resources directory.
    find_python_home("/../Resources");

    // Relative to the base directory.
    find_python_home("");

    // Relative to lib/mac-x86_64.
    find_python_home("/../..");

    // Relative to game.app/Contents/MacOS.
    find_python_home("/../../..");
#endif

#ifdef WINDOWS
    // Relative to the base directory.
    find_python_home("");

    // Relative to lib/windows-i686.
    find_python_home("\\..\\..");

#endif

#ifdef IOS
    // Relative to the base directory.
    find_python_home("/base");
#endif

}


/**
 * This finds the main python file. If it's been found, sets pyname to the
 * value that's been found.
 */
static void find_pyname(const char *p) {
    static int found = 0;

    if (found) {
        return;
    }

    if (exists(p, pyname)) {
        found = 1;
        pyname = join(p, pyname);
        return;
    }

    if (exists(p, "main.py")) {
        found = 1;
        pyname = join(p, "main.py");
        return;
    }
}


static void search_pyname() {

#ifdef LINUX
    // Relative to the base directory.
    find_pyname("/");

    // Relative to lib/windows-i686
    find_pyname("/../../");
#endif

#ifdef MAC
    // Relative to the base directory.
    find_pyname("/");

    // Relative to lib/windows-i686
    find_pyname("/../../");

    // In the mac app - exe is in game.app/Contents/MacOS,
    // main.py is in game.app/Contents/MacOS/Resources/autorun.
    find_pyname("/../Resources/autorun/");

    // Relative to renpy.app/Contents/MacOS.
    find_pyname("/../../../");
#endif

#ifdef WINDOWS
    // Relative to the base directory.
    find_pyname("\\");

    // Relative to lib/windows-i686.
    find_pyname("\\..\\..\\");
#endif

#ifdef IOS
    find_pyname("/base/");
#endif
}

/**
 * This sets the RENPY_PLATFORM environment variable, if it hasn't been set
 * already.
 */
static void set_renpy_platform() {
    if (!getenv("RENPY_PLATFORM")) {
        putenv("RENPY_PLATFORM=" PLATFORM "-" ARCH);
    }
}

/**
 * Preinitializes Python, to enable UTF-8 mode.
 */

static void preinitialize(int isolated, int argc, char **argv) {
    PyPreConfig preconfig;

    // Initialize PreConfig.
    if (isolated) {
        PyPreConfig_InitIsolatedConfig(&preconfig);
    } else {
        PyPreConfig_InitPythonConfig(&preconfig);
    }

    preconfig.utf8_mode = 1;
    preconfig.use_environment = 0;

    Py_PreInitializeFromBytesArgs(&preconfig, argc, argv);

    init_librenpy();

    // Initialize Config.
    if (isolated) {
        PyConfig_InitIsolatedConfig(&config);
    } else {
        PyConfig_InitPythonConfig(&config);
    }

}

/**
 * The same, but use wchar_t arguments.
 */
static void preinitialize_wide(int isolated, int argc, wchar_t **argv) {
    PyPreConfig preconfig;

    // Initialize PreConfig.
    if (isolated) {
        PyPreConfig_InitIsolatedConfig(&preconfig);
    } else {
        PyPreConfig_InitPythonConfig(&preconfig);
    }

    preconfig.utf8_mode = 1;
    preconfig.use_environment = 0;

    Py_PreInitializeFromArgs(&preconfig, argc, argv);

    init_librenpy();

    // Initialize Config.
    if (isolated) {
        PyConfig_InitIsolatedConfig(&config);
    } else {
        PyConfig_InitPythonConfig(&config);
    }

}


/**
 * This is the python command, and all it does is to modify the path to the
 * python library, and start python.
 */
int EXPORT renpython_main(int argc, char **argv) {

    preinitialize(0, argc, argv);

    set_renpy_platform();
    take_argv0(argv[0]);
    search_python_home();

    config.user_site_directory = 0;
    Py_InitializeFromConfig(&config);

    return Py_BytesMain(argc, argv);
}

int EXPORT renpython_main_wide(int argc, wchar_t **argv) {

    preinitialize_wide(0, argc, argv);

    set_renpy_platform();
    take_argv0(encode_utf8(argv[0]));
    search_python_home();

    config.user_site_directory = 0;
    Py_InitializeFromConfig(&config);

    return Py_Main(argc, argv);
}


/**
 * This is called from the launcher executable, to start Ren'Py running.
 */
int EXPORT launcher_main(int argc, char **argv) {

#ifdef WEB
    argv[0] = "./main";
#endif

    preinitialize(1, argc, argv);

    set_renpy_platform();
    take_argv0(argv[0]);
    search_python_home();

    config.user_site_directory = 0;
    config.parse_argv = 1;
    config.install_signal_handlers = 1;

    search_pyname();

    // Figure out argv.
    char **new_argv = (char **) alloca((argc + 1) * sizeof(char *));

    new_argv[0] = argv[0];
    new_argv[1] = pyname;

    for (int i = 1; i < argc; i++) {
        new_argv[i + 1] = argv[i];
    }

    PyConfig_SetBytesArgv(&config, argc + 1, new_argv);
    Py_InitializeFromConfig(&config);

    return Py_RunMain();
}

/**
 * This is called from the launcher executable, to start Ren'Py running.
 */
int EXPORT launcher_main_wide(int argc, wchar_t **argv) {

    preinitialize_wide(1, argc, argv);

    set_renpy_platform();
    take_argv0(encode_utf8(argv[0]));
    search_python_home();

    config.user_site_directory = 0;
    config.parse_argv = 1;
    config.install_signal_handlers = 1;

    search_pyname();

    // Figure out argv.
    wchar_t **new_argv = (wchar_t **) alloca((argc + 1) * sizeof(wchar_t *));

    new_argv[0] = argv[0];
    new_argv[1] = decode_utf8(pyname);

    for (int i = 1; i < argc; i++) {
        new_argv[i + 1] = argv[i];
    }

    PyConfig_SetArgv(&config, argc + 1, new_argv);
    Py_InitializeFromConfig(&config);

    return Py_RunMain();
}
