#include <windows.h>

int __declspec(dllimport) renpython_main_wide(int argc, wchar_t **argv);

int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {
    return renpython_main_wide(__argc, __wargv);
}
