from renpybuild.context import Context
from renpybuild.task import task

version = "1.2.11"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/zlib-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("zlib-{{version}}")
    c.run("{{configure}} {{ configure_cross }} --static --prefix={{install}}")

    c.run(""" {{ make }} """)
    c.run("{{ make_exec }} install")


@task(platforms="web", pythons="3")
def build_web(c: Context):
    c.run("embuilder build zlib")
