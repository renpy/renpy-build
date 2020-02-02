#!/usr/bin/env python2.7

import pygame_sdl2
import sys

import re
import tarfile
import os
import shutil
import time
import zipfile
import subprocess
import hashlib

from . import plat
from . import iconmaker

import rapt.plat as plat
import rapt.iconmaker as iconmaker

__ = plat.__

sys.path.append(os.path.join(plat.RAPT_PATH, "buildlib", "jinja2.egg"))

import jinja2
import rapt.configure as configure

# If we have python 2.7, record the path to it.
if sys.version_info.major == 2 and sys.version_info.minor == 7:
    PYTHON = sys.executable
else:
    PYTHON = None


class PatternList(object):
    """
    Used to load in the blacklist and whitelist patterns.
    """

    def __init__(self, *args):
        self.patterns = [ ]

        for i in args:
            self.load(plat.path(i))

    def match(self, s):
        """
        Matches the patterns against s. Returns true if they match, False
        otherwise.
        """

        slash_s = "/" + s

        for p in self.patterns:
            if p.match(s):
                return True
            if p.match(slash_s):
                return True

        return False

    def load(self, fn):

        with open(fn, "r") as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue

                if l.startswith("#"):
                    continue

                self.patterns.append(self.compile(l))

    def compile(self, pattern):
        """
        Compiles a pattern into a regex object.
        """

        regexp = ""

        while pattern:
            if pattern.startswith("**"):
                regexp += r'.*'
                pattern = pattern[2:]
            elif pattern[0] == "*":
                regexp += r'[^/]*'
                pattern = pattern[1:]
            elif pattern[0] == '[':
                regexp += r'['
                pattern = pattern[1:]

                while pattern and pattern[0] != ']':
                    regexp += pattern[0]
                    pattern = pattern[1:]

                pattern = pattern[1:]
                regexp += ']'

            else:
                regexp += re.escape(pattern[0])
                pattern = pattern[1:]

        regexp += "$"

        return re.compile(regexp, re.I)


# Used by render.
environment = jinja2.Environment(loader=jinja2.FileSystemLoader(plat.path('')))


def render(always, template, dest, **kwargs):
    """
    Using jinja2, render `template` to the filename `dest`, supplying the keyword
    arguments as template parameters.
    """

    dest = plat.path(dest)

    if (not always) and os.path.exists(dest):
        return

    template = environment.get_template(template)
    text = template.render(**kwargs)

    f = file(dest, "wb")
    f.write(text.encode("utf-8"))
    f.close()


def compile_dir(iface, dfn):
    """
    Compile *.py in directory `dfn` to *.pyo
    """

    # -OO = strip docstrings
    iface.call([PYTHON, '-O', '-m', 'compileall', '-f', dfn])


def make_tar(iface, fn, source_dirs):
    """
    Make a zip file `fn` from the contents of source_dis.
    """

    source_dirs = [ plat.path(i) for i in source_dirs ]

    def include(fn):
        rv = True

        if blacklist.match(fn):
            rv = False

        if whitelist.match(fn):
            rv = True

        return rv

    # zf = zipfile.ZipFile(fn, "w")
    tf = tarfile.open(fn, "w:gz", format=tarfile.USTAR_FORMAT)

    added = set()

    def add(fn, relfn):

        adds = [ ]

        while relfn:
            adds.append((fn, relfn))
            fn = os.path.dirname(fn)
            relfn = os.path.dirname(relfn)

        adds.reverse()

        for fn, relfn in adds:

            if relfn not in added:
                added.add(relfn)
                tf.add(fn, relfn, recursive=False)

    for sd in source_dirs:

        if PYTHON and not RENPY:
            compile_dir(iface, sd)

        sd = os.path.abspath(sd)

        for dir, dirs, files in os.walk(sd): # @ReservedAssignment

            for _fn in dirs:
                fn = os.path.join(dir, _fn)
                relfn = os.path.relpath(fn, sd)

                if include(relfn):
                    add(fn, relfn)

            for fn in files:
                fn = os.path.join(dir, fn)
                relfn = os.path.relpath(fn, sd)

                if include(relfn):
                    add(fn, relfn)

    tf.close()


def make_tree(src, dest):

    src = plat.path(src)
    dest = plat.path(dest)

    def ignore(dir, files):

        rv = [ ]

        for basename in files:
            fn = os.path.join(dir, basename)
            relfn = os.path.relpath(fn, src)

            ignore = False

            if blacklist.match(relfn):
                ignore = True
            if whitelist.match(relfn):
                ignore = False

            if ignore:
                rv.append(basename)

        return rv

    shutil.copytree(src, dest, ignore=ignore)


def join_and_check(base, sub):
    """
    If base/sub is a directory, returns the joined path. Otherwise, return None.
    """

    rv = os.path.join(base, sub)
    if os.path.exists(rv):
        return rv

    return None


def edit_file(fn, pattern, line):
    """
    Replaces lines in `fn` that begin with `pattern` with `line`. `line`
    should not end with a newline - we add it.
    """

    fn = plat.path(fn)

    lines = [ ]

    with open(fn, "r") as f:
        for l in f:

            if re.match(pattern, l):
                l = line + "\n"

            lines.append(l)

    with open(fn, "w") as f:
        f.write(''.join(lines))


def zip_directory(zf, prefix, dn):
    """
    Zips up the directory `dn`. `zf` is the file to place the
    contents of the directory into.
    """

    for dirname, dirs, files in os.walk(dn):
        for fn in files:
            fn = os.path.join(dirname, fn)
            archive_fn = os.path.join(prefix, os.path.relpath(fn, dn))
            zf.write(fn, archive_fn)


def copy_presplash(directory, name, default):
    """
    Copies the presplash file.
    """

    for ext in [ ".png", ".jpg" ]:

        fn = os.path.join(directory, name + ext)

        if os.path.exists(fn):
            break
    else:
        fn = default
        ext = os.path.splitext(fn)[1]

    shutil.copy(fn, plat.path("project/app/src/main/assets/" + name + ext))


def split_renpy(directory):
    """
    Takes a built Ren'Py game, and splits it into the private and assets
    directories. This also renames <game>.py to main.py, and moves common/
    into assets.
    """

    private = os.path.join(directory, "private")
    assets = os.path.join(directory, "assets")

    filenames = os.listdir(directory)

    os.mkdir(private)
    os.mkdir(assets)
    os.mkdir(os.path.join(assets, "renpy"))

    plat.rename(os.path.join(directory, "renpy", "common"), os.path.join(assets, "renpy", "common"))

    for fn in filenames:
        full_fn = os.path.join(directory, fn)

        if fn.startswith("android-"):
            continue

        if fn.endswith(".py"):
            plat.rename(full_fn, os.path.join(private, "main.py"))
            continue

        if fn == "renpy":
            plat.rename(full_fn, os.path.join(private, fn))
            continue

        plat.rename(full_fn, os.path.join(assets, fn))

    return private, assets


GENERATED = [
    (False, "templates/app-build.gradle", "project/app/build.gradle"),
    (False, "templates/app-AndroidManifest.xml", "project/app/src/main/AndroidManifest.xml"),
    (False, "templates/app-strings.xml", "project/app/src/main/res/values/strings.xml"),
    (False, "templates/renpyandroid-AndroidManifest.xml", "project/renpyandroid/src/main/AndroidManifest.xml"),
    (False, "templates/renpyandroid-strings.xml", "project/renpyandroid/src/main/res/values/strings.xml"),
    (False, "templates/Constants.java", "project/renpyandroid/src/main/java/org/renpy/android/Constants.java"),
]

COPIED = [
    "renpyandroid/src/main/jniLibs",
    "renpyandroid/src/main/private",
]


def copy_project(update_always=False):
    """
    This updates the project, if necessary.
    """

    def snarf(fn):
        fn = plat.path(fn)

        if os.path.exists(fn):
            return open(fn, "r").read().strip()
        else:
            return None

    project = plat.path("project")
    prototype = plat.path("prototype")

    update = False

    if not os.path.exists(project):
        update = True
    elif update_always:
        if snarf("project/build.txt") != snarf("prototype/build.txt"):
            update = True

    if not update:
        return

    lp = snarf("project/local.properties")

    if os.path.exists(project):
        shutil.rmtree(project)

    shutil.copytree(prototype, project)

    if lp is not None:
        with open(plat.path("project/local.properties"), "w") as f:
            f.write(lp + "\n")


def copy_libs():
    """
    This copies updated libraries from the prototype to the project each
    time a build occurs.
    """

    for i in COPIED:
        project = plat.path("project/" + i)
        prototype = plat.path("prototype/" + i)

        if os.path.exists(project):
            shutil.rmtree(project)

        shutil.copytree(prototype, project)


def build(iface, directory, commands, launch=False, finished=None):

    # Are we doing a Ren'Py build?

    global RENPY

    if not os.path.isdir(directory):
        iface.fail(__("{} is not a directory.").format(directory))

    if os.path.isdir(os.path.join(directory, "renpy")):
        RENPY = True
    else:
        RENPY = False

    if RENPY and not os.path.isdir(os.path.join(directory, "game")):
        iface.fail(__("{} does not contain a Ren'Py game.").format(directory))

    config = configure.Configuration(directory)
    if config.package is None:
        iface.fail(__("Run configure before attempting to build the app."))

    if (config.store == "play" or config.store == "all") and ((config.google_play_key is None) or (len(config.google_play_key) < 32)):
        iface.fail(__("Google Play support is enabled, but build.google_play_key is not defined."))

    global blacklist
    global whitelist

    blacklist = PatternList("blacklist.txt")
    whitelist = PatternList("whitelist.txt")

    if RENPY:
        default_presplash = plat.path("templates/renpy-presplash.jpg")

        private_dir, assets_dir = split_renpy(directory)

    else:
        default_presplash = plat.path("templates/pygame-presplash.jpg")

        if config.layout == "internal":
            private_dir = directory
            assets_dir = None
        elif config.layout == "split":
            private_dir = join_and_check(directory, "internal")
            assets_dir = join_and_check(directory, "assets")

    versioned_name = config.name
    versioned_name = re.sub(r'[^\w]', '', versioned_name)
    versioned_name += "-" + config.version

    # Annoying fixups.
    config.name = config.name.replace("'", "\\'")
    config.icon_name = config.icon_name.replace("'", "\\'")

    if config.store not in [ "play", "none" ]:
        config.expansion = False

    iface.info(__("Updating project."))

    copy_project(config.update_always)

    copy_libs()

    iface.info(__("Creating assets directory."))

    assets = plat.path("project/app/src/main/assets")

    if os.path.isdir(assets):
        shutil.rmtree(assets)

    def make_assets():

        if assets_dir is not None:
            make_tree(assets_dir, assets)
        else:
            os.mkdir(assets)

        # If we're Ren'Py, rename things.
        if RENPY:

            # Ren'Py uses a lot of names that don't work as assets. Auto-rename
            # them.
            for dirpath, dirnames, filenames in os.walk(assets, topdown=False):

                for fn in filenames + dirnames:
                    if fn[0] == ".":
                        continue

                    old = os.path.join(dirpath, fn)
                    new = os.path.join(dirpath, "x-" + fn)

                    plat.rename(old, new)

    iface.background(make_assets)

    if not os.path.exists(plat.path("bin")):
        os.mkdir(plat.path("bin"), 0o777)

    if config.expansion:
        iface.info(__("Creating expansion file."))
        expansion_file = "bin/main.{}.{}.obb".format(config.numeric_version, config.package)

        def make_expansion():

            zf = zipfile.ZipFile(plat.path(expansion_file), "w", zipfile.ZIP_STORED)
            zip_directory(zf, "assets", assets)
            zf.close()

            # Delete and re-make the assets directory.
            shutil.rmtree(assets)
            os.mkdir(assets)

        iface.background(make_expansion)

        # Write the file size into DownloaderActivity.
        file_size = os.path.getsize(plat.path(expansion_file))

    else:
        expansion_file = None
        file_size = 0

    iface.info(__("Packaging internal data."))

    private_dirs = [ 'project/renpyandroid/src/main/private' ]

    if private_dir is not None:
        private_dirs.append(private_dir)

    # Really, a tar file with the private data in it.
    private_mp3 = os.path.join(assets, "private.mp3")

    private_version = [ ]

    def pack():
        make_tar(iface, private_mp3, private_dirs)

        with open(private_mp3, "rb") as f:
            private_version.append(hashlib.md5(f.read()).hexdigest())

    iface.background(pack)
    private_version = private_version[0]

    # Write out constants.java.
    if not config.google_play_key:
        config.google_play_key = "NOT_SET"

    if not config.google_play_salt:
        config.google_play_salt = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20"

    for always, template, i in GENERATED:

        render(
            always or config.update_always,
            template,
            i,
            private_version=private_version,
            file_size=file_size,
            config=config,
            sdkpath=plat.path("Sdk"),
            )

    if config.update_icons:
        iconmaker.IconMaker(directory, config)

    # Copy the presplash files.
    copy_presplash(directory, "android-presplash", default_presplash)

    # Find and clean the apkdirs.

    apkdirs = [ ]

    if any(i.endswith("Debug") for i in commands):
        apkdirs.append(plat.path("project/app/build/outputs/apk/debug"))

    if any(i.endswith("Release") for i in commands):
        apkdirs.append(plat.path("project/app/build/outputs/apk/release"))

    for i in apkdirs:
        if os.path.exists(i):
            shutil.rmtree(i)

    # Build.
    iface.info(__("I'm using Gradle to build the package."))

    # This is a list of generated files that need to be copied over to the
    # dists folder.
    files = [ ]

    try:

        iface.call([ plat.gradlew, "--stacktrace", "-p", plat.path("project") ] + commands, cancel=True)

        if (expansion_file is not None) and any(i.startswith("install") for i in commands):
            iface.info(__("Uploading expansion file."))

            dest = "/storage/emulated/0/Android/obb/{}/{}".format(config.package, os.path.basename(expansion_file))

            iface.call([ plat.adb, "push", plat.path(expansion_file), dest ], cancel=True)

        if expansion_file is not None:
            files.append(plat.path(expansion_file))

    except subprocess.CalledProcessError:

        iface.fail(__("The build seems to have failed."))

    # Copy everything to bin.

    for i in apkdirs:
        for j in os.listdir(i):

            if not j.endswith(".apk"):
                continue

            sfn = os.path.join(i, j)

            dfn = "bin/{}-{}".format(
                config.package,
                j[4:])

            dfn = plat.path(dfn)

            shutil.copy(sfn, dfn)
            files.append(dfn)

    # Launch.

    if launch:
        iface.info(__("Launching app."))

        if expansion_file:
            launch_activity = "DownloaderActivity"
        else:
            launch_activity = "PythonSDLActivity"

        iface.call([
            plat.adb, "shell",
            "am", "start",
            "-W",
            "-a", "android.intent.action.MAIN",
            "{}/org.renpy.android.{}".format(config.package, launch_activity),
            ], cancel=True)

    if finished is not None:
        finished(files)

    iface.final_success(
        __("The build seems to have succeeded.") +
        "\n\n" +
        __("The arm64-v8a version works on newer Android devices, the armeabi-v7a version works on older devices, and the x86_64 version works on the simulator and chromebooks.") +
        "\n\n" +
        __("The universal version works everywhere but is larger.")
        )


def distclean(interface):
    """
    Cleans everything back to as it was when RAPT was first distributed.
    """

    if os.path.exists(plat.path("build_renpy.sh")):
        raise Exception("Can't clean android directory!")

    def rmdir(name):
        path = plat.path(name)

        if os.path.isdir(path):
            shutil.rmtree(path)

    def rm(name):
        path = plat.path(name)

        if os.path.exists(path):
            os.unlink(path)

    rm("buildlib/CheckJDK8.class")
    rmdir("project")
    rmdir("bin")

    try:
        rmdir("Sdk")
    except:
        rm("Sdk")
