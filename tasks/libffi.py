from renpybuild.context import Context
from renpybuild.task import task

version = "3.4.6"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libffi-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run("""{{configure}} {{ ffi_cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)


@task(platforms="web")
def build_web(c: Context):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    # Adapted from cpython/Tools/wasm/emscripten/make_libffi.sh
    c.env("CFLAGS", "-O3 -fPIC -DWASM_BIGINT")
    c.env("CXXFLAGS", "{{ CFLAGS }}")

    c.run("""
        {{configure}}
        --host="wasm32-unknown-linux"
        --prefix="{{ install }}"
        --enable-static
        --disable-shared
        --disable-dependency-tracking
        --disable-builddir
        --disable-multi-os-directory
        --disable-raw-api
        --disable-docs
        """)
    c.run("""make install """)

    c.copy("fficonfig.h", "{{ install }}/include/ffi_common.h")
    c.copy("include/ffi_common.h", "{{ install }}/include/ffi_common.h")
