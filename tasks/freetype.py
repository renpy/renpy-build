from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "2.13.1"


@annotator
def annotate(c: Context):
    c.include("{{ install }}/include/freetype2")


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/freetype-{{version}}.tar.gz")

    c.var("version", version)
    c.chdir("freetype-{{version}}")
    c.patch("freetype-otvalid.diff")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("freetype-{{version}}")

    c.run("""{{configure}} {{ cross_config }} --disable-shared --prefix="{{ install }}" --with-harfbuzz=no""")
    c.run("""{{ make }}""")
    c.run("""make install""")
