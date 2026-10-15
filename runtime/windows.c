#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <shlwapi.h>

#include <stdio.h>

typedef enum {
    RENPY_OK = 0,
    RENPY_ERR_OLD_WINDOWS = 1,
    RENPY_ERR_NO_UTF8_ACP = 2,
    RENPY_ERR_MODULE_PATH = 3,
    RENPY_ERR_NO_DIR = 4,
    RENPY_ERR_PATH_TOO_LONG = 5,
    RENPY_ERR_CONVERT_PATH = 6,
    RENPY_ERR_SET_DLL_DIRS = 7,
    RENPY_ERR_ADD_DLL_DIR = 8,
    RENPY_ERR_NO_RUNTIME_DLL = 9
} RenpyError;

int setup_dll_directory() {
    RenpyError error = RENPY_OK;

    char message[128];
    char dll_path[MAX_PATH];
    wchar_t wide_path[MAX_PATH];

    OSVERSIONINFOEXW info = { sizeof(info) };
    info.dwMajorVersion = 10;
    DWORDLONG mask = VerSetConditionMask(0, VER_MAJORVERSION, VER_GREATER_EQUAL);
    if (!VerifyVersionInfoW(&info, VER_MAJORVERSION, mask)) {
        error = RENPY_ERR_OLD_WINDOWS;
        goto cleanup;
    }

    if (GetACP() != CP_UTF8) {
        error = RENPY_ERR_NO_UTF8_ACP;
        goto cleanup;
    }

    DWORD length = GetModuleFileNameA(NULL, dll_path, sizeof(dll_path));
    if (length == 0 || length >= sizeof(dll_path)) {
        error = RENPY_ERR_MODULE_PATH;
        goto cleanup;
    }

    if (!PathRemoveFileSpecA(dll_path)) {
        error = RENPY_ERR_NO_DIR;
        goto cleanup;
    }

    if (!PathAppendA(dll_path, "librenpython.dll")) {
        error = RENPY_ERR_PATH_TOO_LONG;
        goto cleanup;
    }

    if (!PathFileExistsA(dll_path)) {
        if (
            !PathRemoveFileSpecA(dll_path) ||
            !PathAppendA(dll_path, "lib") ||
            !PathAppendA(dll_path, "py3-" PLATFORM "-" ARCH) ||
            !PathAppendA(dll_path, "librenpython.dll")
        ) {
            error = RENPY_ERR_PATH_TOO_LONG;
            goto cleanup;
        }
    }

    if (!PathFileExistsA(dll_path)) {
        error = RENPY_ERR_NO_RUNTIME_DLL;
        goto cleanup;
    }

    if (!PathRemoveFileSpecA(dll_path)) {
        error = RENPY_ERR_NO_DIR;
        goto cleanup;
    }

    int wide_length = MultiByteToWideChar(CP_UTF8, MB_ERR_INVALID_CHARS, dll_path, -1, wide_path, MAX_PATH);
    if (wide_length == 0) {
        error = RENPY_ERR_CONVERT_PATH;
        goto cleanup;
    }

    if (!SetDefaultDllDirectories(LOAD_LIBRARY_SEARCH_SYSTEM32 | LOAD_LIBRARY_SEARCH_USER_DIRS)) {
        error = RENPY_ERR_SET_DLL_DIRS;
        goto cleanup;
    }

    if (AddDllDirectory(wide_path) == NULL) {
        error = RENPY_ERR_ADD_DLL_DIR;
        goto cleanup;
    }

    if (error == RENPY_OK) {
        return 0;
    }

cleanup:
    snprintf(message, sizeof(message), "Failed to initialize the Ren'Py runtime. (Error code %d)", error);
    MessageBoxA(NULL, message, "Ren'Py Runtime Error", MB_OK | MB_ICONERROR);
    return error;
}
