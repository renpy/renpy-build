from renpybuild.context import Context
from renpybuild.task import task

version = "3.12.8"


@task(kind="host", platforms="all")
def unpack_hostpython(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/Python-{{version}}.tar.xz")


@task(kind="host", platforms="all")
def build_host(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.run("""{{configure}} --prefix="{{ host }}" """)
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup.stdlib")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup")

    c.run("""{{ make }} install""")

    c.rmtree("{{ host }}/lib/python3.12/config-3.12-x86_64-linux-gnu/Tools/")
    c.run("install -d {{ host }}/lib/python3.12/config-3.12-x86_64-linux-gnu/Tools/")
    c.run("cp -a Tools/scripts {{ host }}/lib/python3.12/config-3.12-x86_64-linux-gnu/Tools/scripts")
