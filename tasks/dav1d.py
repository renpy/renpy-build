from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.4.3"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xJf {{source}}/dav1d-{{version}}.tar.xz")

    c.var("version", version)
    c.chdir("dav1d-{{version}}")

    c.patch("dav1d-dll-version.patch")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("dav1d-{{version}}")

    c.run("""
        {{ meson_configure }} {{ meson_args }}
        --prefix={{install}}
        --default-library=static
        -Denable_tests=false
        -Denable_tools=false
        build
        """)

    try:
        c.run("{{ meson_compile }} -C build")
    except:
        c.run("meson compile -j 1 -C build -v")

    c.run("meson install -C build")
