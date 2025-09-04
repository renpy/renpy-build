#include <stdio.h>
#include <string.h>

#include <windows.h>

#include "r440/nvapi.h"
#include "r440/NvApiDriverSettings.h"

static char *error = NULL;
static void *(*QueryInterface)(unsigned int);

typedef NvAPI_Status (*InitializeType)();
typedef NvAPI_Status (*DRS_CreateSessionType)(NvDRSSessionHandle *);
typedef NvAPI_Status (*DRS_DestroySessionType)(NvDRSSessionHandle);
typedef NvAPI_Status (*DRS_LoadSettingsType)(NvDRSSessionHandle);
typedef NvAPI_Status (*DRS_GetBaseProfileType)(NvDRSSessionHandle, NvDRSProfileHandle *);
typedef NvAPI_Status (*DRS_GetSettingType)(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NvU32 settingId, NVDRS_SETTING *pSetting);
typedef NvAPI_Status (*DRS_SetSettingType)(NvDRSSessionHandle hSession, NvDRSProfileHandle hProfile, NVDRS_SETTING *pSetting);
typedef NvAPI_Status (*DRS_SaveSettingsType)(NvDRSSessionHandle);

static InitializeType Initialize;
static DRS_CreateSessionType DRS_CreateSession;
static DRS_DestroySessionType DRS_DestroySession;
static DRS_LoadSettingsType DRS_LoadSettings;
static DRS_GetBaseProfileType DRS_GetBaseProfile;
static DRS_GetSettingType DRS_GetSetting;
static DRS_SetSettingType DRS_SetSetting;
static DRS_SaveSettingsType DRS_SaveSettings;

/**
 * This queries for the named interface. If found, it will load
 * it, otherwise it sets the error message.
 */
static void *load_interface(char *name, unsigned int id) {
    void *rv = QueryInterface(id);

    if (!rv) {
        char msg[128];
        snprintf(msg, 128, "%s not found.", name);
        error = strdup(msg);
    }

    return rv;
}

static int loaded = 0;

static void load_nvapi() {

    if (loaded) {
        return;
    }

    loaded = 1;

    HMODULE nvlib = LoadLibrary("nvapi64");

    if (!nvlib) {
        nvlib = LoadLibrary("nvapi");
    }

    if (!nvlib) {
        error = "Couldn't load nvlib.";
        return;
    }

    QueryInterface = (void *(*)(unsigned int)) GetProcAddress(nvlib, "nvapi_QueryInterface");

    if (!QueryInterface) {
        error = "Couldn't find QueryInterface";
        return;
    }

    Initialize = load_interface("Initialize", 0x0150e828);
    DRS_CreateSession = load_interface("DRS_CreateSession", 0x0694d52e);
    DRS_DestroySession = load_interface("DRS_DestroySession", 0xdad9cff8);
    DRS_LoadSettings = load_interface("DRS_LoadSettings", 0x375dbd6b);
    DRS_GetBaseProfile = load_interface("DRS_GetBaseProfile", 0xda8466a0);
    DRS_GetSetting = load_interface("DRS_GetSetting", 0x73bf8338);
    DRS_SetSetting = load_interface("DRS_SetSetting", 0x577dd202);
    DRS_SaveSettings = load_interface("DRS_SaveSettings", 0xfcbc7e14);

}

static void check(const char *func, NvAPI_Status ret) {
    if (ret) {
        char msg[128];
        snprintf(msg, 128, "%s() = %d.", func, ret);
        error = strdup(msg);
    }
}

static unsigned int original = OGL_THREAD_CONTROL_ENABLE;
static unsigned int got_original = 0;
static unsigned int should_set = 0;

void set_thread_optimization(unsigned value) {
    int ret;
    NvDRSSessionHandle hSession;
    NvDRSProfileHandle hProfile;
    NVDRS_SETTING setting;
    setting.version = NVDRS_SETTING_VER;

    load_nvapi();

    if (error) {
        return;
    }

    check("Initialize", Initialize());
    if (error) {
        return;
    }

    check("DRS_CreateSession", DRS_CreateSession(&hSession));
    if (error) {
        return;
    }

    check("DRS_LoadSettings", DRS_LoadSettings(hSession));
    if (error) {
        goto fail;
    }

    check("DRS_GetBaseProfile", DRS_GetBaseProfile(hSession, &hProfile));
    if (error) {
        goto fail;
    }

    /* This can fail, if the setting hasn't been set yet. */
    DRS_GetSetting(hSession, hProfile, OGL_THREAD_CONTROL_ID, &setting);

    if (!got_original) {
        original = setting.u32CurrentValue;
        got_original = 1;

        if (original != value) {
            should_set = 1;
        }
    }

    if (!should_set) {
        return;
    }

    if (original < 1 || original > 16) {
        original = OGL_THREAD_CONTROL_ENABLE;
    }

    setting.version = NVDRS_SETTING_VER;
    setting.settingId = OGL_THREAD_CONTROL_ID;
    setting.settingType = NVDRS_DWORD_TYPE;
    setting.u32CurrentValue = value;

    check("DRS_SetSetting", DRS_SetSetting(hSession, hProfile, &setting));
    if (error) {
        goto fail;
    }

    check("DRS_SaveSettings", DRS_SaveSettings(hSession));
    if (error) {
        goto fail;
    }

fail:
    DRS_DestroySession(hSession);
}

void disable_thread_optimization() {
    set_thread_optimization(2);
}

void restore_thread_optimization() {
    if (should_set) {
        set_thread_optimization(original);
    }
}

char *get_nvdrs_error() {
    return error;
}

// int main(int argc, char **argv) {

//     disable_thread_optimization();
//     restore_thread_optimization();

//     printf("original: %d\n", original);
//     printf("result: %s\n", error);
// }
