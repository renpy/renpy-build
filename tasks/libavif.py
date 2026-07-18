from renpybuild.context import Context
from renpybuild.task import task


@task(kind="host", platforms="all")
def download(c: Context):
    c.clean("{{ tmp }}/source/libavif")
    c.chdir("{{ tmp }}/source")

    c.clone("https://github.com/AOMediaCodec/libavif", "--branch v1.4.2")
    c.chdir("{{ tmp }}/source/libavif")
    c.run("sed -i 's/if(BUILD_SHARED_LIBS OR VCPKG_TARGET_TRIPLET)/if(1)/' CMakeLists.txt")
    c.run(
        "sed -i 's/if(APPLE)/if(APPLE AND CMAKE_HOST_SYSTEM_NAME STREQUAL \"Darwin\")/' cmake/Modules/merge_static_libs.cmake"
    )


@task(platforms="all")
def build(c: Context):
    c.clean()

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DAVIF_CODEC_AOM=SYSTEM
        -DAVIF_CODEC_AOM_ENCODE=0
        -DBUILD_SHARED_LIBS=0
        {{ tmp }}/source/libavif
        """)

    try:
        c.run("cmake --build .")
    except Exception:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")
