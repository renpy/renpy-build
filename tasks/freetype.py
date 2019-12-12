from renpybuild.model import task, annotator

version = "2.10.1"


@annotator
def annotate(c):
    c.include("{{ install }}/include/freetype2")


@task(kind="host")
def hostunpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/freetype-{{version}}.tar.gz")


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/freetype-{{version}}.tar.gz")


@task(kind="host")
def hostbuild(c):
    c.var("version", version)
    c.chdir("freetype-{{version}}")

    c.run("""./configure --prefix="{{ install }}" --with-harfbuzz=no""")
    c.run("""cp {{source}}/ftoption.h builds/unix/""")
    c.run("""cp {{source}}/ftoption.h builds/mac/""")
    c.run("""cp {{source}}/ftoption.h builds/windows/""")
    c.run("""{{ make }}""")
    c.run("""cp objs/apinames {{host}}/freetype-apinames""")


@task()
def build(c):
    c.var("version", version)
    c.chdir("freetype-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" --with-harfbuzz=no""")
    c.run("""cp {{source}}/ftoption.h builds/unix/""")
    c.run("""cp {{source}}/ftoption.h builds/mac/""")
    c.run("""cp {{source}}/ftoption.h builds/windows/""")
    c.run("""mkdir -p objs""")
    c.run("""cp {{host}}/freetype-apinames objs/apinames""")
    c.run("""cp {{host}}/freetype-apinames objs/apinames.exe""")
    c.run("""touch objs/apinames objs/apinames.exe""")
    c.run("""{{ make }}""")
    c.run("""make install""")
