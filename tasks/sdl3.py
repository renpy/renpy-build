from renpybuild.context import Context
from renpybuild.task import task, annotator
import shutil

version = "3.4.2"



@task(kind="host", platforms="all")
def unpack(c: Context):

    if not c.args.sdl:

        c.clean()

        c.var("version", version)
        c.clean("{{ tmp }}/source/SDL3-{{version}}")
        c.chdir("{{ tmp }}/source")
        c.run("tar xzf {{source}}/SDL3-{{version}}.tar.gz")


        # c.chdir("SDL2-{{version}}")
        # c.patchdir("SDL2-{{version}}")

        # c.run("""./autogen.sh""")


@task()
def build(c: Context):
    c.var("version", version)

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DSDL_STATIC=ON
        -DSDL_SHARED=OFF
        -DSDL_CAMERA=OFF
        -DSDL_DEPS_SHARED=ON
        -DSDL_X11_XTEST=OFF
        {{ tmp }}/source/SDL3-{{version}}
        """)

    try:
        c.run("cmake --build .")
    except:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")


# @task(kind="arch-python", platforms="android", archs="x86_64", always=True)
# def rapt(c: Context):
#     c.var("version", version)
#     c.chdir("SDL2-{{version}}")
#     c.copytree("android-project/app/src/main/java/org/libsdl", "{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl")
