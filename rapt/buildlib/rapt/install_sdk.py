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
        raise
        return False
    return True


##############################################################################
def check_java(interface):
    """
    Checks for the presence of a minimally useful java on the user's system.
    """

    interface.info(__("I'm compiling a short test program, to see if you have a working JDK on your system."))

    if not run_slow(interface, plat.javac, plat.path("buildlib/CheckJDK8.java"), use_path=True):
        interface.fail(__("I was unable to use javac to compile a test file. If you haven't installed the Java Development Kit yet, please download it from:\n\n{a=https://adoptium.net/?variant=openjdk8}https://adoptium.net/?variant=openjdk8{/a}\n\nThe JDK is different from the JRE, so it's possible you have Java without having the JDK. Please make sure you installed the 'JavaSoft (Oracle) registry keys'.\n\nWithout a working JDK, I can't continue."))

    if not run_slow(interface, plat.java, "-classpath", plat.path("buildlib"), "CheckJDK8", use_path=True):
        interface.fail(__("The version of Java on your computer does not appear to be JDK 8, which is the only version supported by the Android SDK. If you need to install JDK 8, you can download it from:\n\n{a=https://adoptium.net/?variant=openjdk8}https://adoptium.net/?variant=openjdk8{/a}\n\nYou can also set the JAVA_HOME environment variable to use a different version of Java."))

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
        ("platforms;android-30", "platforms/android-30"),
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


local_properties = plat.path("project/local.properties")
bundle_properties = plat.path("project/bundle.properties")


def set_property(properties, key, value, replace=False):
    """
    Sets the property `key` in local/bundle.properties to `value`. If replace is True,
    replaces the value.
    """

    lines = [ ]

    try:
        with open(properties, "r") as f:
            for l in f:
                k = l.partition("=")[0].strip()

                if k == key:
                    if not replace:
                        return
                    else:
                        continue

                lines.append(l)

    except:
        pass

    with open(properties, "w") as f:
        for l in lines:
            f.write(l)

        f.write("{}={}\n".format(key, value))


def get_property(properties, key, default=None):

    with open(properties, "r") as f:
        for l in f:
            k, _, v = l.partition("=")

            if k.strip() == key:
                return v.strip()

    return default


def get_local_key_properties():
    return [
        "--ks", get_property(local_properties, "key.store"),
        "--ks-pass", "pass:" + get_property(local_properties, "key.store.password"),
        "--ks-key-alias", get_property(local_properties, "key.alias"),
        "--key-pass", "pass:" + get_property(local_properties, "key.alias.password"),
    ]


dname = None


def get_dname(interface):
    global dname

    if dname is None:
        dname = "CN=" + interface.input(__("Please enter your name or the name of your organization."), "A Ren'Py Creator")


def backup_keys(source):

    try:

        import __main__
        import time
        import renpy
        import shutil

        backups = __main__.path_to_saves(renpy.config.gamedir, "backups")

        keys = os.path.join(backups, "keys")
        keyfile = os.path.join(keys, os.path.basename(source) + "-" + str(int(time.time())))

        if not os.path.isdir(keys):
            os.mkdir(keys, 0o700)

        shutil.copy(source, keyfile)

    except:
        pass


def generate_keys(interface):

    properties = local_properties

    set_property(properties, "key.alias", "android")
    set_property(properties, "key.store.password", "android")
    set_property(properties, "key.alias.password", "android")

    default_keystore = plat.path("android.keystore").replace("\\", "/")

    if get_property(properties, "key.store", default_keystore) != default_keystore:
        return

    if os.path.exists(plat.path("android.keystore")):
        set_property(properties, "key.store", default_keystore)
        return

    if not interface.yesno(__("I can create an application signing key for you. This key is required to create Universal APK for sideloading and stores other than Google Play.\n\nDo you want to create a key?")):
        return

    get_dname(interface)

    if not interface.yesno(__("I will create the key in the android.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\nYou also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of android.keystore, and keep it in a safe place?")):
        return

    if not run(interface, plat.keytool, "-genkey", "-keystore", "android.keystore", "-alias", "android", "-keyalg", "RSA", "-keysize", "2048", "-keypass", "android", "-storepass", "android", "-dname", dname, "-validity", "20000", use_path=True):
        interface.fail(__("Could not create android.keystore. Is keytool in your path?"))

    interface.success(__("I've finished creating android.keystore. Please back it up, and keep it in a safe place."))

    backup_keys(default_keystore)
    set_property(properties, "key.store", default_keystore)

    return True


def generate_bundle_keys(interface):

    properties = bundle_properties

    set_property(properties, "key.alias", "android")
    set_property(properties, "key.store.password", "android")
    set_property(properties, "key.alias.password", "android")

    default_keystore = plat.path("bundle.keystore").replace("\\", "/")

    if get_property(properties, "key.store", default_keystore) != default_keystore:
        return

    if os.path.exists(plat.path("bundle.keystore")):
        set_property(properties, "key.store", default_keystore)
        return

    if not interface.yesno(__("I can create a bundle signing key for you. This key is required to build an Android App Bundle (AAB) for upload to Google Play.\n\nDo you want to create a key?")):
        return

    get_dname(interface)

    if not interface.yesno(__("I will create the key in the bundle.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\nYou also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of bundle.keystore, and keep it in a safe place?")):
        return

    if not run(interface, plat.keytool, "-genkey", "-keystore", "bundle.keystore", "-alias", "android", "-keyalg", "RSA", "-keysize", "2048", "-keypass", "android", "-storepass", "android", "-dname", dname, "-validity", "20000", use_path=True):
        interface.fail(__("Could not create bundle.keystore. Is keytool in your path?"))

    backup_keys(default_keystore)
    set_property(properties, "key.store", default_keystore)

    return True


def install_sdk(interface):

    # Create the project directory.
    import rapt.build
    rapt.build.copy_project(False)

    check_java(interface)

    unpack_sdk(interface)

    get_packages(interface)

    generated = False

    if generate_keys(interface):
        generated = True

    if generate_bundle_keys(interface):
        generated = True

    set_property(local_properties, "sdk.dir", plat.sdk.replace("\\", "/"), replace=True)
    set_property(bundle_properties, "sdk.dir", plat.sdk.replace("\\", "/"), replace=True)

    if generated:
        interface.open_directory(plat.path("."), __("I've opened the directory containing android.keystore and bundle.keystore. Please back them up, and keep them in a safe place."))

    interface.final_success(__("It looks like you're ready to start packaging games."))
