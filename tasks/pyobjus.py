from renpybuild.context import Context
from renpybuild.task import task, annotator
import re

version = "1.1.0"


@annotator
def annotate(c: Context):
    c.env("CFLAGS", "{{ CFLAGS }} -DOBJC_OLD_DISPATCH_PROTOTYPES=1")


@task(kind="python", platforms="mac,ios")
def unpack(c: Context):
    c.clean()

    # c.var("version", version)
    # c.run("tar xzf {{source}}/pyobjus-{{version}}.tar.gz")
    c.run("git clone https://github.com/kivy/pyobjus pyobjus")
    c.chdir("pyobjus")

    c.run("git checkout 573bd69b857ca4a64c7154a27f0bff6850851797")
    c.patch("pyobjus/ffi-h.diff")


@task(kind="host-python")
def host_unpack(c: Context):
    c.clean()

    c.run("git clone https://github.com/kivy/pyobjus pyobjus")
    c.chdir("pyobjus")

    c.run("git checkout 573bd69b857ca4a64c7154a27f0bff6850851797")
    c.patch("pyobjus/ffi-h.diff")


@task(kind="python", platforms="mac,ios")
def build(c: Context):

    c.var("version", version)
    c.chdir("pyobjus/pyobjus")

    with open(c.path("config.pxi"), "w") as f:

        f.write(c.expand("""\
DEF PLATFORM = "{{ 'ios' if c.platform == 'ios' else 'darwin' }}"
DEF ARCH = "{{ c.arch.replace('sim-', '') }}"
DEF PYOBJUS_CYTHON_3 = True
"""))

    c.run("""cython --3str pyobjus.pyx""")

    c_fn = c.path("pyobjus.c")

    parent_module = "pyobjus"
    parent_module_identifier = "pyobjus"

    with open(c_fn, 'r') as f:
        ccode = f.read()

    ccode = re.sub(r'Py_InitModule4\("([^"]+)"', 'Py_InitModule4("' + parent_module + '.\\1"', ccode)
    ccode = re.sub(r'^__Pyx_PyMODINIT_FUNC init', '__Pyx_PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub(r'^PyMODINIT_FUNC init', 'PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    ccode = re.sub(r'^__Pyx_PyMODINIT_FUNC PyInit_', '__Pyx_PyMODINIT_FUNC PyInit_' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub(r'^PyMODINIT_FUNC PyInit_', 'PyMODINIT_FUNC PyInit_' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    with open(c_fn, 'w') as f:
        f.write(ccode)

    c.run("""install -d {{ install }}/pyobjus""")

    c.run("""install pyobjus.c _runtime.h {{ install }}/pyobjus/""")

    with open(c.path("{{ install }}/pyobjus/Setup"), "w") as f:
        f.write(c.expand("""\
pyobjus.pyobjus pyobjus.c
"""))


@task(kind="host-python")
def host_build(c: Context):

    c.var("version", version)
    c.chdir("pyobjus/pyobjus")

    c.run("""install -d {{ pytmp }}/pyobjus/pyobjus""")
    c.run("""install dylib_manager.py  __init__.py  objc_py_types.py  protocols.py {{ pytmp }}/pyobjus/pyobjus""")
