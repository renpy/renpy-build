from renpybuild.context import Context
from renpybuild.task import task

version = "3.14.3"


@task(kind="host", pythons="3", platforms="all")
def unpack_hostpython(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/Python-{{version}}.tar.xz")


@task(kind="host", pythons="3", platforms="all")
def patch_hostpython(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.copy(
        "{{ source }}/Python-{{ version }}-Setup.local",
        "Modules/Setup.local",
    )

    c.patch("Python-{{ version }}/static-hacl.diff")

    c.run(""" autoreconf -vfi """)


@task(kind="host", pythons="3", platforms="all")
def build_host(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.env("MODULE_BUILDTYPE", "static")
    c.env("LIBHACL_LDEPS_LIBTYPE", "STATIC")

    c.run("""{{configure}} --prefix="{{ host }}" --disable-test-modules""")

    c.run("""{{ make }} install""")

    c.rmtree("{{ host }}/lib/python3.14/config-3.14-x86_64-linux-gnu/Tools/")
    c.run("install -d {{ host }}/lib/python3.14/config-3.14-x86_64-linux-gnu/Tools/")
    c.run("cp -a Tools/scripts {{ host }}/lib/python3.14/config-3.14-x86_64-linux-gnu/Tools/scripts")
