from renpybuild.model import task
import zipfile

binutils_version = "2.33.1"
gcc_version = "9.2.0"


@task(kind="cross", platforms="linux")
def build(c):
    c.var("binutils_version", binutils_version)
    c.var("gcc_version", gcc_version)

    if c.path("{{ install }}/bin/{{ host_platform }}-gcc").exists():
        return

    c.clean()

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


@task(kind="cross", platforms="mac")
def build(c):

    if c.path("{{ install }}/bin/{{ host_platform }}-cc").exists():
        return

    c.clean()

    c.run("git clone https://github.com/tpoechtrager/osxcross")
    c.chdir("osxcross")

    c.copy("{{ tars }}/MacOSX10.10.sdk.tar.bz2", "tarballs")

    c.env("TARGET_DIR", "{{ install }}")
    c.env("UNATTENDED", "1")
    c.env("MAKE", "{{ make }}")

    c.run("./build.sh")


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


@task(kind="cross", platforms="ios", archs="armv7s,arm64")
def build(c):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("git clone https://github.com/tpoechtrager/cctools-port")
    c.chdir("cctools-port/usage_examples/ios_toolchain")
    # c.run("git checkout 606eb7dcb21ea90df1d36cd6b67e04c23cafe705")

    c.run("./build.sh {{tars}}/iPhoneOS14.0.sdk.tar.gz {{ c.arch }}")

    c.chdir("{{ cross }}")
    c.run("ln -s cctools-port/usage_examples/ios_toolchain/target/bin bin")


@task(kind="cross", platforms="ios", archs="x86_64")
def build(c):

    c.clean("{{ cross }}")
    c.chdir("{{ cross }}")

    c.run("git clone https://github.com/tpoechtrager/cctools-port")
    c.chdir("cctools-port/usage_examples/ios_toolchain")

    c.run("ls")

    with open(c.path("build.sh"), "r") as f:
        data = f.read()

    data = data.replace("iPhoneOS", "iPhoneSimulator")
    data = data.replace("arm-apple-darwin11", "x86_64-apple-darwin11")

    with open(c.path("build.sh"), "w") as f:
        f.write(data)

    c.run("./build.sh {{tars}}/iPhoneSimulator14.0.sdk.tar.gz {{ c.arch }}")

    c.chdir("{{ cross }}")
    c.run("ln -s cctools-port/usage_examples/ios_toolchain/target/bin bin")

