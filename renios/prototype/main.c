#include <stdio.h>

int launcher_main(int argc, char **argv);

int SDL_main(int argc, char **argv) {
    return launcher_main(argc, argv);
}
