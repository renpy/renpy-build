from renpybuild.context import Context
from renpybuild.task import task

import os
import requests

mingw_version = "20241217-ucrt-ubuntu-20.04-x86_64"


@task(kind="cross", platforms="windows")
def download(c: Context):

    c.var("mingw_version", mingw_version)

    url = "https://github.com/mstorsjo/llvm-mingw/releases/download/20241217/llvm-mingw-20241217-ucrt-ubuntu-20.04-x86_64.tar.xz"
    dest = f"llvm-mingw-{mingw_version}.tar.xz"

    c.download(url, dest)


@task(kind="cross", platforms="windows")
def unpack(c: Context):
    c.var("mingw_version", mingw_version)

    c.clean("{{cross}}")
    c.chdir("{{cross}}")

    c.run("tar xaf {{ tmp }}/tars/llvm-mingw-{{mingw_version}}.tar.xz")
    c.run("ln -s llvm-mingw-{{mingw_version}} llvm-mingw")


@task(kind="cross", platforms="android", always=True)
def build(c: Context):

    if c.path("{{cross}}/{{ndk_version}}").exists():
        return

    c.clean("{{cross}}")
    c.chdir("{{cross}}")

    c.run("""unzip -q {{ tars }}/{{ndk_version}}-linux.zip""")

@task(kind="cross", platforms="mac")
def build(c: Context):
    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/MacOSX12.3.sdk.tar.bz2")
    c.run("ln -s MacOSX.sdk sdk")


@task(kind="cross", platforms="ios", archs="armv7s,arm64")
def build(c: Context):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/iPhoneOS14.0.sdk.tar.gz")
    c.run("ln -s iPhoneOS14.0.sdk sdk")


@task(kind="cross", platforms="ios", archs="sim-arm64,sim-x86_64")
def build(c: Context):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/iPhoneSimulator14.0.sdk.tar.gz")
    c.run("ln -s iPhoneSimulator14.0.sdk sdk")


@task(platforms="ios")
def mockrt(c: Context):
    c.clean()
    c.run("{{ CC }} {{ CFLAGS }} -c {{ source }}/mockrt.c")
    c.run("mkdir -p {{ install }}/lib")
    c.run("{{ AR }} rc {{ install }}/lib/libmockrt.a mockrt.o")
    c.run("{{ RANLIB }} {{ install }}/lib/libmockrt.a")


@task(platforms="web")
def emsdk(c: Context):
    # c.var("emsdk_version", "3.1.67")
    c.var("emsdk_version", "5.0.2")

    c.clean("{{ cross }}")
    c.run("git clone https://github.com/emscripten-core/emsdk/ {{cross}}")
    c.chdir("{{ cross }}")
    c.run("./emsdk install {{ emsdk_version }}")
    c.run("./emsdk activate {{ emsdk_version }}")


@task(platforms="web")
def embuilder(c: Context):
    c.run("embuilder build bzip2")
    c.run("embuilder build zlib")
    c.run("embuilder build libjpeg")
    c.run("embuilder build libpng")
    c.run("embuilder build sdl3")
