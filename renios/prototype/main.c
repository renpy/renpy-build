#include <stdio.h>

int launcher_main(int argc, char **argv);
int SDL_UIKitRunApp(int, char **, int (*)(int, char**));

int main(int argc, char **argv) {
    return SDL_UIKitRunApp(argc, argv, launcher_main);
}

