from renpybuild.context import Context
from renpybuild.task import task

version = "1.2.11"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/zlib-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("zlib-{{version}}")
#    if c.platform == "freebsd":
#        c.env("C_INCLUDE_PATH", "/usr/include:/usr/local/include")
#        c.env("CFLAGS", "{{ CFLAGS }} -L/usr/lib -L/usr/local/lib/gcc13")
#        # fix a weird linking bug where these system files were hardcoded
#        c.run("cp -rf /usr/lib/crt1.o .")
#        c.run("cp -rf /usr/lib/crti.o .")
#        c.run("cp -rf /usr/lib/crtbegin.o .")
#        c.run("cp -rf /usr/lib/crtend.o .")
#        c.run("cp -rf /usr/lib/crtn.o .")
#        # nuke the minigzip64 test; the bug was fixed in 1.2.13 but this was easier
#        c.run("cp /dev/null test/minigzip64.c")
    c.run("{{configure}} {{ configure_cross }} --static --prefix={{install}}")

    c.run(""" {{ make }} """)
    c.run("{{ make }} install")


@task(platforms="web", pythons="3")
def build_web(c: Context):
    c.run("embuilder build zlib")
