#include <stdio.h>

int launcher_main(int argc, char **argv);
int SDL_RunApp(int, char **, int (*)(int, char**), void *);

int main(int argc, char **argv) {
    return SDL_RunApp(argc, argv, launcher_main, NULL);
}
