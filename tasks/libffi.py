from renpybuild.model import task

version = "3.3"


@task(platforms="-web")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libffi-{{version}}.tar.gz")


@task(platforms="-web")
def build(c):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run("""{{ configure }} {{ ffi_cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make }} install """)
