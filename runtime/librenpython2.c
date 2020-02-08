#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <stdlib.h>
#include "Python.h"

void init_librenpy(void);

#ifdef MS_WINDOWS
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

/* The name of the directory containing the exe. */
static char *exedir;

/* The name of the .py file to use */
static char *pyname;

/**
 * This takes argv0 and sets the exedir and pyname variables.
 */
static void take_argv0(char *argv0) {

    Py_SetProgramName(argv0);

    // This copy is required because dirname can change its arguments.
    argv0 = strdup(argv0);

    char *exename = basename(argv0);
    int pyname_size = strlen(exename) + 3;

    pyname = (const char *) malloc(pyname_size);
    strncpy(pyname, exename, pyname_size);

#ifdef MS_WINDOWS
    // This removes the .exe suffix.
    pyname[strlen(pyname) - 4] = 0;
#endif

    strncat(pyname, ".py", pyname_size);

    exedir = strdup(dirname(argv0));

    free(argv0);
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
 * This comnbines exedir with the optional p1 and p2. It returns 1 if the
 * file exists, and 0 otherwise.
 */
static exists(const char *p1, const char *p2) {
    char *path = join(p1, p2);

    FILE *f = fopen(path, "rb");

    free(path);

    if (f) {
        fclose(f);
        return 1;
    } else {
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

    if (exists(p, "\\lib\\python2.7\\site.pyo") || exists(p, "\\lib\\python27.zip")) {
        found = 1;
        Py_SetPythonHome(join(p, NULL));
    }
}

/**
 * Searches for the python home directory in the platform-specific location.
 */
static void search_python_home(void) {
#ifdef MS_WINDOWS
    // Relative to the base directory.
    find_python_home("");

    // Relative to lib/windows-i686.
    find_python_home("\\..\\..");

#else
    // Relative to the base directory.
    find_python_home("");

    // Relative to lib/linux-x86_64.
    find_python_home("/../..");

    // Relative to game.app/Contents/MacOS.
    find_python_home("/../../..");
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
    }
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
 * This is the python command, and all it does is to modify the path to the
 * python library, and start python.
 */
int EXPORT renpython_main(int argc, char **argv) {

    set_renpy_platform();
    take_argv0(argv[0]);
    search_python_home();

    Py_OptimizeFlag = 2;
    Py_NoUserSiteDirectory = 1;

    init_librenpy();
    return Py_Main(argc, argv);
}

/**
 * This is called from the launcher executable, to start Ren'Py running.
 */
int EXPORT launcher_main(int argc, char **argv) {

    set_renpy_platform();
    take_argv0(argv[0]);
    search_python_home();

#ifdef MS_WINDOWS
    // Relative to the base directory.
    find_pyname("\\");

    // Relative to lib/windows-i686.
    find_pyname("\\..\\..\\");
#else

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

    // Figure out argv.
    char **new_argv = (char **) alloca((argc + 1) * sizeof(char *));

    new_argv[0] = argv[0];
    new_argv[1] = pyname;

    for (int i = 1; i < argc; i++) {
        new_argv[i + 1] = argv[i];
    }

    // Set up the Python flags.
    Py_OptimizeFlag = 2;
    Py_IgnoreEnvironmentFlag = 1;
    Py_NoUserSiteDirectory = 1;

    init_librenpy();
    return Py_Main(argc + 1, new_argv);
}
