#include <stdio.h>
#include <string.h>

#include <windows.h>
#include "r440/nvapi.h"

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


int main(int argc, char **argv) {

    load_nvapi();

    printf("%s\n", error);
}