from renpybuild.model import task

binutils_version = "2.33.1"
gcc_version = "5.3.0"


@task(kind="cross")
def build_toolchain(c):
    c.var("binutils_version", binutils_version)
    c.var("gcc_version", gcc_version)

    c.clean()

    c.run("tar xaf {{ source }}/binutils-{{ binutils_version }}.tar.gz")
    c.chdir("binutils-{{ binutils_version }}")

    c.run("./configure --target={{ host_platform }} --prefix={{ install }}")
    c.run("{{ make }}")
    c.run("make install")

    c.chdir("{{ build }}")

    c.run("tar xaf {{ source }}/gcc-{{ gcc_version }}.tar.gz")
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
    """, verbose=True)

    c.run("{{ make }}")
    c.run("make install")

    import sys
    sys.exit(0)
