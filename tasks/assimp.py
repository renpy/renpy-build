from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c : Context):
    c.clean("{{ tmp }}/source/assimp")
    c.chdir("{{ tmp }}/source")

    c.run("git clone --depth 1 --branch v5.4.3 https://github.com/assimp/assimp")

    c.chdir("assimp")
    c.patch("assimp.diff")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.env("CXXFLAGS", "-Wno-unknown-pragmas {{CXXFLAGS}}")

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DCMAKE_CXX_STANDARD=17
        -DBUILD_SHARED_LIBS=0
        -DASSIMP_NO_EXPORT=ON
        -DASSIMP_BUILD_TESTS=OFF
        -DASSIMP_BUILD_ZLIB=OFF
        {{ tmp }}/source/assimp
        """)

    try:
        c.run("cmake --build .")
    except:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")
