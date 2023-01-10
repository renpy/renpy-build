from renpybuild.context import Context
from renpybuild.task import task

version = "0.6.2"


@task(kind="python")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/zsync-{{version}}.tar.bz2")

    c.run("""cp /usr/share/autoconf/build-aux/config.sub zsync-{{version}}/autotools""")

@task(kind="python", platforms="linux")
def build(c: Context):

    c.var("version", version)
    c.chdir("zsync-{{ version }}")

    c.patch("zsync-no-isastty.diff", p=1)
    c.patch("zsync-compress-5.diff", p=0)

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" """)
    c.run("""{{ make }}""")

    c.run("install -d {{ dlpa }}")
    c.run("install zsync zsyncmake {{ dlpa }}")


@task(kind="python", platforms="mac")
def build(c: Context):

    c.var("version", version)
    c.chdir("zsync-{{ version }}")

    c.patch("zsync-no-isastty.diff", p=1)
    c.patch("zsync-compress-5.diff", p=0)

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" """)
    c.run("""{{ make }}""")

    c.run("""install -d {{ install }}/mac{{python}}""")
    c.run("""install zsync zsyncmake {{ install }}/mac{{python}}""")


@task(kind="host-python", platforms="mac")
def lipo_mac(c: Context):

    c.var("dlpa", "{{distlib}}/py{{ python }}-{{ platform }}-universal")

    c.var("ac", "{{ renpy }}/renpy{{ python }}.app/Contents")
    c.var("acm", "{{ renpy }}/renpy{{ python }}.app/Contents/MacOS")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install -d {{ acm }}""")

    def lipo(fn):
        c.var("fn", fn)
        c.run("""
            {{ lipo }} -create
            -output {{ dlpa }}/{{ fn }}
            {{tmp}}/install.mac-x86_64/mac{{python}}/{{fn}}
            {{tmp}}/install.mac-arm64/mac{{python}}/{{fn}}
            """)

        c.run("install {{ dlpa }}/{{ fn }} {{ acm }}/{{ fn }}")

    lipo("zsync")
    lipo("zsyncmake")


@task(kind="python", platforms="windows")
def install(c: Context):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/zsync.exe {{ prebuilt}}/zsyncmake.exe {{ dlpa }}")
