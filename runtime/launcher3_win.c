#define WINDOWS_LEAN_AND_MEAN
#include <windows.h>
#include <versionhelpers.h>

#include <stdio.h>
#include <string.h>
#include <libgen.h>
#include <wchar.h>

#define str(s) #s

static wchar_t *widedirname(wchar_t *s) {
    wchar_t *rv = wcsdup(s);
    wchar_t *p = rv + wcslen(rv);

    while (1) {
        p--;

        if (p == rv) {
            return L".";
        }

        if (*p == '\\' || *p == '/') {
            *p = 0;
            break;
        }
    }

    return rv;

}

int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
    wchar_t path[4096];
    HMODULE library;

    wchar_t *platform = L"" PLATFORM;
    wchar_t *arch = L"" ARCH;

    if (!IsWindowsVistaOrGreater()) {
        MessageBox(NULL, "This program requires Windows Vista or greater to run.", "Version Not Supported", MB_OK);
        return 0;
    }

    swprintf(path, 4096, L"%ls\\lib\\py3-%ls-%ls", widedirname(__wargv[0]), platform, arch);
    SetDllDirectoryW(path);
    library = LoadLibrary("librenpython.dll");

    int (*launcher_main_wide)(int, wchar_t **) = (int (*)(int, wchar_t **)) GetProcAddress(library, "launcher_main_wide");

    return launcher_main_wide(__argc, __wargv);
}
