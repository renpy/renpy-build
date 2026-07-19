from renpybuild.context import Context
from renpybuild.task import task, annotator
import re

commit = "b61d65fdc620dbe19892d2419b77340341e76084"


@annotator
def annotate(c: Context):
    c.env("CFLAGS", "{{ CFLAGS }} -DOBJC_OLD_DISPATCH_PROTOTYPES=1")
    c.env("OBJCFLAGS", "{{ OBJCFLAGS }} -DOBJC_OLD_DISPATCH_PROTOTYPES=1")


@task(kind="arch", platforms="mac,ios")
def unpack(c: Context):
    c.clean()

    c.var("commit", commit)
    c.clone("https://github.com/kivy/pyobjus", minimal=False)
    c.chdir("pyobjus")

    c.run("git checkout {{ commit }}")
    c.patch("pyobjus-ffi-h.diff")


@task(kind="host")
def host_unpack(c: Context):
    c.clean()

    c.var("commit", commit)
    c.clone("https://github.com/kivy/pyobjus", minimal=False)
    c.chdir("pyobjus")

    c.run("git checkout {{ commit }}")
    c.patch("pyobjus-ffi-h.diff")


@task(kind="arch", platforms="mac,ios")
def build(c: Context):

    c.chdir("pyobjus/pyobjus")

    with open(c.path("config.pxi"), "w") as f:
        f.write(
            c.expand("""\
DEF PLATFORM = "{{ 'ios' if c.platform == 'ios' else 'darwin' }}"
DEF ARCH = "{{ c.arch.replace('sim-', '') }}"
DEF PYOBJUS_CYTHON_3 = True
""")
        )

    c.run("""cython pyobjus.pyx""")

    c.run("""install -d {{ install }}/pyobjus""")

    c.run("""install pyobjus.c _runtime.h {{ install }}/pyobjus/""")

    with open(c.path("{{ install }}/pyobjus/Setup"), "w") as f:
        f.write("pyobjus.pyobjus pyobjus.c\n")


@task(kind="host")
def host_build(c: Context):

    c.chdir("pyobjus/pyobjus")

    c.run("""install -d {{ pytmp }}/pyobjus/pyobjus""")
    c.run("""install dylib_manager.py  __init__.py  objc_py_types.py  protocols.py {{ pytmp }}/pyobjus/pyobjus""")
