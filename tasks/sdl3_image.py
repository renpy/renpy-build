from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "3.4.0"


@task(kind="host", platforms="all", always=True)
def download(c: Context):
    c.var("version", version)

    url = f"https://github.com/libsdl-org/SDL_image/releases/download/release-{ version }/SDL3_image-{ version }.tar.gz"
    dest = c.expand("SDL3_image-{{version}}.tar.gz")

    c.download(url, dest)

@task(kind="host", platforms="all")
def unpack(c: Context):
    c.var("version", version)

    c.clean("{{ tmp }}/source/SDL3_image-{{version}}")
    c.chdir("{{ tmp }}/source")
    c.run("tar xzf {{tmp}}/tars/SDL3_image-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)

    c.clean()

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=OFF
        -DSDLIMAGE_DEPS_SHARED=OFF
        -DSDLIMAGE_BACKEND_STB=OFF
        -DSDLIMAGE_ANI_SAVE=OFF
        -DSDLIMAGE_AVIF_SAVE=OFF
        -DSDLIMAGE_GIF_SAVE=OFF
        -DSDLIMAGE_WEBP_SAVE=OFF
        -DSDLIMAGE_SAMPLES=OFF

        {{ tmp }}/source/SDL3_image-{{version}}
        """)

    try:
        c.run("cmake --build .")
    except:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")
