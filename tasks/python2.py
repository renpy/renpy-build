from renpybuild.model import task, annotator

version = "2.7.18"


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


@task(kind="python", pythons="2", platforms="linux,mac,ios")
def patch_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("python2-no-multiarch.diff")
    c.patch("python2-cross-darwin.diff")
    c.patch("mingw-w64-python2/0001-fix-_nt_quote_args-using-subprocess-list2cmdline.patch")
    c.patch("mingw-w64-python2/0855-mingw-fix-ssl-dont-use-enum_certificates.patch")
    c.patch("python2-utf8.diff")


@task(kind="python", pythons="2", platforms="ios")
def patch_ios(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("ios-python2/posixmodule.patch")

    c.run("cp {{patches}}/ios-python2/_scproxy.pyx Modules")
    c.chdir("Modules")
    c.run("cython _scproxy.pyx")


@task(kind="python", pythons="2", platforms="windows")
def patch_windows(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patchdir("mingw-w64-python2")
    c.patch("python2-no-dllmain.diff")
    c.patch("python2-utf8.diff")

    c.run(""" autoreconf -vfi """)


@task(kind="python", pythons="2", platforms="android")
def patch_android(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patchdir("android-python2")
    c.patch("mingw-w64-python2/0001-fix-_nt_quote_args-using-subprocess-list2cmdline.patch")
    c.patch("python2-utf8.diff")
    c.patch("mingw-w64-python2/0855-mingw-fix-ssl-dont-use-enum_certificates.patch")

    c.run(""" autoreconf -vfi """)


@task(kind="python", pythons="2", platforms="linux,mac")
def build_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

        if c.platform == "ios":
            f.write("ac_cv_little_endian_double=yes\n")
            f.write("ac_cv_header_langinfo_h=no\n")
            f.write("ac_cv_func_getentropy=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --enable-ipv6""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }} install""")

    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="2", platforms="ios")
def build_ios(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")
        f.write("ac_cv_little_endian_double=yes\n")
        f.write("ac_cv_header_langinfo_h=no\n")
        f.write("ac_cv_func_getentropy=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --disable-toolbox-glue --enable-ipv6""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }} install""")

    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="2", platforms="android")
def build_android(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")
        f.write("ac_cv_little_endian_double=yes\n")
        f.write("ac_cv_header_langinfo_h=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --enable-ipv6""")

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

    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="2")
def pip(c):
    c.run("{{ install }}/bin/hostpython2 -s -m ensurepip")
    c.run("{{ install }}/bin/hostpython2 -s -m pip install --upgrade future==0.18.2 six==1.12.0 rsa==3.4.2 pyasn1==0.4.2")
    c.run("{{ install }}/bin/hostpython2 -s -m pip install --upgrade urllib3==1.22 certifi idna==2.6 requests==2.20.0")

# @task(kind="python", pythons="2", always=True)
# def sitecustomize(c):
#     c.run("install {{ source }}/sitecustomize.py {{ install }}/lib/{{ pythonver }}/sitecustomize.py")
#     c.run("{{ install }}/bin/hostpython2 -m compileall {{ install }}/lib/{{ pythonver }}/sitecustomize.py")
