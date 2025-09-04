from renpybuild.context import Context
from renpybuild.task import task
import re

version = "1.6.1"


@task(kind="host-python")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/pyjnius-{{version}}.tar.gz")

@task(kind="host-python")
def patch(c: Context):
    c.var("version", version)
    c.chdir("pyjnius-{{version}}/")

    c.patch("pyjnius-{{version}}/py3-division.diff")
    c.patch("pyjnius-{{version}}/no-win-jdk-home.diff")

@task(kind="host-python")
def build(c: Context):

    c.var("version", version)
    c.chdir("pyjnius-{{version}}/jnius")

    with open(c.path("config.pxi"), "w") as f:
        f.write(c.expand("""\
# cython: language_level={{ c.python }}

DEF JNIUS_PLATFORM = 'android'

DEF JNIUS_CYTHON_3 = True
"""))

# on android, rely on SDL to get the JNI env
    with open(c.path("jnius_jvm_android.pxi"), "w") as f:
        f.write("""
cdef extern from "SDL2/SDL.h":
    JNIEnv *SDL_AndroidGetJNIEnv()

cdef JNIEnv *get_platform_jnienv():
    return SDL_AndroidGetJNIEnv()
""")

    c.run("""cython --3str jnius.pyx""")

    c_fn = c.path("jnius.c")

    parent_module = "jnius"
    parent_module_identifier = "jnius"

    with open(c_fn, 'r') as f:
        ccode = f.read()
    ccode = re.sub(r'Py_InitModule4\("([^"]+)"', 'Py_InitModule4("' + parent_module + '.\\1"', ccode)
    ccode = re.sub(r'^__Pyx_PyMODINIT_FUNC init', '__Pyx_PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub(r'^PyMODINIT_FUNC init', 'PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    ccode = re.sub(r'^__Pyx_PyMODINIT_FUNC PyInit_', '__Pyx_PyMODINIT_FUNC PyInit_' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub(r'^PyMODINIT_FUNC PyInit_', 'PyMODINIT_FUNC PyInit_' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    with open(c_fn, 'w') as f:
        f.write(ccode)

    c.run("""install -d {{ pytmp }}/pyjnius/jnius""")
    c.run("""install env.py  __init__.py  reflect.py  signatures.py {{ pytmp }}/pyjnius/jnius""")
    c.run("""install jnius.c {{ pytmp }}/pyjnius/""")

    with open(c.path("{{ pytmp }}/pyjnius/Setup"), "w") as f:
        f.write(c.expand("""\
jnius.jnius jnius.c
"""))


@task(kind="host-python", platforms="android", always=True)
def rapt(c: Context):
    c.var("version", version)
    c.chdir("pyjnius-{{version}}/jnius")

    c.copytree("src/org/jnius", "{{ rapt }}{{ c.python }}/prototype/renpyandroid/src/main/java/org/jnius")
