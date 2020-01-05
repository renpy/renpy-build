from renpybuild.model import task, annotator

version = "2.7.17"


@annotator
def annotate(c):
    if c.python == "2":
        c.var("pythonver", "python2.7")
    else:
        c.var("pythonver", "python3.8")

    c.include("{{ install }}/include/{{ pythonver }}")


@task(kind="python", pythons="2")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")


@task(kind="python", pythons="2", platforms="linux,mac")
def patch_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("python2-no-multiarch.diff")
    c.patch("python2-cross-darwin.diff")


@task(kind="python", pythons="2", platforms="windows")
def patch_windows(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patchdir("mingw-w64-python2")
    c.patch("python2-no-dllmain.diff")

    c.run(""" autoreconf -vfi """)


@task(kind="python", pythons="2", platforms="linux,mac")
def build_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --enable-ipv6""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }} install""")

    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="2", platforms="windows")
def build_windows(c):

    c.var("version", version)

    c.chdir("Python-{{ version }}")

    c.env("MSYSTEM", "MINGW")
    c.env("PYTHON_FOR_BUILD", "{{ host }}/bin/python2")
    c.env("LDFLAGS", "{{ LDFLAGS }} -static-libgcc")

    c.run("""./configure {{ cross_config }} --enable-shared --prefix="{{ install }}" --with-threads --with-system-ffi""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    with open(c.path("Lib/plat-generic/regen"), "w") as f:
        f.write("""\
#! /bin/sh
set -v
CCINSTALL=$($1 -print-search-dirs | head -1 | cut -d' ' -f2)
REGENHEADER=${CCINSTALL}/include/stddef.h
eval $PYTHON_FOR_BUILD ../../Tools/scripts/h2py.py -i "'(u_long)'" $REGENHEADER
""")

    c.run("""{{ make }} install DLLLIBRARY={{ pythonver }}-{{ c.arch }}.dll""")
    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="2")
def pip(c):
    c.run("{{ install }}/bin/hostpython2 -m ensurepip")
    c.run("{{ install }}/bin/hostpython2 -m pip install --upgrade pip future rsa pyasn1 future")


@task(kind="python", pythons="2", always=True)
def sitecustomize(c):
    c.run("install {{ source }}/sitecustomize.py {{ install }}/lib/{{ pythonver }}/sitecustomize.py")
    c.run("{{ install }}/bin/hostpython2 -m compileall {{ install }}/lib/{{ pythonver }}/sitecustomize.py")
