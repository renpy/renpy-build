from renpybuild.context import Context
from renpybuild.task import task

version = "2.6.2"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2_image-{{version}}.tar.gz")
    c.chdir("SDL2_image-{{version}}")

    c.patch("sdl2_image-avif-error.diff")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("SDL2_image-{{version}}")

    if c.platform == "windows":
        c.env("ac_cv_lib_jpeg_jpeg_CreateDecompress", "yes")

    c.run("""cp /usr/share/misc/config.sub config.sub""")

    # c.run("""./autogen.sh""")
    c.run("autoreconf -f")

    c.env("LIBAVIF_LIBS", "-lavif -ldav1d -lyuv")

    if c.platform == "web":
        c.env("SDL_CFLAGS", "-sUSE_SDL=2")
        c.env("SDL_LIBS", "-sUSE_SDL=2")

    c.run("""{{configure}} {{ cross_config }} --prefix="{{ install }}"
    --with-gnu-ld
    --disable-shared

    --disable-imageio
    --disable-stb-image

    --enable-avif
    --disable-avif-shared
    --disable-jpg-shared
    --disable-jxl
    --disable-jxl-shared
    --disable-lbm
    --disable-pcx
    --disable-png-shared
    --disable-tif
    --disable-xcf
    --disable-webp-shared
    --disable-qoi
    """)

    libtool = c.path("libtool")
    text = libtool.read_text()

    text = text.replace("cygpath -w -p", "echo")
    text = text.replace("cygpath -w", "echo")

    libtool.write_text(text)

    c.run("""{{ make }}""")
    c.run("""make install""")
