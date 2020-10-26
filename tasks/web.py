from renpybuild.model import task, annotator
import subprocess
import os
import re


@task(kind="host-python", platforms="web")
def clean(c):
    c.rmtree("{{ renpyweb }}/build")
    c.rmtree("{{ renpyweb }}/install")
    c.rmtree("{{ renpyweb }}/toolchain")
    c.rmtree("{{ renpyweb }}/emsdk")


@task(kind="host-python", platforms="web")
def links(c):
    c.unlink("{{ renpyweb }}/renpy")
    c.unlink("{{ renpyweb }}/pygame_sdl2")

    c.symlink("{{ renpy }}", "{{ renpyweb }}/renpy")
    c.symlink("{{ pygame_sdl2 }}", "{{ renpyweb }}/pygame_sdl2")


@task(kind="host-python", platforms="web")
def download_emsdk(c):
    c.var("emsdk_version", "2.0.7")

    c.chdir("{{ renpyweb }}")
    c.run("git clone https://github.com/emscripten-core/emsdk/")
    c.chdir("{{ renpyweb }}/emsdk")
    c.run("./emsdk install {{ emsdk_version }}")
    c.run("./emsdk activate {{ emsdk_version }}")


@task(kind="host-python", platforms="web")
def patch_emsdk(c):
    c.chdir("{{ renpyweb }}/emsdk/upstream/emscripten/")
    c.patch("{{ renpyweb }}/patches/emscripten.patch")


@task(kind="host-python", platforms="web", always=True)
def clean_python_emscripten(c):
    newmakefile = c.path("{{ renpyweb }}/Makefile")
    oldmakefile = c.path("{{ build }}/Makefile")

    new = newmakefile.read_text()
    if not oldmakefile.exists():
        old = ''
    else:
        old = oldmakefile.read_text()

    if new != old:

        if int(os.environ.get("RENPYWEB_CLEAN", "1")):
            c.unlink("{{ renpyweb }}/python-emscripten.fossil")
            c.rmtree("{{ renpyweb }}/python-emscripten")
            c.rmtree("{{ renpyweb }}/build")
            c.rmtree("{{ renpyweb }}/install")

        oldmakefile.write_text(new)


def read_environment(c):
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


@task(kind="host-python", platforms="web", always=True)
def build(c):
    environ = read_environment(c)
    subprocess.check_call("make cythonobjclean", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
    subprocess.check_call("nice make EMCC='ccache emcc'", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
    subprocess.check_call("scripts/install_in_renpy.sh", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
