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


static PyMethodDef AndroidEmbedMethods[] = {
    {"log", androidembed_log, METH_VARARGS, "Log on android platform."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef androidembed_module =
{
    PyModuleDef_HEAD_INIT,
    "androidembed", /* name of module */
    "",          /* module documentation, may be NULL */
    -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    AndroidEmbedMethods
};

PyMODINIT_FUNC PyInit_androidembed(void) {
    return PyModule_Create(&androidembed_module);
}

static struct _inittab inittab[] = {
   { "androidembed",  PyInit_androidembed },
   { NULL, NULL },
};

/* Python Startup *************************************************************/

int start_python(void) {
    PyPreConfig preconfig;
    PyConfig config;

    PyImport_ExtendInittab(inittab);
    init_librenpy();

    char *private = getenv("ANDROID_PRIVATE");
    chdir(private);

    char python[2048];
    snprintf(python, 2048, "%s/python", private);

    char main_py[2048];
    snprintf(main_py, 2048, "%s/main.py", private);

    int argc = 2;
    char *argv[] = { python, main_py, NULL };

    PyPreConfig_InitPythonConfig(&preconfig);

    preconfig.utf8_mode = 1;
    preconfig.use_environment = 0;

    Py_PreInitializeFromBytesArgs(&preconfig, argc, argv);

    PyConfig_InitPythonConfig(&config);

    config.home = Py_DecodeLocale(private, NULL);
    config.user_site_directory = 0;
    config.parse_argv = 1;
    config.install_signal_handlers = 1;

    PyConfig_SetBytesArgv(&config, argc, argv);
    Py_InitializeFromConfig(&config);

    int rv = Py_RunMain();

    return rv;
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

    init_environ();
    setenv_workaround("RENPY_PLATFORM", PLATFORM "-" ARCH);
    SDL_SetHint(SDL_HINT_ANDROID_BLOCK_ON_PAUSE, "0");

	call_prepare_python();

	return start_python();
}
