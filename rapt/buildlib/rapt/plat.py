# This sets up various variables and commands based on the platform we're on.

from __future__ import print_function

##############################################################################
# These are set based on the platform we're on.
windows = False
macintosh = False
linux = False

import sys
import os
import platform
import traceback
import shutil
import subprocess


def translate(s):
    """
    This is intended to be replaced when this module is imported from Ren'Py
    proper, to translate `s` itself.
    """

    return s


def __(s):
    """
    This is imported into the other modules. It's called to translate `s`,
    which is
    """

    return translate(s)


def set_win32_java_home():
    """
    When run on Win32, this is used to set the JAVA_HOME environment variable.
    """

    if "JAVA_HOME" in os.environ:
        return

    def scanreg(key, bitflag):

        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        p = subprocess.Popen([ "reg", "query", key, "/s", bitflag], startupinfo=startupinfo, stdout=subprocess.PIPE)
        output = p.stdout.read()

        rv = { }

        prefix = ""

        for l in output.split(b"\r\n"):
            if not l:
                continue

            if not l.startswith(b"    "):
                prefix = l
                continue

            a = l.split(b"    ")

            key = prefix + b"\\" + a[1]
            rv[key.decode("utf-8")] = a[3]

        return rv

    SCANS = [
        ("HKEY_LOCAL_MACHINE\\SOFTWARE\\JavaSoft\\Java Development Kit", "/reg:64"),
        ("HKEY_LOCAL_MACHINE\\SOFTWARE\\JavaSoft\\JDK", "/reg:64"),
    ]

    for key, bitflag in SCANS:
        keys = scanreg(key, bitflag)

        jh = key + "\\1.8\\JavaHome"

        if jh in keys:
            if sys.version_info[0] == 2:
                os.environ["JAVA_HOME"] = keys[jh]
            else:
                os.environ["JAVA_HOME"] = keys[jh].decode("mbcs")
            return


def set_mac_java_home():
    """
    When run on macOS, this is used to set the JAVA_HOME environment variable.
    """

    if "JAVA_HOME" in os.environ:
        return

    try:
        import plistlib

        raw_plist = subprocess.check_output("/usr/libexec/java_home -X -v 1.8", shell=True)
        plist = plistlib.readPlistFromString(raw_plist)

        java_home = None

        for d in plist:
            if not d.get("JVMEnabled", True):
                continue

            java_home = d["JVMHomePath"]

            if os.path.exists(os.path.join(java_home, "bin", "javac")):
                break
        else:
            return

        os.environ["JAVA_HOME"] = java_home
    except:
        return


def maybe_java_home(s):
    """
    If JAVA_HOME is in the environ, return $JAVA_HOME/bin/s. Otherwise, return
    s.
    """

    if "JAVA_HOME" in os.environ:
        return os.path.join(os.environ["JAVA_HOME"], "bin", s)
    else:
        return s


if platform.win32_ver()[0]:
    windows = True

    try:
        set_win32_java_home()
    except:
        traceback.print_exc()

    adb = "platform-tools\\adb.exe"
    sdkmanager = "cmdline-tools\\latest\\bin\\sdkmanager.bat"

    java = maybe_java_home("java.exe")
    javac = maybe_java_home("javac.exe")
    keytool = maybe_java_home("keytool.exe")

    gradlew = "project/gradlew.bat"

elif platform.mac_ver()[0]:
    macintosh = True

    try:
        set_mac_java_home()
    except:
        traceback.print_exc()

    adb = "platform-tools/adb"
    sdkmanager = "cmdline-tools/latest/bin/sdkmanager"

    java = maybe_java_home("java")
    javac = maybe_java_home("javac")
    keytool = maybe_java_home("keytool")

    gradlew = "project/gradlew"

else:
    linux = True

    adb = "platform-tools/adb"
    sdkmanager = "cmdline-tools/latest/bin/sdkmanager"

    java = maybe_java_home("java")
    javac = maybe_java_home("javac")
    keytool = maybe_java_home("keytool")

    gradlew = "project/gradlew"

# The path to RAPT.

if sys.version_info.major >= 3:
    RAPT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
else:
    RAPT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__.decode(sys.getfilesystemencoding())))))


def path(path, relative=False):
    """
    Turns a relative path into an absolute path relative to the RAPT
    directory.
    """

    if not path:
        return RAPT_PATH

    if not relative:
        path = os.path.join(RAPT_PATH, path)

    return path


sdk_version = "7583922_latest"

try:
    with open(path("sdk.txt")) as f:
        sdk = f.read().strip()
except:
    sdk = path("Sdk")

adb = os.path.join(sdk, adb)
sdkmanager = os.path.join(sdk, sdkmanager)

gradlew = path(gradlew)

# This gets set in the Ren'Py launcher if we're a Ren'Py build.
renpy = False


def rename(src, dst):
    """
    Renames src to dst.
    """

    if os.path.isdir(dst):
        shutil.rmtree(dst)
    elif os.path.exists(dst):
        os.unlink(dst)

    if os.path.isdir(src):
        shutil.copytree(src, dst)
        shutil.rmtree(src)
    else:
        shutil.copy(src, dst)
        os.unlink(src)
