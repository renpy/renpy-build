from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "2.13.1"


@annotator
def annotate(c: Context):
    c.include("{{ install }}/include/freetype2")


@task(kind="host", platforms="all")
def hostunpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/freetype-{{version}}.tar.gz")

    c.var("version", version)
    c.chdir("freetype-{{version}}")
    c.patch("freetype-otvalid.diff")


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/freetype-{{version}}.tar.gz")

    c.var("version", version)
    c.chdir("freetype-{{version}}")
    c.patch("freetype-otvalid.diff")


@task(kind="host", platforms="all")
def hostbuild(c: Context):
    c.var("version", version)
    c.chdir("freetype-{{version}}")

    c.run("""{{configure}} --prefix="{{ install }}" --with-harfbuzz=no""")
    c.run("""cp {{source}}/ftoption.h builds/unix/""")
    c.run("""cp {{source}}/ftoption.h builds/mac/""")
    c.run("""cp {{source}}/ftoption.h builds/windows/""")
    c.run("""{{ make }}""")
    c.run("""cp objs/apinames {{host}}/freetype-apinames""")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("freetype-{{version}}")

    c.run("""{{configure}} {{ cross_config }} --disable-shared --prefix="{{ install }}" --with-harfbuzz=no""")
    c.run("""cp {{source}}/ftoption.h builds/unix/""")
    c.run("""cp {{source}}/ftoption.h builds/mac/""")
    c.run("""cp {{source}}/ftoption.h builds/windows/""")
    c.run("""mkdir -p objs""")
    c.run("""cp {{host}}/freetype-apinames objs/apinames""")
    c.run("""cp {{host}}/freetype-apinames objs/apinames.exe""")
    c.run("""touch objs/apinames objs/apinames.exe""")
    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install""")
