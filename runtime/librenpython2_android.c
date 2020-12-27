#include "SDL.h"
#include "SDL_image.h"
#include "Python.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <jni.h>
#include "android/log.h"
#include "jniwrapperstuff.h"

void init_librenpy(void);

/* Environment Handling *******************************************************/
extern char **environ;

/**
 * This is true if the environment is malfunctioning and we need to work
 * around that.
 */
static int environ_workaround = 0;


static void init_environ() {
    setenv("TEST_ENV_VAR", "The test worked.", 1);

    if (*environ) {
        return;
    }

    environ_workaround = 1;
    environ = calloc(50, sizeof(char *));
}

static void setenv_workaround(const char *c_variable, const char *c_value) {
    setenv(c_variable, c_value, 1);

    char buf[2048];
    char **e = environ;

    if (environ_workaround) {
        snprintf(buf, 2048, "%s=%s", c_variable, c_value);

        while (*e) {
            e++;
        }

        *e = strdup(buf);
    }
}

JNIEXPORT void JNICALL JAVA_EXPORT_NAME(PythonSDLActivity_nativeSetEnv) (
        JNIEnv*  env, jobject thiz,
        jstring variable,
        jstring value) {

    jboolean iscopy;
    const char *c_variable = (*env)->GetStringUTFChars(env, variable, &iscopy);
    const char *c_value  = (*env)->GetStringUTFChars(env, value, &iscopy);

    setenv_workaround(c_variable, c_value);
}

/* The Androidembed module ****************************************************/

SDL_Window *window = NULL;

#define LOG(x) __android_log_write(ANDROID_LOG_INFO, "python", (x))

static PyObject *androidembed_log(PyObject *self, PyObject *args) {
    char *logstr = NULL;
    if (!PyArg_ParseTuple(args, "s", &logstr)) {
        return NULL;
    }
    LOG(logstr);
    Py_RETURN_NONE;
}

static PyObject *androidembed_close_window(PyObject *self, PyObject *args) {
    char *logstr = NULL;
    if (!PyArg_ParseTuple(args, "")) {
        return NULL;
    }

    if (window) {
		SDL_DestroyWindow(window);
		window = NULL;
    }

    Py_RETURN_NONE;
}

static PyMethodDef AndroidEmbedMethods[] = {
	    {"log", androidembed_log, METH_VARARGS, "Log on android platform."},
	    {"close_window", androidembed_close_window, METH_VARARGS, "Close the initial window."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initandroidembed(void) {
    (void) Py_InitModule("androidembed", AndroidEmbedMethods);
}

static struct _inittab inittab[] = {
               { "androidembed",  initandroidembed },
               { NULL, NULL },
};

/* Python Startup *************************************************************/

int start_python(void) {
    char *private = getenv("ANDROID_PRIVATE");

    chdir(private);

    /* The / is required to stop python from doing a search that causes
     * a crash on ARC.
     */
    char python[2048];
    snprintf(python, 2048, "%s/python", private);

    Py_SetProgramName(python);
    Py_SetPythonHome(private);

    char *args[] = { python, "main.py", NULL };

    Py_OptimizeFlag = 2;
    Py_IgnoreEnvironmentFlag = 1;
    Py_NoUserSiteDirectory = 1;

    PyImport_ExtendInittab(inittab);

    init_librenpy();

    return Py_Main(2, args);
}


void call_prepare_python(void) {
	JNIEnv* env = (JNIEnv*) SDL_AndroidGetJNIEnv();
	jobject activity = (jobject) SDL_AndroidGetActivity();
	jclass clazz = (*env)->GetObjectClass(env, activity);
	jmethodID method_id = (*env)->GetMethodID(env, clazz, "preparePython", "()V");
	(*env)->CallVoidMethod(env, activity, method_id);
	(*env)->DeleteLocalRef(env, activity);
	(*env)->DeleteLocalRef(env, clazz);
}

int SDL_main(int argc, char **argv) {
	SDL_Surface *surface;
	SDL_RWops *rwops = NULL;
	SDL_Surface *presplash = NULL;
	SDL_Surface *presplash2 = NULL;
	SDL_Rect pos;
	SDL_Event event;

	Uint32 pixel;

	init_environ();
    setenv_workaround("RENPY_PLATFORM", PLATFORM "-" ARCH);
    SDL_SetHint(SDL_HINT_ANDROID_BLOCK_ON_PAUSE, "0");

	if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
	    return 1;
	}

	IMG_Init(IMG_INIT_JPG|IMG_INIT_PNG);

	window = SDL_CreateWindow("presplash", 0, 0, 0, 0, SDL_WINDOW_FULLSCREEN_DESKTOP| SDL_WINDOW_SHOWN);
	surface = SDL_GetWindowSurface(window);
	pixel = SDL_MapRGB(surface->format, 128, 128, 128);

	rwops = SDL_RWFromFile("android-presplash.png", "r");

	if (!rwops) {
		rwops = SDL_RWFromFile("android-presplash.jpg", "r");
	}

	if (!rwops) goto done;

	presplash = IMG_Load_RW(rwops, 1);

    if (!presplash) goto done;

	presplash2 = SDL_ConvertSurfaceFormat(presplash, SDL_PIXELFORMAT_RGB888, 0);
	Uint8 *pp = (Uint8 *) presplash2->pixels;

#if SDL_BYTEORDER == SDL_LIL_ENDIAN
	pixel = SDL_MapRGB(surface->format, pp[2], pp[1], pp[0]);
#else
	pixel = SDL_MapRGB(surface->format, pp[0], pp[1], pp[2]);
#endif

	SDL_FreeSurface(presplash2);

done:


	while (SDL_WaitEventTimeout(&event, 500)) {

	    if (event.type == SDL_WINDOWEVENT) {

	        if (event.window.event == SDL_WINDOWEVENT_RESIZED || event.window.event == SDL_WINDOWEVENT_SHOWN) {
	            break;
	        }
	    }
	}

    SDL_FillRect(surface, NULL, pixel);

    if (presplash) {
        pos.x = (surface->w - presplash->w) / 2;
        pos.y = (surface->h - presplash->h) / 2;
        SDL_BlitSurface(presplash, NULL, surface, &pos);
        SDL_FreeSurface(presplash);
    }

    SDL_UpdateWindowSurface(window);
    SDL_PumpEvents();
    SDL_UpdateWindowSurface(window);
    SDL_PumpEvents();
    SDL_UpdateWindowSurface(window);
    SDL_PumpEvents();
    SDL_UpdateWindowSurface(window);
    SDL_PumpEvents();

    SDL_GL_MakeCurrent(NULL, NULL);

	call_prepare_python();

	return start_python();
}
