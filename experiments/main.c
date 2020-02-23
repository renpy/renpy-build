#include <stdio.h>
#include <SDL.h>
#include <SDL_opengles2.h>
#include <unistd.h>

int main(int argc, char **argv) {
    int pass = 0;
    SDL_GLContext gl_context;
    SDL_Window *window;
    SDL_Renderer* renderer;

    SDL_Init(SDL_INIT_EVERYTHING);
    SDL_Log("Hello, world.");

    window = SDL_CreateWindow("presplash", 0, 0, 0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP|SDL_WINDOW_SHOWN);

    renderer = SDL_CreateRenderer(window, -1, 0);

    for (pass = 0; pass < 50; pass++) {

        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
//        SDL_UpdateWindowSurface(window);

        SDL_Delay(100);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);

    window = SDL_CreateWindow("presplash", 0, 0, 0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP|SDL_WINDOW_SHOWN|SDL_WINDOW_OPENGL);

    SDL_GL_SetAttribute(SDL_GL_RED_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_GREEN_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_BLUE_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_ALPHA_SIZE, 8);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 2);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 0);
    SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_ES);



    gl_context = SDL_GL_CreateContext(window);

    while (1) {

        float blue = (pass % 100) / 100.0;

        glClearColor(0.0, 0.0, blue, 1.0);
        glClear(GL_COLOR_BUFFER_BIT);

        SDL_GL_SwapWindow(window);

        if (1) {
            SDL_Event ev;
            SDL_WaitEventTimeout(&ev, 10);
            SDL_Log("Event %x, pass %d", ev.type, pass);

            if (ev.type == SDL_APP_WILLENTERBACKGROUND) {
                SDL_Log("WILLENTERBACKGROUND");
                usleep(2000000);
                SDL_Log("SLEEP DONE");

                while (1) {
                    SDL_WaitEvent(&ev);

                    if (ev.type == SDL_APP_DIDENTERFOREGROUND) {
                        SDL_Log("DIDENTERFOREGROUND.");
                        break;
                    } else if (SDL_APP_TERMINATING) {
                        SDL_Log("TERMINATING");
                        exit(0);
                    } else {
                        SDL_Log("SLEEP EVENT: %x", ev.type);
                    }
                }

            }


            pass += 1;
        }


       pass += 1;

    }

    SDL_GL_DeleteContext(gl_context);

}
