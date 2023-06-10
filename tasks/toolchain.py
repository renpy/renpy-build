from renpybuild.context import Context
from renpybuild.task import task

import os
import requests


@task(kind="cross", platforms="windows")
def download(c: Context):

    url = "https://github.com/mstorsjo/llvm-mingw/releases/download/20220906/llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64.tar.xz"
    dest = c.path("{{ tmp }}/tars/llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64.tar.xz")

    if os.path.exists(dest):
        return

    dest.parent.mkdir(parents=True, exist_ok=True)

    print("Downloading windows toolchain.")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest.with_suffix(".tmp"), "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                f.write(chunk)

    dest.with_suffix(".tmp").rename(dest)


@task(kind="cross", platforms="windows")
def unpack(c: Context):

    c.clean("{{cross}}")
    c.chdir("{{cross}}")

    c.run("tar xaf {{ tmp }}/tars/llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64.tar.xz")
    c.run("ln -s llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64 llvm-mingw")


@task(kind="cross", platforms="windows", always=True)
def usrinclude(c: Context):
    c.chdir("{{cross}}")

    c.run("mkdir -p llvm-mingw/usr/include")
    c.run("mkdir -p llvm-mingw/aarch64-w64-mingw32/usr/include")
    c.run("mkdir -p llvm-mingw/armv7-w64-mingw32/usr/include")
    c.run("mkdir -p llvm-mingw/i686-w64-mingw32/usr/include")
    c.run("mkdir -p llvm-mingw/x86_64-w64-mingw32/usr/include")


@task(kind="cross", platforms="android", always=True)
def build(c: Context):

    if c.path("{{cross}}/android-ndk-r25b").exists():
        return

    c.clean("{{cross}}")
    c.chdir("{{cross}}")

    c.run("""unzip -q {{ tars }}/android-ndk-r25b-linux.zip""")


@task(kind="cross", platforms="mac", archs="x86_64")
def build(c: Context):
    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/MacOSX10.10.sdk.tar.bz2")
    c.run("ln -s MacOSX10.10.sdk sdk")

    # This should go away when the SDK is updated.
    with open(c.path("sdk/SDKSettings.json"), "w") as f:
        f.write("""\
{
	"CanonicalName": "macosx10.10",
	"CustomProperties":
	{
		"KERNEL_EXTENSION_HEADER_SEARCH_PATHS": "$(KERNEL_FRAMEWORK)/PrivateHeaders $(KERNEL_FRAMEWORK_HEADERS)"
	},
	"DefaultProperties":
	{
		"MACOSX_DEPLOYMENT_TARGET": "10.10",
		"PLATFORM_NAME": "macosx",
		"DEFAULT_KEXT_INSTALL_PATH": "$(LIBRARY_KEXT_INSTALL_PATH)"
	},
	"DisplayName": "OS X 10.10",
	"MaximumDeploymentTarget": "10.10",
	"MinimalDisplayName": "10.10",
	"MinimumSupportedToolsVersion": "3.2",
	"SupportedBuildToolComponents": ["com.apple.compilers.gcc.headers.4_2"],
	"Version": "10.10",
	"isBaseSDK": "YES"
}
""")


@task(kind="cross", platforms="mac", archs="arm64")
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
    c.var("emsdk_version", "3.1.24")

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
    c.run("embuilder build sdl2")
