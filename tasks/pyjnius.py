from renpybuild.model import task
import re

version = "1.2.1"


@task(kind="host-python")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/pyjnius-{{version}}.tar.gz")


@task(kind="host-python")
def build(c):

    c.var("version", version)
    c.chdir("pyjnius-{{version}}/jnius")

    with open(c.path("config.pxi"), "w") as f:
        f.write(c.expand("""\
DEF JNIUS_PLATFORM = 'android'

# cython: language_level={{ c.python }}

DEF JNIUS_PYTHON3 = {{ c.python == '3' }}
"""))

# on android, rely on SDL to get the JNI env
    with open(c.path("jnius_jvm_android.pxi"), "w") as f:
        f.write("""
cdef extern from "SDL2/SDL.h":
    JNIEnv *SDL_AndroidGetJNIEnv()

cdef JNIEnv *get_platform_jnienv():
    return SDL_AndroidGetJNIEnv()
""")

    c.run("""cython jnius.pyx""")

    c_fn = c.path("jnius.c")

    parent_module = "jnius"
    parent_module_identifier = "jnius"

    with open(c_fn, 'r') as f:
        ccode = f.read()
    ccode = re.sub('Py_InitModule4\("([^"]+)"', 'Py_InitModule4("' + parent_module + '.\\1"', ccode)
    ccode = re.sub('^__Pyx_PyMODINIT_FUNC init', '__Pyx_PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.28.2
    ccode = re.sub('^PyMODINIT_FUNC init', 'PyMODINIT_FUNC init' + parent_module_identifier + '_', ccode, 0, re.MULTILINE) # Cython 0.25.2
    with open(c_fn, 'w') as f:
        f.write(ccode)

    c.run("""install -d {{ pytmp }}/pyjnius/jnius""")
    c.run("""install env.py  __init__.py  reflect.py  signatures.py {{ pytmp }}/pyjnius/jnius""")
    c.run("""install jnius.c {{ pytmp }}/pyjnius/""")

    c.run("{{ hostpython }} -OO -m compileall {{ pytmp }}/pyjnius/jnius")

    with open(c.path("{{ pytmp }}/pyjnius/Setup"), "w") as f:
        f.write(c.expand("""\
jnius.jnius jnius.c
"""))


@task(kind="host-python", platforms="android")
def rapt(c):
    c.var("version", version)
    c.chdir("pyjnius-{{version}}/jnius")

    c.copytree("src/org/jnius", "{{ rapt }}{{ c.python }}/prototype/renpyandroid/src/main/java/org/jnius")
