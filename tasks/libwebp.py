from renpybuild.model import task

version = "1.1.0"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libwebp-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("libwebp-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
