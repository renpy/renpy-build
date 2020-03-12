#include <stdio.h>

int renpython_main(int argc, char **argv);

int main(int argc, char **argv) {

    for (int i = 0; i < argc; i++) {
        printf("%d %s\n", i, argv[i]);
    }

    return renpython_main(argc, argv);
}
