from renpybuild.model import task

version = "3.3"


@task()
def unpack_libffi(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libffi-{{version}}.tar.gz")


@task()
def build_libffi(c):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
