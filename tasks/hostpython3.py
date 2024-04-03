from renpybuild.context import Context
from renpybuild.task import task
import sys
import os

version = "3.9.10"
web_version = "3.11.0"

# new Python version used by FreeBSD to not conflict with system default
fbd_version = "3.10.13"


@task(kind="host", pythons="3")
def unpack_hostpython(c: Context):
    c.clean()

    if sys.platform.startswith('freebsd'):
        c.var("version", fbd_version)
    else:
        c.var("version", version)

    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="host", pythons="3")
def build_host(c: Context):
    if sys.platform.startswith('freebsd'):
        c.var("version", fbd_version)
        c.var("pyver", "3.10")
    else:
        c.var("version", version)
        c.var("pyver", "3.9")

    c.chdir("Python-{{ version }}")
    
    c.run("""{{configure}} --prefix="{{ host }}" """)
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    # nuke nismodule.c to prevent build failure; this is deprecated and not needed for this build
    c.run("cp /dev/null Modules/nismodule.c")

    # create the install folder to solve build error
    c.run("mkdir -p {{ host }}/lib/python{{ pyver }}")

    c.run("""{{ make_exec }} install""")

    if sys.platform.startswith('freebsd'):
        c.var("ending", "freebsd14.0")
    else:
        c.var("ending", "linux-gnu")

    c.rmtree("{{ host }}/lib/python{{ pyver }}/config-{{ pyver }}-x86_64-{{ ending }}/Tools/")
    c.run("install -d {{ host }}/lib/python{{ pyver }}/config-{{ pyver }}-x86_64-{{ ending }}/Tools/")
    c.run("cp -a Tools/scripts {{ host }}/lib/python{{ pyver }}/config-{{ pyver }}-x86_64-{{ ending }}/Tools/scripts")


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
