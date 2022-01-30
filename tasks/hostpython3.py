from renpybuild.model import task

version = "3.9.10"


@task(kind="host", pythons="e")
def unpack_hostpython(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")

    c.chdir("Python-{{ version }}")


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
