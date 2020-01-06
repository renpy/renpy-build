#include <stdio.h>
#include <string.h>
#include <libgen.h>
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

    init_librenpy();
    return Py_Main(argc, argv);
}
