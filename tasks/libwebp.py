from renpybuild.model import task

version = "1.0.3"


@task()
def unpack_libwebp(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libwebp-{{version}}.tar.gz")


@task()
def build_libwebp(c):
    c.var("version", version)
    c.chdir("libwebp-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""make install """)
