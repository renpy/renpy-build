from renpybuild.context import Context
from renpybuild.task import task

version = "2.14.02"


@task(kind="host", platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/nasm-{{version}}.tar.gz")


@task(kind="host", platforms="all")
def build(c: Context):
    c.var("version", version)

    c.chdir("nasm-{{version}}")
    c.run("""{{configure}} --prefix="{{install}}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install""")
