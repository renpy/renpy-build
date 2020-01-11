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

static int check_file(const char *argv0, const char *relpath) {
    char *base;
    char path[4096];
    FILE *f;


    base = strdup(argv0);
    snprintf(path, 4096, "%s%s", dirname(base), relpath);
    free(base);

    f = fopen(path, "r");
    if (f) {
        fclose(f);
        return 1;
    } else {
        return 0;
    }
}

static void set_python_home(const char *argv0, const char *relpath) {
    char *base;
    char path[4096];

    base = strdup(argv0);
    snprintf(path, 4096, "%s%s", dirname(base), relpath);
    free(base);

    Py_SetPythonHome(path);
}



/**
 * This is the python command, and all it does is to modify the path to the
 * python library, and start python.
 */
int EXPORT renpython_main(int argc, char **argv) {

    Py_SetProgramName(argv[0]);

    /* Linux: The executable is lib/linux-(arch)/python. */
    set_python_home(argv[0], "/../..");

    Py_OptimizeFlag = 2;
    Py_NoUserSiteDirectory = 1;

    init_librenpy();
    return Py_Main(argc, argv);
}


/**
 * This is called from the launcher executable, to start Ren'Py running.
 */
int EXPORT launcher_main(int argc, char **argv) {

    Py_SetProgramName(argv[0]);

#ifdef MS_WINDOWS
    set_python_home(argv[0], "");
#endif

    char **new_argv = (char **) alloca((argc + 1) * sizeof(char *));

    new_argv[0] = argv[0];
    new_argv[1] = strdup(argv[0]);

    for (int i = 1; i < argc; i++) {
        new_argv[i + 1] = argv[i];
    }

    int l = strlen(new_argv[1]);
    new_argv[1][l - 3] = 'p';
    new_argv[1][l - 2] = 'y';
    new_argv[1][l - 1] = 0;

    Py_OptimizeFlag = 2;
    Py_IgnoreEnvironmentFlag = 1;
    Py_NoUserSiteDirectory = 1;

    return Py_Main(argc + 1, new_argv);
}
