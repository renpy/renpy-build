from renpybuild.model import task

version = "1.2.1"


@task(kind="python-only", always=True)
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/pyjnius-{{version}}.tar.gz")


@task(kind="python-only", always=True)
def build(c):

    c.var("version", version)
    c.chdir("pyjnius-{{version}}/jnius")

    with open(c.path("config.pxi"), "w") as f:
        f.write(c.expand("""\
DEF JNIUS_PLATFORM = 'android'

# cython: language_level={{ c.python }}

DEF JNIUS_PYTHON3 = {{ c.python == '3' }}
"""))

    c.run("""cython jnius.pyx""")
    c.run("""install -d {{ pytmp }}/pyjnius/jnius""")
    c.run("""install env.py  __init__.py  reflect.py  signatures.py {{ pytmp }}/pyjnius/jnius""")
    c.run("""install jnius.c {{ pytmp }}/pyjnius/""")

    with open(c.path("{{ pytmp }}/pyjnius/Setup"), "w") as f:
        f.write(c.expand("""\
jnius.jnius jnius.c
"""))

