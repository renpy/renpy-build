from renpybuild.model import task

version = "2.0.5"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2_image-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("SDL2_image-{{version}}")

    if c.platform == "windows":
        c.env("ac_cv_lib_jpeg_jpeg_CreateDecompress", "yes")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}"
    --disable-shared

    --disable-tif
    --disable-imageio
    --disable-jpg-shared
    --disable-png-shared
    --enable-webp
    --disable-webp-shared
    --disable-xcf
    --disable-svg
    """)

    c.run("""{{ make }}""")
    c.run("""make install""")

