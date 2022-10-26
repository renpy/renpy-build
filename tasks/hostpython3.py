from renpybuild.model import task

version = "3.9.10"

web_version = "3.11.0rc2"


@task(kind="host", pythons="3")
def unpack_hostpython(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="host", pythons="3")
def build_host(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.run("""./configure --prefix="{{ host }}" """)
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }} install""")

    c.rmtree("{{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/")
    c.run("install -d {{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/")
    c.run("cp -a Tools/scripts {{ host }}/lib/python3.9/config-3.9-x86_64-linux-gnu/Tools/scripts")



@task(kind="host", pythons="3")
def unpack_web(c):
    c.clean()

    c.var("version", web_version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="host", pythons="3")
def build_web(c):
    c.var("version", web_version)

    c.chdir("Python-{{ version }}")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup.stdlib")

    c.run("""./configure --prefix="{{ host }}/web" """)
    c.run("""{{ make }} install""")
