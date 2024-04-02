from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.0.7"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/fribidi-{{version}}.tar.bz2")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    if c.platform != "freebsd":
        c.run("""cp /usr/share/misc/config.sub config.sub""")

    c.run("""{{configure}} {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install """)
