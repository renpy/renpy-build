from renpybuild.context import Context
from renpybuild.task import task

version = "3.02"


@task(kind="host", platforms="all")
def download(c: Context):
    c.var("version", version)
    c.download("https://www.nasm.us/pub/nasm/releasebuilds/{{ version }}/nasm-{{ version }}.tar.xz", "nasm-{{ version }}.tar.xz")


@task(kind="host", platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{ tmp }}/tars/nasm-{{version}}.tar.xz")


@task(kind="host", platforms="all")
def build(c: Context):
    c.var("version", version)

    c.chdir("nasm-{{version}}")
    c.run("""{{configure}} --prefix="{{install}}" """)
    c.run("""{{ make }}""")
    c.run("""make install""")
