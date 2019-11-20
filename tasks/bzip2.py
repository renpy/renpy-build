from renpybuild.model import task

version = "1.0.8"


@task()
def unpack_bzip2(c):
    c.var("version", version)
    c.run("tar xzf {{source}}/bzip2-{{version}}.tar.gz")


@task(always=True)
def build_bzip2(c):
    c.var("version", version)
    c.chdir("bzip2-{{version}}")

    c.env("CC", "ccache gcc")
    c.env("CFLAGS", "{{ CFLAGS }} -D_FILE_OFFSET_BITS=64")
    c.env("PREFIX", "{{ install }}")

    c.run("""
make
    CC="{{ CC }}"
    CFLAGS="{{ CFLAGS }}"
""")

    c.run("""
make install
    PREFIX="{{ install }}"
""")
