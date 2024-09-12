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

int wmain(int argc, wchar_t *argv[], wchar_t *envp[]) {
    wchar_t path[4096];
    HMODULE library;

    wchar_t *platform = L"" PLATFORM;
    wchar_t *arch = L"" ARCH;

    if (!IsWindows10OrGreater()) {
        MessageBox(NULL, L"This program requires Windows 10 or greater to run.", L"Version Not Supported", MB_OK);
        return 0;
    }

    swprintf(path, 4096, L"%ls\\lib\\py3-%ls-%ls", widedirname(argv[0]), platform, arch);

    SetDllDirectoryW(path);
    library = LoadLibrary(L"librenpython.dll");

    int (*launcher_main_wide)(int, wchar_t **) = (int (*)(int, wchar_t **)) GetProcAddress(library, "launcher_main_wide");

    return launcher_main_wide(argc, argv);
}
