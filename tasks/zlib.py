from renpybuild.model import task

version = "1.2.11"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/zlib-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("zlib-{{version}}")

    c.run("./configure {{ configure_cross }} --static --prefix={{install}}")
    c.run("{{ make }}")
    c.run("make install")
