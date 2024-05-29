from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.0.14"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xJf {{source}}/fribidi-{{version}}.tar.xz")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    c.run("""
        {{ meson_configure }} {{ meson_args }}
        --prefix={{install}}
        --default-library=static
        -Ddocs=false
        -Dbin=false
        -Dtests=false
        build
        """)

    try:
        c.run("{{ meson_compile }} -C build")
    except:
        c.run("meson compile -j 1 -C build -v")

    c.run("meson install -C build")
