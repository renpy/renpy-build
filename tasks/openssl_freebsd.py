from renpybuild.context import Context
from renpybuild.task import task

version = "1.1.1s"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("openssl-{{version}}")

    c.env("CC", "ccache clang15")
    c.run("""./Configure cc shared threads -lpthread --prefix="{{ host }}" """)

    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install_sw""")
