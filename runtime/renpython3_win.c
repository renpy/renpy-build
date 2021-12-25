#include <wchar.h>

int __declspec(dllimport) renpython_main_wide(int argc, char **argv);

int WinMain(int argc, char **argv) {
    return renpython_main_wide(argc, argv);
}
