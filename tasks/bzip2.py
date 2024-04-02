from renpybuild.context import Context
from renpybuild.task import task

version = "1.0.8"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/bzip2-{{version}}.tar.gz")

    c.chdir("bzip2-{{version}}")
    c.patch("bzip2-no-tests.diff")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("bzip2-{{version}}")

    c.run("""{{ make }} AR="{{ AR }}" RANLIB="{{ RANLIB }}" CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
    c.run("""touch bzip2 bunzip2 bzip2recover bzgrep bzmore bzdiff""")

    c.run("""{{ make_exec }} install PREFIX="{{ install }}" AR="{{ AR }}" RANLIB="{{ RANLIB }}" CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
