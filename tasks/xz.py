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

    c.run("""{{configure}} {{ cross_config }} --enable-static --disable-shared --disable-xz --disable-xzdec --disable-lzmainfo --disable-scripts  --prefix="{{ install }}" """)

    c.run("""rm -f src/common/common_w32res.rc""")
    c.run("""touch src/common/common_w32res.rc""")

    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install """)
