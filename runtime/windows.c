#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {
    RENPY_OK = 0,
    RENPY_ERR_OLD_WINDOWS = 1,
    RENPY_ERR_NO_RUNTIME_DLL = 2,
    RENPY_ERR_MODULE_PATH = 3,
    RENPY_ERR_NO_MEMORY = 4,
    RENPY_ERR_SET_DLL_DIRS = 5
} RenpyError;

static void report(RenpyError error, DWORD last_error) {
    char message[256];

    switch (error) {
    case RENPY_ERR_OLD_WINDOWS:
        snprintf(message, sizeof(message),
            "Failed to initialize the Ren'Py runtime.\n\n"
            "Ren'Py requires Windows 10 version 1903 or later.");
        break;
    case RENPY_ERR_NO_RUNTIME_DLL:
        snprintf(message, sizeof(message),
            "Failed to initialize the Ren'Py runtime.\n\n"
            "Could not find librenpython.dll.");
        break;
    default:
        snprintf(message, sizeof(message),
            "Failed to initialize the Ren'Py runtime.\n\n"
            "Unable to set up the runtime.\n\n"
            "(Error code %d, Windows error %lu)",
            (int) error, (unsigned long) last_error);
        break;
    }

#ifdef RENPY_CONSOLE
    // python.exe runs from scripts and CI; a modal dialog would hang them.
    fprintf(stderr, "%s\n", message);
#else
    MessageBoxA(NULL, message, "Ren'Py Runtime Error", MB_OK | MB_ICONERROR);
#endif
}

static char *join(const char *dir, const char *name) {
    size_t size = strlen(dir) + strlen(name) + 2;
    char *rv = (char *) malloc(size);
    if (rv) {
        snprintf(rv, size, "%s\\%s", dir, name);
    }
    return rv;
}

static int file_exists(const char *path) {
    DWORD attributes = GetFileAttributesA(path);
    return attributes != INVALID_FILE_ATTRIBUTES && !(attributes & FILE_ATTRIBUTE_DIRECTORY);
}

int setup_dll_directory(void) {
    RenpyError error = RENPY_OK;
    DWORD last_error = 0;

    char *exe_dir = NULL;
    char *runtime_dir = NULL;
    char *dll_path = NULL;
    const char *dll_dir = NULL;
    char *slash;
    DWORD capacity = MAX_PATH;

    OSVERSIONINFOEXW info = { sizeof(info) };
    info.dwMajorVersion = 10;
    DWORDLONG mask = VerSetConditionMask(0, VER_MAJORVERSION, VER_GREATER_EQUAL);
    if (!VerifyVersionInfoW(&info, VER_MAJORVERSION, mask)) {
        error = RENPY_ERR_OLD_WINDOWS;
        goto done;
    }

    // activeCodePage from the manifest is honored on Windows 10 1903+ only.
    if (GetACP() != CP_UTF8) {
        error = RENPY_ERR_OLD_WINDOWS;
        goto done;
    }

    // Path of the executable, without a MAX_PATH limit.
    for (;;) {
        char *grown = (char *) realloc(exe_dir, capacity);
        if (grown == NULL) {
            error = RENPY_ERR_NO_MEMORY;
            goto done;
        }
        exe_dir = grown;

        DWORD length = GetModuleFileNameA(NULL, exe_dir, capacity);
        if (length == 0) {
            error = RENPY_ERR_MODULE_PATH;
            last_error = GetLastError();
            goto done;
        }
        if (length < capacity) {
            break;
        }
        capacity *= 2;
    }

    slash = strrchr(exe_dir, '\\');
    if (slash == NULL) {
        error = RENPY_ERR_MODULE_PATH;
        goto done;
    }
    *slash = '\0';

    dll_dir = exe_dir;
    dll_path = join(dll_dir, "librenpython.dll");
    if (dll_path == NULL) {
        error = RENPY_ERR_NO_MEMORY;
        goto done;
    }

    if (!file_exists(dll_path)) {
        free(dll_path);

        runtime_dir = join(exe_dir, "lib\\py3-" PLATFORM "-" ARCH);
        dll_path = runtime_dir ? join(runtime_dir, "librenpython.dll") : NULL;
        if (dll_path == NULL) {
            error = RENPY_ERR_NO_MEMORY;
            goto done;
        }

        if (!file_exists(dll_path)) {
            error = RENPY_ERR_NO_RUNTIME_DLL;
            goto done;
        }

        dll_dir = runtime_dir;
    }

    if (
        !SetDefaultDllDirectories(LOAD_LIBRARY_SEARCH_SYSTEM32 | LOAD_LIBRARY_SEARCH_USER_DIRS) ||
        !SetDllDirectoryA(dll_dir)
    ) {
        error = RENPY_ERR_SET_DLL_DIRS;
        last_error = GetLastError();
        goto done;
    }

done:
    free(exe_dir);
    free(runtime_dir);
    free(dll_path);

    if (error != RENPY_OK) {
        report(error, last_error);
        return (int) error;
    }

    return 0;
}
