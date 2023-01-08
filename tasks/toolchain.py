from renpybuild.model import task
import zipfile


from zipfile import ZipFile, ZipInfo
import os


class ZipFileWithPermissions(ZipFile):
    """ Custom ZipFile class handling file permissions. """

    def _extract_member(self, member, targetpath, pwd):
        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        targetpath = super()._extract_member(member, targetpath, pwd)

        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(targetpath, attr)
        return targetpath


@task(kind="cross", platforms="windows")
def unpack(c):

    c.clean("{{cross}}")
    c.chdir("{{cross}}")

    c.run("tar xaf {{ tars }}/llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64.tar.xz")
    c.run("ln -s llvm-mingw-20220906-ucrt-ubuntu-18.04-x86_64 llvm-mingw")


@task(kind="cross", platforms="android")
def build(c):

    if c.path("{{cross}}/android-ndk-r25b").exists():
        return

    zf = ZipFileWithPermissions(c.path("{{ tars }}/android-ndk-r25b-linux.zip"))
    zf.extractall(c.path("{{ install }}"))
    zf.close()


@task(kind="cross", platforms="mac", archs="x86_64")
def build(c):
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
def build(c):
    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/MacOSX12.3.sdk.tar.bz2")
    c.run("ln -s MacOSX.sdk sdk")


@task(kind="cross", platforms="ios", archs="armv7s,arm64")
def build(c):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/iPhoneOS14.0.sdk.tar.gz")
    c.run("ln -s iPhoneOS14.0.sdk sdk")


@task(kind="cross", platforms="ios", archs="sim-arm64,sim-x86_64")
def build(c):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("tar xaf {{ tars }}/iPhoneSimulator14.0.sdk.tar.gz")
    c.run("ln -s iPhoneSimulator14.0.sdk sdk")


@task(platforms="ios")
def mockrt(c):
    c.clean()
    c.run("{{ CC }} {{ CFLAGS }} -c {{ source }}/mockrt.c")
    c.run("mkdir -p {{ install }}/lib")
    c.run("{{ AR }} rc {{ install }}/lib/libmockrt.a mockrt.o")
    c.run("{{ RANLIB }} {{ install }}/lib/libmockrt.a")


@task(platforms="web")
def emsdk(c):
    c.var("emsdk_version", "3.1.24")

    c.clean("{{ cross }}")
    c.run("git clone https://github.com/emscripten-core/emsdk/ {{cross}}")
    c.chdir("{{ cross }}")
    c.run("./emsdk install {{ emsdk_version }}")
    c.run("./emsdk activate {{ emsdk_version }}")


@task(platforms="web")
def embuilder(c):
    c.run("embuilder build bzip2")
    c.run("embuilder build zlib")
    c.run("embuilder build libjpeg")
    c.run("embuilder build libpng")
    c.run("embuilder build sdl2")
