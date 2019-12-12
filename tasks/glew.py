from renpybuild.model import task

version = "2.1.0"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/glew-{{version}}.tgz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("glew-{{version}}")

    # LN= prevents the shared library symlink from being madse.
    c.run("""{{ make }} install LIB.DEVLNK=libglew_shared.so OPT='{{ CFLAGS }} {{ LDFLAGS }}' CC='{{ CC }}' LD='{{ CC }}' GLEW_DEST="{{ install }}" """)
