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


def maybe_java_home(s):
    """
    If JAVA_HOME is in the environ, return $JAVA_HOME/bin/s. Otherwise, return
    s.
    """

    if "JAVA_HOME" in os.environ:
        if not os.path.exists(os.path.join(os.environ["JAVA_HOME"], "bin", "javac.exe")):
            return s

        return os.path.join(os.environ["JAVA_HOME"], "bin", s)
    else:
        return s


if platform.win32_ver()[0]:
    windows = True

    adb = "platform-tools\\adb.exe"
    sdkmanager = "cmdline-tools\\latest\\bin\\sdkmanager.bat"

    java = maybe_java_home("java.exe")
    javac = maybe_java_home("javac.exe")
    keytool = maybe_java_home("keytool.exe")

    gradlew = "project/gradlew.bat"

elif platform.mac_ver()[0]:
    macintosh = True

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

jdk_requirement = 17
sdk_version = "9477386_latest"

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
