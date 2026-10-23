import concurrent.futures
import gzip
import hashlib
import os
import re
import shutil
import subprocess
import tarfile
import time

import jinja2

from . import configure, iconmaker, install_sdk, plat
from .keys import get_local_key_properties, update_project_keys
from .properties import bundle_properties, local_properties, set_property

__ = plat.__


class PatternList:
    """
    Used to load in the blocklist and keeplist patterns.
    """

    def __init__(self, *args):
        self.patterns = []

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
        with open(fn) as f:
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
                regexp += r".*"
                pattern = pattern[2:]
            elif pattern[0] == "*":
                regexp += r"[^/]*"
                pattern = pattern[1:]
            elif pattern[0] == "[":
                regexp += r"["
                pattern = pattern[1:]

                while pattern and pattern[0] != "]":
                    regexp += pattern[0]
                    pattern = pattern[1:]

                pattern = pattern[1:]
                regexp += "]"

            else:
                regexp += re.escape(pattern[0])
                pattern = pattern[1:]

        regexp += "$"

        return re.compile(regexp, re.I)


def should_autoescape(fn):
    """
    Returnes true if the filename `fn` should be autoescaped.
    """

    return fn.endswith(".xml")


# Used by render.
environment = jinja2.Environment(loader=jinja2.FileSystemLoader(plat.path("")), autoescape=should_autoescape)


def render(always, template, dest, **kwargs):
    """
    Using jinja2, render `template` to the filename `dest`, supplying the keyword
    arguments as template parameters.
    """

    dest = plat.path(dest)

    if (not always) and os.path.exists(dest):
        return

    if not os.path.isdir(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))

    template = environment.get_template(template)
    text = template.render(**kwargs)

    with open(dest, "wb") as f:
        f.write(text.encode("utf-8"))


def make_tar(iface, fn, source_dirs):
    """
    Make a zip file `fn` from the contents of source_dis.
    """

    source_dirs = [plat.path(i) for i in source_dirs]

    def include(fn):
        rv = True

        if blocklist.match(fn):
            rv = False

        if keeplist.match(fn):
            rv = True

        return rv

    tf = tarfile.open(fn, "w:gz", format=tarfile.GNU_FORMAT)

    added = set()

    def add(fn, relfn):
        adds = []

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
        sd = os.path.abspath(sd)

        for dir, dirs, files in os.walk(sd):
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


def copy_into(src, dest):
    """
    Copies all files from `src` into `dest`, creating
    directories that do not exist.
    """

    if not os.path.exists(src):
        return

    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.mkdir(dest, 0o777)

        for i in os.listdir(src):
            copy_into(
                os.path.join(src, i),
                os.path.join(dest, i),
            )

        return

    shutil.copy2(src, dest)


def make_assets_tree(src, dst):
    """
    Copies a subset of files from src to dst (governed by blocklist/keeplist)
    in a single concurrent pass. Additionally, because Ren'Py uses a lot of
    names that don't work as assets, every path segment is prefixed with 'x-'.
    """

    src = plat.path(src)
    dst = plat.path(dst)

    copy2 = shutil.copy2

    def copy(pair):
        old, new = pair

        if old[-3:] == ".gz":
            # AAPT unavoidably gunzips files with a .gz extension.
            # To prevent this we temporarily double gzip such files,
            # leaving AAPT to unpack them back into the original
            # location. /o\
            with open(old, "rb") as r, gzip.open(f'{new}.gz', "wb") as w:
                shutil.copyfileobj(r, w)

        else:
            copy2(old, new)

    def walk(old, new):
        drop = blocklist.match
        keep = keeplist.match

        mkdir = os.mkdir
        relpath = os.path.relpath
        sep = os.sep

        # join: Faster than os.path.join for our purposes.
        join = lambda a, b: f"{a}{sep}{b}"

        # Special case the top-level iteration where rel_path='.', then
        # replace with normal join function in subsequent iterations.
        # join1: ignore 1st arg
        join1 = lambda a, b: b

        cache = {old: new}

        mkdir(new)

        for old_stem, dirnames, filenames in os.walk(old):
            new_stem = cache[old_stem]
            rel_stem = relpath(old_stem, old)

            visit = []

            for name in dirnames:
                rel_path = join1(rel_stem, name)

                if drop(rel_path) and not keep(rel_path):
                    continue

                old_path = join(old_stem, name)
                new_path = join(new_stem, f"x-{name}")

                cache[old_path] = new_path
                visit.append(name)

                mkdir(new_path)

            dirnames[:] = visit

            for name in filenames:
                rel_path = join1(rel_stem, name)

                if drop(rel_path) and not keep(rel_path):
                    continue

                old_path = join(old_stem, name)
                new_path = join(new_stem, f"x-{name}")

                yield old_path, new_path

            join1 = join

    # Limiting factor is I/O not CPU, so use a fixed value for max workers.
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for _ in executor.map(copy, walk(src, dst)):
            pass


MAX_SIZE = 1000000000


def make_bundle_tree(src):
    src = plat.path(src)

    dst = []
    vol = {}

    rename = plat.rename

    # Initialise an assets directory for each bundle and add a test
    # file to make sure they exist and are writable.
    for i in range(1, 5):
        root = plat.path(f"project/ff{i}/src/main/assets")

        if os.path.isdir(root):
            shutil.rmtree(root)

        try:
            os.makedirs(root, 0o777)
        except Exception:
            pass

        with open(os.path.join(root, "00_pack.txt"), "w") as f:
            f.write("Shiro was here.\n")

        dst.append(root)
        vol[root] = 0

    def move(pair):
        old, new = pair

        rename(old, new)

    def walk(old, new):
        drop = blocklist.match
        keep = keeplist.match

        getsize = os.path.getsize
        makedirs = os.makedirs
        relpath = os.path.relpath
        sep = os.sep

        # join: Faster than os.path.join for our purposes.
        join = lambda a, b: f"{a}{sep}{b}"

        # Special case the top-level iteration where rel_path='.', then
        # replace with normal join function in subsequent iterations.
        # join1: ignore 1st arg
        # join2: ignore 2nd arg
        join1 = lambda a, b: b
        join2 = lambda a, b: a

        cache = set(new)
        cache_add = cache.add

        for old_stem, dirnames, filenames in os.walk(old):
            rel_stem = relpath(old_stem, old)

            visit = []

            for name in dirnames:
                rel_path = join1(rel_stem, name)

                if drop(rel_path) and not keep(rel_path):
                    continue

                visit.append(name)

            dirnames[:] = visit

            for name in filenames:
                rel_path = join1(rel_stem, name)

                if drop(rel_path) and not keep(rel_path):
                    continue

                old_path = join(old_stem, name)
                old_size = getsize(old_path)

                threshold = MAX_SIZE - old_size

                for new_root in new:
                    if vol[new_root] <= threshold:
                        break
                else:
                    raise Exception("Game too big for bundle, or single file > 1 GB.")

                vol[new_root] += old_size

                new_stem = join2(new_root, rel_stem)

                if new_stem not in cache:
                    makedirs(new_stem)
                    cache_add(new_stem)

                new_path = join(new_stem, name)

                yield old_path, new_path

            join1 = join2 = join

    # Limiting factor is I/O not CPU, so use a fixed value for max workers.
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for _ in executor.map(move, walk(src, dst)):
            pass


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

    lines = []

    with open(fn) as f:
        for l in f:
            if re.match(pattern, l):
                l = line + "\n"

            lines.append(l)

    with open(fn, "w") as f:
        f.write("".join(lines))


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

    for ext in [".png", ".jpg"]:
        fn = os.path.join(directory, name + ext)

        if os.path.exists(fn):
            break
    else:
        fn = default
        ext = os.path.splitext(fn)[1]

    shutil.copy(fn, plat.path("project/app/src/main/assets/" + name + ext))


def eliminate_pycache(directory):
    """
    Eliminates the __pycache__ directory, and moves the files in it up a level,
    renaming them to remove the cache tag.
    """

    import pathlib

    paths = list(pathlib.Path(directory).glob("**/__pycache__/*.pyc"))

    for p in paths:
        name = p.stem.partition(".")[0]

        target = p.parent.parent / (name + ".pyc")

        if target.exists():
            target.unlink()

        p.rename(target)

    paths = list(pathlib.Path(directory).glob("**/__pycache__"))

    for p in paths:
        p.rmdir()


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

        if fn == "lib":
            plat.rename(full_fn, os.path.join(private, fn))
            continue

        if fn == "public_key.pem":
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
    (False, "templates/settings.gradle", "project/settings.gradle"),
]

COPIED = [
    "renpyandroid/src/main/jniLibs",
]


def copy_project(update_always=False):
    """
    This updates the project, if necessary.
    """

    def snarf(fn):
        fn = plat.path(fn)

        if os.path.exists(fn):
            with open(fn) as f:
                return f.read().strip()
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
    bp = snarf("project/bundle.properties")

    if os.path.exists(project):
        shutil.rmtree(project)

    shutil.copytree(prototype, project)

    if lp is not None:
        with open(plat.path("project/local.properties"), "w") as f:
            f.write(lp + "\n")

    if bp is not None:
        with open(plat.path("project/bundle.properties"), "w") as f:
            f.write(bp + "\n")


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


def size_tree(dn):
    """
    Returns the size of the tree `dn`, in bytes.
    """

    rv = 0

    for dn, directories, filenames in os.walk(dn):
        for fn in filenames:
            fn = os.path.join(dn, fn)
            rv += os.path.getsize(fn)

    return rv


def build(
    iface, directory, base, install=False, bundle=False, launch=False, finished=None, permissions=[], version=None
):

    if not os.path.isdir(directory):
        iface.fail(__("{} is not a directory.").format(directory))

    if not os.path.isdir(os.path.join(directory, "renpy")):
        iface.fail(__("{} does not contain a Ren'Py game.").format(directory))

    if not os.path.isdir(os.path.join(directory, "game")):
        iface.fail(__("{} does not contain a Ren'Py game.").format(directory))

    install_sdk.check_java(iface)

    config = configure.Configuration(directory)

    if config.package is None:
        iface.fail(__("Run configure before attempting to build the app."))

    if version is not None:
        split_version = [i for i in version.split(".") if i.isdigit()]

        if not split_version:
            split_version = ["1", "0"]

        config.version = ".".join(split_version)

    global blocklist
    global keeplist

    blocklist = PatternList("blocklist.txt")
    keeplist = PatternList("keeplist.txt")

    default_presplash = plat.path("templates/renpy-presplash.jpg")
    default_downloading = plat.path("templates/renpy-downloading.jpg")

    eliminate_pycache(directory)

    private_dir, assets_dir = split_renpy(directory)

    # Pick the numeric version.

    if int(config.numeric_version) == 1:
        VERSION_CUTOFF_TIME = 1_800_000_000  # 'Fri Jan 15 03:00:00 2027'

        numeric_version = int(time.time())
        if numeric_version > VERSION_CUTOFF_TIME:
            numeric_version = (numeric_version - VERSION_CUTOFF_TIME) // 8 + VERSION_CUTOFF_TIME

        config.numeric_version = numeric_version

    # Annoying fixups.
    config.name = config.name.replace("'", "\\'")
    config.icon_name = config.icon_name.replace("'", "\\'")

    config.permissions.extend(permissions)

    iface.info(__("Updating project."))

    copy_project(config.update_always)

    copy_libs()

    if config.update_keystores:
        update_project_keys(base)

    iface.info(__("Creating assets directory."))

    assets = plat.path("project/app/src/main/assets")

    if os.path.isdir(assets):
        def on_rm_error(func, p, exc_info):
            try:
                os.chmod(p, 0o777)
                func(p)
            except Exception:
                pass
        for _ in range(3):
            try:
                shutil.rmtree(assets, onerror=on_rm_error)
                break
            except Exception:
                time.sleep(0.3)

    big_bundle = bundle and size_tree(assets_dir) > 50 * 1024 * 1024

    def make_assets():

        if big_bundle:
            os.mkdir(assets)
            make_bundle_tree(assets_dir)
        else:
            make_assets_tree(assets_dir, assets)

    iface.background(make_assets)

    # Copy assets out of the prototype, and into the project.
    copy_into(plat.path("prototype/app/src/main/assets"), assets)

    if not os.path.exists(plat.path("bin")):
        os.mkdir(plat.path("bin"), 0o777)

    iface.info(__("Packaging internal data."))

    private_dirs = ["project/renpyandroid/src/main/private"]

    if private_dir is not None:
        private_dirs.append(private_dir)

    # Really, a tar file with the private data in it.
    private_mp3 = os.path.join(assets, "private.mp3")

    make_tar(iface, private_mp3, private_dirs)

    with open(private_mp3, "rb") as f:
        private_version = hashlib.md5(f.read()).hexdigest()

    for always, template, i in GENERATED:
        render(
            always or config.update_always,
            template,
            i,
            private_version=private_version,
            config=config,
            bundle=bundle,
            big_bundle=big_bundle,
            sdkpath=plat.path("Sdk"),
        )

    if config.update_icons:
        iconmaker.IconMaker(directory, config)

    # Copy the presplash files.
    copy_presplash(directory, "android-presplash", default_presplash)
    copy_presplash(directory, "android-downloading", default_downloading)

    # Update the sdk path in the properties files.
    set_property(local_properties, "sdk.dir", plat.sdk.replace("\\", "/"), replace=True)
    set_property(bundle_properties, "sdk.dir", plat.sdk.replace("\\", "/"), replace=True)

    # Find and clean the apkdirs.

    apkdirs = []

    if not bundle:
        apkdirs.append(plat.path("project/app/build/outputs/apk/release"))
    else:
        apkdirs.append(plat.path("project/app/build/outputs/bundle/release"))

    for i in apkdirs:
        if os.path.exists(i):
            shutil.rmtree(i)

    # Build.
    iface.info(__("I'm using Gradle to build the package."))

    # This is a list of generated files that need to be copied over to the
    # dists folder.
    files = []

    if bundle:
        command = "bundleRelease"
    elif install:
        command = "installRelease"
    else:
        command = "assembleRelease"

    try:
        iface.call([plat.gradlew, "-p", plat.path("project"), command], cancel=True)

    except subprocess.CalledProcessError:
        iface.fail(__("The build seems to have failed."))

    # Copy everything to bin.

    for i in apkdirs:
        for j in os.listdir(i):
            for k in [".apk", ".aab"]:
                if j.endswith(k):
                    break
            else:
                continue

            sfn = os.path.join(i, j)

            dfn = f"bin/{config.package}-{config.version}-{j[4:]}"

            dfn = plat.path(dfn)

            shutil.copy(sfn, dfn)
            files.append(dfn)

    # Install the bundle.

    if bundle and install:
        iface.info(__("I'm installing the bundle."))

        try:
            iface.call(
                [
                    plat.java,
                    "-jar",
                    plat.path("bundletool.jar"),
                    "build-apks",
                    "--bundle=" + plat.path("project/app/build/outputs/bundle/release/app-release.aab"),
                    "--output=" + plat.path("project/app/build/outputs/bundle/release/app-release.apks"),
                    "--local-testing",
                ]
                + get_local_key_properties()
            )

            iface.call(
                [
                    plat.java,
                    "-jar",
                    plat.path("bundletool.jar"),
                    "install-apks",
                    "--apks=" + plat.path("project/app/build/outputs/bundle/release/app-release.apks"),
                    "--adb=" + plat.adb,
                ]
            )

        except subprocess.CalledProcessError:
            iface.fail(__("Installing the bundle appears to have failed."))

    # Launch.

    if launch:
        iface.info(__("Launching app."))

        launch_activity = "PythonSDLActivity"

        try:
            iface.call(
                [
                    plat.adb,
                    "shell",
                    "am",
                    "start",
                    "-W",
                    "-a",
                    "android.intent.action.MAIN",
                    f"{config.package}/org.renpy.android.{launch_activity}",
                ],
                cancel=True,
            )

        except subprocess.CalledProcessError:
            iface.fail(__("Launching the app appears to have failed."))

    if finished is not None:
        finished(files)

    iface.final_success(__("The build seems to have succeeded."))


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
    except Exception:
        rm("Sdk")
