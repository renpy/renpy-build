from renpybuild.context import Context
from renpybuild.task import task

version = "0.6.2"


@task(kind="arch")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/zsync-{{version}}.tar.bz2")

    c.run("""cp /usr/share/misc/config.sub zsync-{{version}}/autotools""")


@task(kind="arch", platforms="linux")
def build_linux(c: Context):

    c.var("version", version)
    c.chdir("zsync-{{ version }}")

    c.patch("zsync-no-isastty.diff", p=1)
    c.patch("zsync-compress-5.diff", p=0)
    c.patch("zsync-includes-strings-h.diff")
    c.patch("zsync-clang22-types.diff")

    c.run("""{{configure}} {{ cross_config }} --prefix="{{ install }}" """)
    c.run("""{{ make }}""")

    c.run("install -d {{ dlpa }}")
    c.run("install zsync zsyncmake {{ dlpa }}")


@task(kind="arch", platforms="mac")
def build_mac(c: Context):

    c.var("version", version)
    c.chdir("zsync-{{ version }}")

    c.patch("zsync-no-isastty.diff", p=1)
    c.patch("zsync-compress-5.diff", p=0)
    c.patch("zsync-includes-strings-h.diff")
    c.patch("zsync-clang22-types.diff")

    c.run("""{{configure}} {{ cross_config }} --prefix="{{ install }}" """)
    c.run("""{{ make }}""")

    c.run("""install -d {{ install }}/mac""")
    c.run("""install zsync zsyncmake {{ install }}/mac""")


@task(kind="platform", platforms="mac")
def lipo_mac(c: Context):

    c.var("ac", "{{ renpy }}/renpy.app/Contents")
    c.var("acm", "{{ renpy }}/renpy.app/Contents/MacOS")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install -d {{ acm }}""")

    def lipo(fn):
        c.var("fn", fn)
        c.run("""
            {{ lipo }} -create
            -output {{ dlpa }}/{{ fn }}
            {{tmp}}/install.mac-x86_64/mac/{{fn}}
            {{tmp}}/install.mac-arm64/mac/{{fn}}
            """)

        c.run("install {{ dlpa }}/{{ fn }} {{ acm }}/{{ fn }}")

    lipo("zsync")
    lipo("zsyncmake")


@task(kind="arch", platforms="windows")
def install(c: Context):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/zsync.exe {{ prebuilt}}/zsyncmake.exe {{ dlpa }}")
