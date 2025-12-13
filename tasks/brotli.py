from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.1.0"

@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/brotli-{{version}}.tar.gz")

@task(platforms="all")
def build(c: Context):
    c.var("version", version)

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -B build
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=0
        brotli-{{version}}
          """)

    c.run("cmake --build build")
    c.run("cmake --install build")

@task(platforms="all", always=True)
def python(c: Context):

    c.var("version", version)
    c.chdir("brotli-{{ version }}/python")

    c.run("""install -d {{ pytmp }}/brotli""")
    c.run("""install brotli.py _brotli.c {{ pytmp }}/brotli""")

    with open(c.path("{{ pytmp }}/brotli/Setup"), "w") as f:
        f.write(c.expand("""\
_brotli _brotli.c
"""))
