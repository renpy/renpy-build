#!/usr/bin/env python

import traceback
import os
import zipfile
import tarfile
import shutil
import subprocess
import stat

from . import plat
from .properties import set_property, get_property, local_properties, bundle_properties
from .configure import Configuration

__ = plat.__


def run(interface, *args, **kwargs):
    """
    Runs the supplied arguments.
    """

    try:
        interface.call(args, **kwargs)
        return True
    except (subprocess.CalledProcessError, OSError):
        return False


dname = None


def default_keystore_path(base):
    """
    Returns the default keystore path for the given project.
    """

    return os.path.join(base, "android.keystore")

def bundle_keystore_path(base):
    """
    Returns the bundle keystore path for the given project.
    """

    return os.path.join(base, "bundle.keystore")

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

        backups = __main__.path_to_saves(renpy.config.gamedir, "backups") # type: ignore

        keys = os.path.join(backups, "keys")
        keyfile = os.path.join(keys, os.path.basename(source) + "-" + str(int(time.time())))

        if not os.path.isdir(keys):
            os.mkdir(keys, 0o700)

        shutil.copy(source, keyfile)

    except:
        pass


def generate_android_keys(interface, base):
    """
    Generates the android.keystore file, if it doesn't exist.
    """


    keystore = default_keystore_path(base)
    old_keystore = plat.path("android.keystore").replace("\\", "/")

    if os.path.exists(keystore):
        return

    if os.path.exists(old_keystore):
        if interface.yesno(__("I found an android.keystore file in the rapt directory. Do you want to use this file?")):
            shutil.copy(old_keystore, keystore)
            return

    if not interface.yesno(__("I can create an application signing key for you. This key is required to create Universal APK for sideloading and stores other than Google Play.\n\nDo you want to create a key?")):
        return

    get_dname(interface)

    if not interface.yesno(__("I will create the key in the android.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\nYou also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of android.keystore, and keep it in a safe place?") +
                           __("\n\nSaying 'No' will prevent key creation.")):
        return

    if not run(interface, plat.keytool, "-genkey", "-keystore", keystore, "-alias", "android", "-keyalg", "RSA", "-keysize", "2048", "-keypass", "android", "-storepass", "android", "-dname", dname, "-validity", "20000", use_path=True):
        interface.fail(__("Could not create android.keystore. Is keytool in your path?"))

    interface.success(__("I've finished creating android.keystore. Please back it up, and keep it in a safe place."))

    backup_keys(keystore)

    return True


def generate_bundle_keys(interface, base):
    """
    Generates the bundle.keystore file, if it doesn't exist.
    """


    keystore = bundle_keystore_path(base)
    old_keystore = plat.path("bundle.keystore").replace("\\", "/")

    if os.path.exists(keystore):
        return

    if os.path.exists(old_keystore):
        if interface.yesno(__("I found a bundle.keystore file in the rapt directory. Do you want to use this file?")):
            shutil.copy(old_keystore, keystore)
            return

    if not interface.yesno(__("I can create a bundle signing key for you. This key is required to build an Android App Bundle (AAB) for upload to Google Play.\n\nDo you want to create a key?")):
        return

    get_dname(interface)

    if not interface.yesno(__("I will create the key in the bundle.keystore file.\n\nYou need to back this file up. If you lose it, you will not be able to upgrade your application.\n\nYou also need to keep the key safe. If evil people get this file, they could make fake versions of your application, and potentially steal your users' data.\n\nWill you make a backup of bundle.keystore, and keep it in a safe place?") +
                           __("\n\nSaying 'No' will prevent key creation.")):
        return

    if not run(interface, plat.keytool, "-genkey", "-keystore", keystore, "-alias", "android", "-keyalg", "RSA", "-keysize", "2048", "-keypass", "android", "-storepass", "android", "-dname", dname, "-validity", "20000", use_path=True):
        interface.fail(__("Could not create bundle.keystore. Is keytool in your path?"))

    backup_keys(keystore)

    return True


def keys_exist(base):
    """
    Returns true if the keys exist.
    """

    config = Configuration(base)

    if not config.update_keystores:
        return True

    if not os.path.exists(default_keystore_path(base)):
        return False

    if not os.path.exists(bundle_keystore_path(base)):
        return False

    return True


def generate_keys(interface, base):
    """
    Called to generate android.keystore and bundle.keystore.
    """

    # Create the project directory.
    import rapt.build
    rapt.build.copy_project(False)

    generated = False

    if generate_android_keys(interface, base):
        generated = True

    if generate_bundle_keys(interface, base):
        generated = True

    if generated:
        interface.open_directory(base, __("I've opened the directory containing android.keystore and bundle.keystore. Please back them up, and keep them in a safe place."))


def update_project_keys(base):
    """
    Updates the project's keys to point to the generated keys. Called from
    build.py.
    """

    # Update local.properties.

    properties = local_properties

    set_property(properties, "key.alias", "android", replace=True)
    set_property(properties, "key.store.password", "android", replace=True)
    set_property(properties, "key.alias.password", "android", replace=True)

    default_keystore = default_keystore_path(base)
    set_property(properties, "key.store", default_keystore.replace("\\", "/"), replace=True)

    # Update the bundle properties.

    properties = bundle_properties

    set_property(properties, "key.alias", "android", replace=True)
    set_property(properties, "key.store.password", "android", replace=True)
    set_property(properties, "key.alias.password", "android", replace=True)

    bundle_keystore = bundle_keystore_path(base)
    set_property(properties, "key.store", bundle_keystore.replace("\\", "/"), replace=True)


def get_local_key_properties():
    return [
        "--ks", get_property(local_properties, "key.store"),
        "--ks-pass", "pass:" + get_property(local_properties, "key.store.password"),
        "--ks-key-alias", get_property(local_properties, "key.alias"),
        "--key-pass", "pass:" + get_property(local_properties, "key.alias.password"),
    ]
