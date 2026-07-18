from renpybuild.context import Context
from renpybuild.task import task

version = "3.4.8"


@task(kind="host", platforms="all", always=True)
def download(c: Context):
    c.var("version", version)

    url = f"https://github.com/libffi/libffi/releases/download/v{version}/libffi-{version}.tar.gz"
    dest = c.expand("libffi-{{version}}.tar.gz")

    c.download(url, dest)


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{tmp}}/tars/libffi-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run(
        """{{configure}} {{ ffi_cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """
    )
    c.run("""{{ make }}""")
    c.run("""make install """)
