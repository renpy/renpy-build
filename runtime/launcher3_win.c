#define WINDOWS_LEAN_AND_MEAN
#include <windows.h>
#include <versionhelpers.h>

#include <stdio.h>
#include <string.h>
#include <libgen.h>

#define str(s) #s

int main(int argc, char **argv) {
    char *base;
    char path[4096];
    HMODULE library;

    if (!IsWindowsVistaOrGreater()) {
        MessageBox(NULL, "This program requires Windows Vista or greater to run.", "Version Not Supported", MB_OK);
        return 0;
    }

    base = strdup(argv[0]);
    snprintf(path, 4096, "%s\\lib\\" PLATFORM "-" ARCH, dirname(base));
    free(base);

    SetDllDirectory(path);
    library = LoadLibrary("librenpython.dll");

    int (*launcher_main)(int, char **) = (int (*)(int, char **)) GetProcAddress(library, "launcher_main");

    return launcher_main(argc, argv);

}
