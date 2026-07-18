from renpybuild.context import Context
from renpybuild.task import task

version = "1.1.0"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/brotli-{{version}}.tar.gz")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)

    if c.platform == "ios":
        c.var("brotli_cmake_args", "-DCMAKE_MACOSX_BUNDLE=OFF -DBROTLI_DISABLE_TESTS=ON")
    else:
        c.var("brotli_cmake_args", "")

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -B build
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=0
        {{ brotli_cmake_args }}
        brotli-{{version}}
          """)

    c.run("cmake --build build")
    c.run("cmake --install build")
