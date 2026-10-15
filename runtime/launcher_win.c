__declspec(dllimport) int launcher_main(int argc, char **argv);
int setup_dll_directory();

int main(int argc, char **argv) {
    int result = setup_dll_directory();
    if (result != 0) {
        return result;
    }

    return launcher_main(argc, argv);
}
