#include <windows.h>
#include <stdio.h>
#include <wchar.h>

int __declspec(dllimport) renpython_main_wide(int argc, wchar_t **argv);

int wmain( int argc, wchar_t *argv[ ], wchar_t *envp[ ] ) {
    return renpython_main_wide(argc, argv);
}
