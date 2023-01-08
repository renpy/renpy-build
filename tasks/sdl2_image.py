from renpybuild.model import task

version = "2.6.2"


@task(platforms="all")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2_image-{{version}}.tar.gz")


@task(platforms="all")
def build(c):
    c.var("version", version)
    c.chdir("SDL2_image-{{version}}")

    if c.platform == "windows":
        c.env("ac_cv_lib_jpeg_jpeg_CreateDecompress", "yes")

    c.run("""cp /usr/share/misc/config.sub config.sub""")

    # c.run("""./autogen.sh""")
    c.run("autoreconf -f")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}"
    --disable-shared

    --disable-imageio
    --disable-stb-image

    --disable-avif
    --disable-jpg-shared
    --disable-jxl-shared
    --disable-lbm
    --disable-pcx
    --disable-png-shared
    --disable-tif
    --disable-xcf
    --disable-webp-shared
    --disable-qoi
    """)

    c.run("""make""")
    c.run("""make install""")
