#include <stdio.h>

int launcher_main(int argc, char **argv);

int main(int argc, char **argv) {

    for (int i = 0; i < argc; i++) {
        printf("%d %s\n", i, argv[i]);
    }

    return launcher_main(argc, argv);
}
