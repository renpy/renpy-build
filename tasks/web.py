from renpybuild.context import Context
from renpybuild.task import task, annotator
import subprocess
import os
import re



@task(kind="host-python", platforms="web", pythons="2")
def clean(c: Context):
    c.rmtree("{{ renpyweb }}/build")
    c.rmtree("{{ renpyweb }}/install")
    c.rmtree("{{ renpyweb }}/toolchain")
    c.rmtree("{{ renpyweb }}/emsdk")
    c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/build")
    c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/crosspython-dynamic")
    c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/crosspython-static")


@task(kind="host-python", platforms="web", pythons="2")
def links(c: Context):
    c.unlink("{{ renpyweb }}/renpy")
    c.unlink("{{ renpyweb }}/pygame_sdl2")

    c.symlink("{{ renpy }}", "{{ renpyweb }}/renpy")
    c.symlink("{{ pygame_sdl2 }}", "{{ renpyweb }}/pygame_sdl2")


@task(kind="host-python", platforms="web", pythons="2")
def download_emsdk(c: Context):
    c.var("emsdk_version", "2.0.20")

    c.chdir("{{ renpyweb }}")
    c.run("git clone https://github.com/emscripten-core/emsdk/")
    c.chdir("{{ renpyweb }}/emsdk")
    c.run("./emsdk install {{ emsdk_version }}")
    c.run("./emsdk activate {{ emsdk_version }}")


@task(kind="host-python", platforms="web", pythons="2")
def patch_emsdk(c: Context):
    c.chdir("{{ renpyweb }}/emsdk/upstream/emscripten/")
    c.patch("{{ renpyweb }}/patches/emscripten.patch")

@task(kind="host-python", platforms="web", always=True, pythons="2")
def clean_python_emscripten(c: Context):
    newmakefile = c.path("{{ renpyweb }}/Makefile")
    oldmakefile = c.path("{{ build }}/Makefile")

    new = newmakefile.read_text()
    if not oldmakefile.exists():
        old = ''
    else:
        old = oldmakefile.read_text()

    if new != old:

        if int(os.environ.get("RENPYWEB_CLEAN", "1")):
            c.rmtree("{{ renpyweb }}/build")
            c.rmtree("{{ renpyweb }}/install")
            c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/build")
            c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/crosspython-dynamic")
            c.rmtree("{{ renpyweb }}/python-emscripten/2.7.18/crosspython-static")

        oldmakefile.write_text(new)


def read_environment(c: Context):
    """
    Loads the emsdk environment into `c`.
    """

    rv = dict(os.environ)
    rv["EMSDK_BASH"] = "1"

    bash = subprocess.check_output([ str(c.path("{{ renpyweb }}/emsdk/emsdk")), "construct_env" ], env=rv, text=True)

    for l in bash.split("\n"):
        m = re.match(r'export (\w+)=\"(.*?)\";?$', l)
        if m:
            rv[m.group(1)] = m.group(2)

    return rv


@task(kind="python", platforms="web", always=True, pythons="2")
def inittab(c: Context):

    modules = [ ]

    def read_setup(dn):

        with open(dn / "Setup") as f:
            for l in f:
                l = l.partition("#")[0]
                l = l.strip()

                if not l:
                    continue

                parts = l.split()

                if "live2d" in parts[0]:
                    continue

                if "renpy.text.hbfont" in parts[0]:
                    continue

                modules.append(parts[0])

    read_setup(c.pygame_sdl2)
    read_setup(c.renpy / "module")

    c.generate("{{ runtime }}/librenpy_inittab{{ c.python }}.c", "{{ renpyweb }}/inittab.c", modules=modules)

    if c.path("{{ renpyweb }}/build/inittab.bc").exists():
        c.unlink("{{ renpyweb }}/build/inittab.bc")


@task(kind="host-python", platforms="web", always=True, pythons="2")
def build(c: Context):
    environ = read_environment(c)
    subprocess.check_call("make cythonobjclean", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
    subprocess.check_call("nice make EMCC='ccache emcc'", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
    subprocess.check_call("scripts/install_in_renpy.sh", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
