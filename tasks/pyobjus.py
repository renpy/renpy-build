from renpybuild.model import task, annotator
import re

version = "1.1.0"


@annotator
def annotate(c):
    c.env("CFLAGS", "{{ CFLAGS }} -DOBJC_OLD_DISPATCH_PROTOTYPES=1")


@task(kind="python", always=True, platforms="mac,ios")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/pyobjus-{{version}}.tar.gz")


@task(kind="host-python", always=True)
def host_unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/pyobjus-{{version}}.tar.gz")


@task(kind="python", always=True, platforms="mac,ios")
def build(c):

    c.var("version", version)
    c.chdir("pyobjus-{{version}}/pyobjus")

    with open(c.path("config.pxi"), "w") as f:

        f.write(c.expand("""\
DEF PLATFORM = "{{ 'ios' if c.platform == 'ios' else 'darwin' }}"
DEF ARCH = "{{ c.arch }}"
"""))

    c.run("""cython pyobjus.pyx""")

    c_fn = c.path("pyobjus.c")

    parent_module = "pyobjus"
    parent_module_identifier = "pyobjus"

    with open(c_fn, 'r') as f:
        ccode = f.read()

    ccode = ccode.replace("ffi/ffi.h", "ffi.h")

    ccode = re.sub('Py_InitModule4\("([^"]+)"', 'Py_InitModule4("' + parent_module + '.\\1"', ccode)
    ccode = re.sub('^__Pyx_PyMODINIT_FUNC init', '__Pyx_PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub('^PyMODINIT_FUNC init', 'PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    with open(c_fn, 'w') as f:
        f.write(ccode)

    c.run("""install -d {{ install }}/pyobjus""")

    c.run("""install pyobjus.c _runtime.h {{ install }}/pyobjus/""")

    with open(c.path("{{ install }}/pyobjus/Setup"), "w") as f:
        f.write(c.expand("""\
pyobjus.pyobjus pyobjus.c
"""))


@task(kind="host-python", always=True)
def host_build(c):

    c.var("version", version)
    c.chdir("pyobjus-{{version}}/pyobjus")

    c.run("""install -d {{ pytmp }}/pyobjus/pyobjus""")
    c.run("""install dylib_manager.py  __init__.py  objc_py_types.py  protocols.py {{ pytmp }}/pyobjus/pyobjus""")
    c.run("{{ hostpython }} -OO -m compileall {{ pytmp }}/pyobjus/pyobjus")

