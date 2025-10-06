#!/usr/bin/env python

import traceback
import os
import zipfile
import tarfile
import shutil
import subprocess
import stat

from . import plat

__ = plat.__

##############################################################################


def run(interface, *args, **kwargs):
    """
    Runs the supplied arguments.
    """

    try:
        interface.call(args, **kwargs)
        return True
    except (subprocess.CalledProcessError, OSError):
        return False


def run_slow(interface, *args, **kwargs):
    """
    Runs the supplied arguments in a manner that lets the program
    be cancelled.
    """

    try:
        interface.call(args, cancel=True, **kwargs)
    except (subprocess.CalledProcessError, OSError):
        return False
    return True


##############################################################################
def check_java(interface):
    """
    Checks for the presence of the correct Java version.
    """

    interface.info(__("I'm compiling a short test program, to see if you have a working JDK on your system."))

    if not run_slow(interface, plat.javac, plat.path("buildlib/CheckJDK.java"), use_path=True):
        interface.fail(__("I was unable to use javac to compile a test file. If you haven't installed the Java Development Kit yet, please download it from:\n\n{a=https://adoptium.net}https://adoptium.net/{/a}\n\nThe JDK is different from the JRE, so it's possible you have Java without having the JDK. Please install JDK [JDK_REQUIREMENT], and add it to your PATH.\n\nWithout a working JDK, I can't continue."))

    if not run_slow(interface, plat.java, "-classpath", plat.path("buildlib"), "CheckJDK", str(plat.jdk_requirement), use_path=True):
        interface.fail(__("The version of Java on your computer does not appear to be JDK [JDK_REQUIREMENT], which is required to build Android apps. If you need to install a newer JDK, you can download it from:\n\n{a=https://adoptium.net/}https://adoptium.net/{/a}, and add it to your PATH.\n\nYou can also set the JAVA_HOME environment variable to use a different version of Java."))

    interface.success(__("The JDK is present and working. Good!"))


class _FixedZipFile(zipfile.ZipFile):
    """
    A patched version of zipfile.ZipFile that adds support for:

    * Unix permissions bits.
    * Unix symbolic links.
    """

    def _extract_member(self, member, targetpath, pwd):

        if not isinstance(member, zipfile.ZipInfo):
            member = self.getinfo(member)

        # build the destination pathname, replacing
        # forward slashes to platform specific separators.
        arcname = member.filename.replace('/', os.path.sep)

        if os.path.altsep:
            arcname = arcname.replace(os.path.altsep, os.path.sep)
        # interpret absolute pathname as relative, remove drive letter or
        # UNC path, redundant separators, "." and ".." components.
        arcname = os.path.splitdrive(arcname)[1]
        invalid_path_parts = ('', os.path.curdir, os.path.pardir)
        arcname = os.path.sep.join(x for x in arcname.split(os.path.sep) if x not in invalid_path_parts)

        targetpath = os.path.join(targetpath, arcname)
        targetpath = os.path.normpath(targetpath)

        # Create all upper directories if necessary.
        upperdirs = os.path.dirname(targetpath)
        if upperdirs and not os.path.exists(upperdirs):
            os.makedirs(upperdirs)

        if member.filename[-1] == "/":
            if not os.path.isdir(targetpath):
                os.mkdir(targetpath)
            return targetpath

        attr = member.external_attr >> 16

        if stat.S_ISLNK(attr):

            with self.open(member, pwd=pwd) as source:
                linkto = source.read()

            os.symlink(linkto, targetpath)

        else:

            with self.open(member, pwd=pwd) as source, open(targetpath, "wb") as target:
                shutil.copyfileobj(source, target)

            if attr:
                os.chmod(targetpath, attr)

        return targetpath

def unpack_sdk(interface):

    if os.path.exists(plat.sdkmanager):
        interface.success(__("The Android SDK has already been unpacked."))
        return

    if "RAPT_NO_TERMS" not in os.environ:
        interface.terms("https://developer.android.com/studio/terms", __("Do you accept the Android SDK Terms and Conditions?"))

    if plat.windows:
        archive = "commandlinetools-win-{}.zip".format(plat.sdk_version)
    elif plat.macintosh:
        archive = "commandlinetools-mac-{}.zip".format(plat.sdk_version)
    elif plat.linux:
        archive = "commandlinetools-linux-{}.zip".format(plat.sdk_version)

    url = "https://dl.google.com/android/repository/" + archive

    interface.info(__("I'm downloading the Android SDK. This might take a while."))

    interface.download(url, plat.path(archive))

    interface.info(__("I'm extracting the Android SDK."))

    # We have to do this because Python has a small (260?) path length
    # limit on windows, and the Android SDK has very long filenames.
    old_cwd = os.getcwd()
    os.chdir(plat.path("."))


    zip = _FixedZipFile(archive)
    zip.extractall("Sdk")
    zip.close()

    # sdkmanager won't run unless we reorganize the unpack.
    os.rename("Sdk/cmdline-tools", "Sdk/latest")
    os.mkdir("Sdk/cmdline-tools")
    os.rename("Sdk/latest", "Sdk/cmdline-tools/latest")

    os.chdir(old_cwd)

    interface.success(__("I've finished unpacking the Android SDK."))


def get_packages(interface):

    packages = [ ]

    wanted_packages = [
        ("platform-tools", "platform-tools"),
        ("platforms;android-36", "platforms/android-36"),
        ]

    for i, j in wanted_packages:
        if not os.path.exists(os.path.join(plat.sdk, j)):
            packages.append(i)

    if packages:

        interface.info(__("I'm about to download and install the required Android packages. This might take a while."))

        if not run_slow(interface, plat.sdkmanager, "--update", yes=True):
            interface.fail(__("I was unable to accept the Android licenses."))

        if not run_slow(interface, plat.sdkmanager, "--licenses", yes=True):
            interface.fail(__("I was unable to accept the Android licenses."))

        if not run_slow(interface, plat.sdkmanager, yes=True, *packages):
            interface.fail(__("I was unable to install the required Android packages."))

    interface.success(__("I've finished installing the required Android packages."))




def install_sdk(interface):

    # Create the project directory.
    import rapt.build
    rapt.build.copy_project(False)

    check_java(interface)

    unpack_sdk(interface)

    get_packages(interface)

    interface.final_success(__("It looks like you're ready to start packaging games."))
