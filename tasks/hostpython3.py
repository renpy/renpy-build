from renpybuild.context import Context
from renpybuild.task import task

version = "3.9.10"

web_version = "3.11.0"


@task(kind="host", pythons="3")
def unpack_hostpython(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="host", pythons="3")
def build_host(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.run("""{{configure}} --prefix="{{ host }}" """)
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make_exec }} install""")

    c.rmtree("{{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/")
    c.run("install -d {{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/")
    c.run("cp -a Tools/scripts {{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/scripts")



@task(kind="host", platforms="web", pythons="3")
def unpack_web(c: Context):
    c.clean()

    c.var("version", web_version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="host", platforms="web", pythons="3")
def build_web(c: Context):
    c.var("version", web_version)

    c.chdir("Python-{{ version }}")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup.stdlib")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup")

    c.run("""{{configure}} --prefix="{{ host }}/web" """)
    c.run("""{{ make_exec }} install""")
