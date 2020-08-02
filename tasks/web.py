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
    README = c.path("{{ renpyweb }}/README.md").read_text("utf-8")

    m = re.search(r"\./emsdk install ([\d\.]+)", README)
    c.var("emsdk_version", m.group(1))

    c.chdir("{{ renpyweb }}")
    c.run("git clone https://github.com/emscripten-core/emsdk/")
    c.chdir("{{ renpyweb }}/emsdk")
    c.run("./emsdk install {{ emsdk_version }}")
    c.run("./emsdk activate {{ emsdk_version }}")

@task(kind="host-python", platforms="web")
def patch_emsdk(c):
    c.chdir("{{ renpyweb }}/emsdk/upstream/emscripten/")
    c.patch("{{ renpyweb }}/patches/emscripten.patch")

def read_environment(c):
    """
    Loads the emsdk environment into `c`.
    """

    rv = dict(os.environ)
    rv["EMSDK_BASH"] = "1"

    bash = subprocess.check_output([ str(c.path("{{ renpyweb }}/emsdk/emsdk")), "construct_env" ], env=rv, text=True)

    for l in bash.split("\n"):
        m = re.match(r'export (\w+)=\"(.*?)\";$', l)
        if m:
            rv[m.group(1)] = m.group(2)

    return rv

@task(kind="host-python", platforms="web", always=True)
def build(c):
    environ = read_environment(c)
    subprocess.check_call("make cythonemscriptenclean", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)    
    subprocess.check_call("nice make EMCC='ccache emcc'", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)
    subprocess.check_call("scripts/install_in_renpy.sh", shell=True, cwd=str(c.path("{{ renpyweb }}")), env=environ)