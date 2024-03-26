from renpybuild.context import Context
from renpybuild.task import task

version = "5.4.2"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/xz-{{version}}.tar.gz")


@task(platforms="all")
def build(c: Context) :
    c.var("version", version)
    c.chdir("xz-{{version}}")

    if c.platform == "freebsd":
        c.env("C_INCLUDE_PATH", "/usr/include:/usr/local/include")
        c.env("CFLAGS", "{{ CFLAGS }} -L/usr/lib -L/usr/local/lib/gcc13")
        c.env("CC", "ccache gcc13 {{ CFLAGS }}")

    c.run("""{{configure}} {{ cross_config }} --enable-static --disable-shared --disable-xz --disable-xzdec --disable-lzmainfo --disable-scripts  --prefix="{{ install }}" """)

    c.run("""rm -f src/common/common_w32res.rc""")
    c.run("""touch src/common/common_w32res.rc""")

    c.run("""{{ make }}""")
    c.run("""{{ make }} install """)
