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

    if c.platform == "freebsd":
        c.env("C_INCLUDE_PATH", "/usr/include:/usr/local/include")
        c.env("CFLAGS", "{{ CFLAGS }} -L/usr/lib -L/usr/local/lib/gcc13")
        # fix a weird linking bug where these system files were hardcoded
        c.run("cp -rf /usr/lib/crt1.o .")
        c.run("cp -rf /usr/lib/crti.o .")
        c.run("cp -rf /usr/lib/crtbegin.o .")
        c.run("cp -rf /usr/lib/crtend.o .")
        c.run("cp -rf /usr/lib/crtn.o .")

    c.run("""{{ make }} AR="{{ AR }}" RANLIB="{{ RANLIB }}" CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
    c.run("""touch bzip2 bunzip2 bzip2recover bzgrep bzmore bzdiff""")

    c.run("""{{ make }} install PREFIX="{{ install }}" AR="{{ AR }}" RANLIB="{{ RANLIB }}" CC="{{ CC }}" CFLAGS="{{ CFLAGS }} -D_FILE_OFFSET_BITS=64" """)
