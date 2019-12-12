from renpybuild.model import task

version = "1.0.8"


@task()
def unpack_bzip2(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/bzip2-{{version}}.tar.gz")

    c.chdir("bzip2-{{version}}")
    c.patch("bzip2-no-tests.diff")


@task()
def build_bzip2(c):
    c.var("version", version)
    c.chdir("bzip2-{{version}}")

    c.run("""{{ make }} CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
    c.run("""touch bzip2 bunzip2 bzip2recover bzgrep bzmore bzdiff""")
    c.run("""make install PREFIX="{{ install }}" CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
