from renpybuild.model import task
import zipfile

binutils_version = "2.33.1"
gcc_version = "9.2.0"


@task(kind="cross", platforms="linux", always=True)
def build(c):
    c.var("binutils_version", binutils_version)
    c.var("gcc_version", gcc_version)

    if c.path("{{ install }}/bin/{{ host_platform }}-gcc").exists():
        return

    c.clean()

    c.env("CC", "ccache gcc-9")
    c.env("CXX", "ccache g++-9")

    c.run("tar xaf {{ tars }}/binutils-{{ binutils_version }}.tar.gz")
    c.chdir("binutils-{{ binutils_version }}")

    c.run("./configure --target={{ host_platform }} --prefix={{ install }}")

    c.run("{{ make }}")
    c.run("make install")

    c.chdir("{{ build }}")

    c.run("tar xaf {{ tars }}/gcc-{{ gcc_version }}.tar.gz")
    c.path("{{ build }}/gcc-{{ gcc_version }}/build").mkdir()
    c.chdir("{{ build }}/gcc-{{ gcc_version }}/build")


    c.run("""
    ../configure
    --build={{ build_platform }}
    --host={{ build_platform }}
    --target={{ host_platform }}
    --prefix={{ install }}
    --with-build-sysroot={{ sysroot }}
    --with-sysroot={{ sysroot }}
    --enable-languages=c,c++
    --with-multiarch
    --disable-multilib
    --disable-bootstrap

    {% if (c.platform == "linux") and (c.arch == "armv7l" ) %}
    --with-arch=armv6 --with-fpu=vfp --with-float=hard
    {% endif %}
    """, verbose=True)

    c.run("{{ make }}")
    c.run("make install")


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


@task(kind="cross", platforms="android")
def build(c):

    if c.path("{{cross}}/android-ndk-r21d").exists():
        return

    zf = ZipFileWithPermissions(c.path("{{ tars }}/android-ndk-r21d-linux-x86_64.zip"))
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
