from renpybuild.model import task

version = "2.0.5"


@task()
def unpack_sdl2image(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2_image-{{version}}.tar.gz")


@task()
def build_sdl2image(c):
    c.var("version", version)
    c.chdir("SDL2_image-{{version}}")

    c.run("""./configure {{ config_cross }} --prefix="{{ install }}"
    --disable-shared

    --disable-tif
    --disable-imageio
    --disable-jpg-shared
    --disable-png-shared
    --enable-webp
    --disable-webp-shared
    --disable-xcf
    """)

    c.run("""make""")
    c.run("""make install""")
