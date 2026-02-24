from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "3.4.2"


@task(kind="host", platforms="all", always=True)
def download(c: Context):
    c.var("version", version)

    url = f"https://github.com/libsdl-org/SDL/releases/download/release-{ version }/SDL3-{ version }.tar.gz"
    dest = c.expand("SDL3-{{version}}.tar.gz")

    c.download(url, dest)

@task(kind="host", platforms="all")
def unpack(c: Context):

    if not c.args.sdl:

        c.clean()

        c.var("version", version)
        c.clean("{{ tmp }}/source/SDL3-{{version}}")
        c.chdir("{{ tmp }}/source")
        c.run("tar xzf {{tmp}}/tars/SDL3-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)

    c.clean()

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DSDL_STATIC=ON
        -DSDL_SHARED=OFF
        -DSDL_CAMERA=OFF
        -DSDL_DEPS_SHARED=ON
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
