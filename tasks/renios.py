import os
import re
import subprocess
import zipfile

from renpybuild.context import Context
from renpybuild.task import task


@task(kind="host")
def download(c: Context):
    url = "https://github.com/mikr/xcodeprojer/archive/refs/heads/master.zip"
    dest = c.expand("xcodeprojer-master.zip")

    c.download(url, dest)


@task(kind="host")
def unpack(c: Context):
    c.clean("{{ tmp }}/source/xcodeprojer-master")

    with zipfile.ZipFile(c.path("{{ tmp }}/tars/xcodeprojer-master.zip")) as zf:
        zf.extractall(c.path("{{ tmp }}/source"))


@task(kind="host", always=True)
def copytree(c: Context):
    c.copytree("{{ root }}/renios", "{{ renios }}")

    c.copy("{{ tmp }}/source/xcodeprojer-master/xcodeprojer.py", "{{ renios }}/buildlib/xcodeprojer.py")

    c.rmtree("{{ renios }}/prototype/prebuilt")
    c.rmtree("{{ renios }}/prototype/base")
    c.rmtree("{{ renios }}/prototype/prototype.xcodeproj/project.xcworkspace")
    c.rmtree("{{ renios }}/prototype/prototype.xcodeproj/xcshareddata")
    c.rmtree("{{ renios }}/prototype/prototype.xcodeproj/xcuserdata")

    c.run("""find {{ renios }}/prototype/ -name ._* -delete""")


def check_sdk(c: Context, name, paths):

    for d in paths:
        fn = d / name

        p = subprocess.run([c.expand("{{ otool }}"), "-l", f"{fn}"], capture_output=True)

        obj = None

        for l in p.stdout.decode("utf-8").split("\n"):
            if re.match(r'.*\.a\(.*\)', l):
                if obj is not None and not ("asm" in obj):
                    raise Exception(f"{obj} does not have a minos defined, in {fn}")

                obj = l

            if "minos" in l:
                obj = None

def lipo(c: Context, namefilter):

    paths = [
        c.path("{{ tmp }}/install.ios-arm64/lib"),
        ]

    c.run("install -d {{ renios }}/prototype/prebuilt/release")

    for i in paths[0].glob("*.a"):
        if i.is_symlink():
            continue

        i = i.name

        if not namefilter(i):
            continue

        check_sdk(c, i, paths)

        print("(Release) Lipo and strip:", i)

        c.var("i", i)
        c.run("""
        {{ lipo }}
        -create
        -segalign arm64 8
{% for p in paths %}
        {{ p }}/{{ i }}
{% endfor %}
        -output {{ renios }}/prototype/prebuilt/release/{{ i }}
        """, paths=paths)

        os.chmod(c.path("{{ renios }}/prototype/prebuilt/release/{{ i }}"), 0o755)

    # debug.

    paths = [
        c.path("{{ tmp }}/install.ios-sim-x86_64/lib"),
        c.path("{{ tmp }}/install.ios-sim-arm64/lib"),
        ]

    c.run("install -d {{ renios }}/prototype/prebuilt/debug")

    for i in paths[0].glob("*.a"):
        if i.is_symlink():
            continue

        i = i.name

        if not namefilter(i):
            continue

        check_sdk(c, i, paths)

        print("(Debug) Lipo and strip:", i)

        c.var("i", i)
        c.run("""
        {{ lipo }}
        -create
        -segalign arm64 8
        -segalign x86_64 8
{% for p in paths %}
        {{ p }}/{{ i }}
{% endfor %}
        -output {{ renios }}/prototype/prebuilt/debug/{{ i }}
        """, paths=paths)

        os.chmod(c.path("{{ renios }}/prototype/prebuilt/debug/{{ i }}"), 0o755)


@task(kind="platform", platforms="ios")
def lipo_all(c: Context):

    def namefilter(i):

        if i.startswith("libpython") and not i.startswith("libpython3"):
            return False

        return True

    lipo(c, namefilter)

@task(kind="platform", platforms="ios", always=True)
def lipo_renpy(c: Context):
    lipo(c, lambda n : "librenpy" in n)


@task(kind="platform", platforms="ios", always=True)
def unpack_metalangle(c: Context):
    c.clean("{{ renios }}/prototype/Frameworks")
    c.chdir("{{ renios }}/prototype/Frameworks")

    c.run("tar xaf {{ source }}/MetalANGLE.xcframework.tar.gz")
