from renpybuild.model import task

version = "2.14.02"


@task(kind="host")
def unpack_nasm(c):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/nasm-{{version}}.tar.gz")


@task(kind="host")
def build_nasm(c):
    c.var("version", version)

    c.chdir("nasm-{{version}}")
    c.run("""./configure --prefix="{{install}}" """)
    c.run("""make""")
    c.run("""make install""")
