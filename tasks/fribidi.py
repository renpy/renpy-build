from renpybuild.model import task

version = "1.0.7"


@task()
def unpack_fribidi(c):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/fribidi-{{version}}.tar.bz2")


@task()
def build_fribidi(c):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
