from renpybuild.context import Context
from renpybuild.task import task

version = "3.4.2"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libffi-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run("""{{configure}} {{ ffi_cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
