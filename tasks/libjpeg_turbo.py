from renpybuild.model import task

# 1.5.3 is the last version that supported ./configure.
version = "1.5.3"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libjpeg-turbo-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("libjpeg-turbo-{{version}}")

    if c.platform == "ios" and "sim-x86_64" in c.arch:
        c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" --without-simd""")
    else:
        c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)

    c.run("""{{ make }}""")
    c.run("""make install """)

@task(platforms="web", pythons="3")
def build_web(c):
    c.run("embuilder build libjpeg")
