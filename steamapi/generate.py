#!/usr/bin/env python3

import json
import pprint
import re
import io
import sys
import argparse

# The file that the generated code will be written to.
out = None # type: io.TextIOBase

def p(s):
    """
    Writes `s` to the output file, and to stdout for debugging purposes.
    """

    out.write(s + "\n")
    # sys.stdout.write(s + "\n")

# A mapping from a type to the corresponding ctypes constructor.
MAPPINGS = {
    "char" : "c_byte",
    "unsigned char" : "c_ubyte",
    "signed char" : "c_byte",
    "short" : "c_short",
    "signed_short" : "c_short",
    "unsigned short" : "c_ushort",
    "int" : "c_int",
    "signed int" : "c_int",
    "unsigned int" : "c_uint",
    "int32_t" : "c_int",
    "intptr_t" : "POINTER(c_int)",
    "long" : "c_long",
    "signed long" : "c_long",
    "unsigned long" : "c_ulong",
    "long long" : "c_longlong",
    "signed long long" : "c_longlong",
    "int64_t" : "c_longlong",
    "unsigned long long" : "c_ulonglong",
    "char *" : "c_char_p",
    "void *" : "c_void_p",
    "CGameID" : "c_ulonglong",
    "CSteamID" : "c_ulonglong",
    "bool" : "c_bool",
    "float" : "c_float",
    "double" : "c_double",
    "void" : "None",
    "size_t" : "c_size_t",
    "SteamAPIWarningMessageHook_t" : "c_void_p",
    "ISteamHTMLSurface::EHTMLMouseButton" : "c_int",
    "ISteamHTMLSurface::EHTMLKeyModifiers" : "c_int",
    "SteamDatagramRelayAuthTicket *" : "c_void_p",
    "ISteamNetworkingConnectionSignaling *" : "c_void_p",
    "ISteamNetworkingSignalingRecvContext *" : "c_void_p",
    "ScePadTriggerEffectParam *" : "c_void_p",
}

def unprefix(name):
    """"
    Removes the SteamAPI_ prefix from a name.
    """

    return name.partition("SteamAPI_")[2]


def map_type(name):
    """
    Given a type name, name, maps it to a ctypes type object.
    """

    rv = MAPPINGS.get(name, None)
    if rv is not None:
        return rv

    name = name.replace("&", "*")

    if name.startswith("const "):
        rv = map_type(name[6:])

    elif name.endswith("const"):
        rv = map_type(name[:-5])

    elif name.endswith(" *"):
        mapped = map_type(name[:-2])
        rv = f"POINTER({mapped})"

    elif name.endswith(" **"):
        mapped = map_type(name[:-1])
        rv = f"POINTER({mapped})"

    elif name.endswith("]"):
        m = re.match(r"(.*) \[(\d+)\]", name)
        if m is None:
            raise Exception(f"Couldn't map type {name}")

        mapped = map_type(m.group(1))
        count = m.group(2)

        rv = f"({mapped} * {count})"

    elif "(*)" in name:
        return "c_void_p"

    else:
        raise Exception(f"Couldn't map type {name!r}")

    MAPPINGS[name] = rv
    return rv



def typedef(typedefs):
    """
    Processes the typedef object in steam_api.json.
    """


    for d in typedefs:


        type = map_type(d["type"])
        typedef = d["typedef"]

        MAPPINGS[typedef] = type



def consts(consts):
    """
    Processes the constants object in steam_api.json.
    """

    namespace = { }

    for c in consts:
        constname = c["constname"]
        consttype = c["consttype"]
        constval = c["constval"]

        # Correct various values that won't evaluate in python.
        if constval == "( SteamItemInstanceID_t ) ~ 0":
            constval = "-1"
        elif constval == "( ( uint32 ) 'd' << 16U ) | ( ( uint32 ) 'e' << 8U ) | ( uint32 ) 'v'":
            constval = "6579574"
        elif constval == "600.f":
            constval = "600.0"
        else:
            constval = re.sub(r"(0x[0-9a-fA-F]*)ull", r"\1", constval)

        # Evaluate the result, and place it into the namespace.
        value = eval(constval, namespace, namespace)
        namespace[constname] = value

        # Generate.
        mapped = map_type(consttype)

        if isinstance(value, float):
            p(f"{constname} = {mapped}({value})")
        elif value > 0:
            p(f"{constname} = {mapped}(0x{value:x})")
        else:
            p(f"{constname} = {mapped}({value})")

def enums(enums):

    p("")
    p("")
    p("# Enums")

    for e in enums:
        enumname = e["enumname"]
        values = e["values"]

        p("")
        p(f"class {enumname}(c_int):")
        p("    pass")

        p("")

        for v in values:
            p(f"{v['name']} = {enumname}({v['value']})")

        MAPPINGS[enumname] = enumname

        if "fqname" in e:
            MAPPINGS[e["fqname"]] = enumname

def structs(structs):

    for s in structs:
        structname = s.get("struct", None) or s["classname"]
        fields = s["fields"]
        methods = s.get("methods", [])

        p("")
        p(f"class {structname}(Structure):")
        p("    _pack_ = PACK")
        p("    _fields_ = [")

        for f in fields:
            fieldname = f["fieldname"]
            fieldtype = f["fieldtype"]

            if fieldtype == "SteamInputActionEvent_t::AnalogAction_t":
                continue

            mapped = map_type(fieldtype)

            p(f"        ({fieldname!r}, {mapped}),")

        p("    ]")

        if "callback_id" in s:
            p(f"    callback_id = {s['callback_id']}")

        for m in methods:

            flat = m["methodname_flat"]
            flat = unprefix(flat)

            methodname = flat.partition("_")[-1]

            params = ", ".join(p["paramname"] for p in m["params"])

            p("")
            p(f"    def {methodname}(self, {params}):")
            p(f"        return {flat}(byref(self), {params}) # type: ignore")


        MAPPINGS[structname] = structname

def callback_by_id(structs):

    p("")
    p("callback_by_id = {")

    for s in structs:
        p(f"{s['callback_id']} : {s['struct']},")

    p("}")


def flatmethod(m, methodname, flat, interface):
    short = unprefix(flat)

    if not short:
        return

    paramtypes = ", ".join(map_type(p["paramtype"]) for p in m["params"])
    returntype = map_type(m["returntype"])

    p("")
    p(f"    global {short}")
    p(f"    {short} = dll.{flat}")
    p(f"    {short}.argtypes = [ POINTER({ interface }), {paramtypes} ]")
    p(f"    {short}.restype = {returntype}")


def flataccessor(a, name, flat, interface):
    short = unprefix(flat)

    if not short:
        return

    p("")
    p(f"    global {short}")
    p(f"    {short} = dll.{flat}")
    p(f"    {short}.argtypes = [ ]")
    p(f"    {short}.restype = POINTER({interface})")


def fixedmethod(name, argtypes, restype):

    short = unprefix(name)

    if not short:
        return

    p("")
    p(f"    global {short}")
    p(f"    {short} = dll.{name}")
    p(f"    {short}.argtypes = [ { argtypes } ]")
    p(f"    {short}.restype = { restype }")


def stubmethod(m, methodname, flat):
    short = unprefix(flat)

    if not short:
        return

    p("")
    p(f"{short} = not_ready")


def stubaccessor(a, name, flat, interface):
    short = unprefix(flat)

    if not short:
        return

    p("")
    p(f"{short} = not_ready")
    p("")
    p(f"def {name}(): # type: () -> {interface}")
    p(f"    return {short}().contents")


def stubfixedmethod(name, argtypes, restype):

    short = unprefix(name)

    if not short:
        return

    p("")
    p(f"{short} = not_ready")


FIXED_METHODS = [
    ("SteamAPI_InitFlat", "c_char_p", "ESteamAPIInitResult"),
    ("SteamAPI_Shutdown", "", "None"),
    ("SteamAPI_RestartAppIfNecessary", "c_uint", "c_bool"),
    ("SteamAPI_ReleaseCurrentThreadMemory", "", "None"),
    ("SteamAPI_WriteMiniDump", "c_uint, c_void_p, c_uint", "None"),
    ("SteamAPI_SetMiniDumpComment", "c_char_p", "None"),
    ("SteamAPI_ManualDispatch_Init", "", "None"),
    ("SteamAPI_ManualDispatch_RunFrame", "c_int", "None"),
    ("SteamAPI_ManualDispatch_GetNextCallback", "c_int, POINTER(CallbackMsg_t)", "c_bool"),
    ("SteamAPI_ManualDispatch_FreeLastCallback", "c_int", "None"),
    ("SteamAPI_ManualDispatch_GetAPICallResult", "c_int, c_ulonglong, c_void_p, c_int, c_int, c_bool", "c_bool"),
    ("SteamAPI_GetHSteamPipe", "", "c_int"),
    ("SteamAPI_GetHSteamUser", "", "c_uint"),
    ("SteamAPI_RunCallbacks", "", "None"),
]


def steamapi(structs, interfaces):

    p("""\
def load(dll):
""")

    for s in structs:
        for m in s.get("methods", []):
            name = m["methodname"]
            flat = m["methodname_flat"]
            flatmethod(m, name, flat, s["struct"])

    for i in interfaces:
        for m in i.get("methods", []):
            name = m["methodname"]
            flat = m["methodname_flat"]
            flatmethod(m, name, flat,  i["classname"])

        for a in i.get("accessors", []):
            name = a["name"]
            flat = a["name_flat"]
            flataccessor(a, name, flat, i["classname"])

    for name, argtypes, restype in FIXED_METHODS:
        fixedmethod(name, argtypes, restype)

    # Stubs.

    for s in structs:
        for m in s.get("methods", []):
            name = m["methodname"]
            flat = m["methodname_flat"]
            stubmethod(m, name, flat)

    for i in interfaces:
        for m in i.get("methods", []):
            name = m["methodname"]
            flat = m["methodname_flat"]
            stubmethod(m, name, flat)

        for a in i.get("accessors", []):
            name = a["name"]
            flat = a["name_flat"]
            stubaccessor(a, name, flat, i["classname"])

    for name, argtypes, restype in FIXED_METHODS:
        stubfixedmethod(name, argtypes, restype)



HEADER = """\
from ctypes import (
    c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_long, c_ulong,
    c_longlong, c_ulonglong, c_char_p, c_void_p, c_bool, c_float, byref,
    c_double, c_size_t, Structure, POINTER, byref, cast, sizeof)

try:
    from typing import Any
except ImportError:
    pass

def not_ready(*args): # type: (...) -> Any
    raise RuntimeError("Please call steamapi.load() before this function.")

import platform
if platform.win32_ver()[0]:
    PACK = 8
else:
    PACK = 4

"""

FOOTER = '''\
class CallbackMsg_t(Structure):
    _fields_ = [
        ( "m_hSteamUser", c_int),
        ( "m_iCallback", c_int),
        ( "m_pubParam", c_void_p),
        ( "m_cubParam", c_int),
        ]

    _pack_ = PACK

hSteamPipe = None

def init_callbacks():
    """
    This initializes Steam callback handling. It should be called after
    Init but before any other call.
    """

    global hSteamPipe
    ManualDispatch_Init()
    hSteamPipe = GetHSteamPipe()

def generate_callbacks():
    """
    This generates the callback objects produced by Steam. This needs to be
    iterated over once per frame to make sure the callbacks are
    processed and the screen is updated.

    The callbacks are generated of the

    """

    if hSteamPipe is None:
        raise RuntimeError("Please call steamapi.init_callbacks() before this function.")

    ManualDispatch_RunFrame(hSteamPipe)

    message = CallbackMsg_t()

    while ManualDispatch_GetNextCallback(hSteamPipe, byref(message)):

        callback_type = callback_by_id.get(message.m_iCallback, None)

        if callback_type is not None:
            cb = cast(message.m_pubParam, POINTER(callback_type)).contents
            yield cb

        ManualDispatch_FreeLastCallback(hSteamPipe)

class APIFailure(Exception):
    pass

def get_api_call_result(call, callback_type):
    """
    Returns the result of an API call.

    `call`
        The SteamAPICall_t returned by the call.

    `callback_type`
        Either the type or an integer representing the type of the API call.

    This returns an object of callback_type if the call completed, None if
    the call hasn't finished, and raises APIFailure if the call failed. (It's
    recommended that APIFailures are caught and the API call retried.)

    One way to use this is with the SteamAPICallCompleted_t callback::

        for i in steamapi.generate_callbacks():
            if isinstance(i, steamapi.SteamAPICallCompleted_t):
                result = steamapi.get_api_call_result(i.m_hAsyncCall, i.m_iCallback)
                print("The result of", i.m_hAsyncCall, "is", result)
            else:
                # Handle other callbacks.
    """

    failure = c_bool()

    if not SteamUtils().IsAPICallCompleted(call, byref(failure)):
        return None

    if failure:
        raise APIFailure(call)

    if isinstance(callback_type, int):
        callback_type = callback_by_id[callback_type]

    result = callback_type()

    if not SteamUtils().GetAPICallResult(call, byref(result), sizeof(result), callback_type.callback_id, byref(failure)):
        raise APIFailure(call)

    if failure:
        raise APIFailure(call)

    return result
'''


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("api_json", default="sdk/public/steam/steam_api.json", nargs='?')
    ap.add_argument("output", default="steamapi.py", nargs='?')
    args = ap.parse_args()

    with open(args.api_json, "r") as f:
        api = json.load(f)

    global out
    out = open(args.output, "w")

    p(HEADER)
    p("")

    typedef(api["typedefs"])

    consts(api["consts"])
    enums(api["enums"])

    for i in api["callback_structs"]:
        if "enums" in i:
            enums(i["enums"])

    structs(api["structs"])
    structs(api["callback_structs"])

    callback_by_id(api["callback_structs"])

    structs(api["interfaces"])
    steamapi(api["structs"], api["interfaces"])

    p(FOOTER)

    out.close()


if __name__ == "__main__":
    main()
