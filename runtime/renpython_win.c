__declspec(dllimport) int renpython_main(int argc, char **argv);
int setup_dll_directory();

int main(int argc, char **argv) {
    int result = setup_dll_directory();
    if (result != 0) {
        return result;
    }

    return renpython_main(argc, argv);
}
