from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "8.0.1"


@annotator
def annotate(c: Context):
    c.include("{{ install }}/include/harfbuzz")


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/harfbuzz-{{version}}.tar.xz")



@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("harfbuzz-{{version}}")

    c.run("""./configure {{ cross_config }}
          --disable-shared
          --prefix="{{ install }}"
          --with-libstdc++=no
          --with-glib=no
          --with-gobject=no
          --with-cairo=no
          --with-chafa=no
          --with-icu=no
          --with-graphite2=no
          --with-freetype=yes
          --with-uniscribe=no
          --with-gdi=no
          --with-directwrite=no
          --with-coretext=no
          """)

    c.run("{{make}} V=1")
    c.run("{{make}} install")
