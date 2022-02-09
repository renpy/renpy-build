from renpybuild.model import task, annotator

version = "3.9.10"
win_version = "3.9.10"

@annotator
def annotate(c):
    if c.python == "3":
        c.var("pythonver", "python3.9")
        c.var("pycver", "39")
        c.include("{{ install }}/include/{{ pythonver }}")


@task(kind="python", pythons="3", platforms="linux,mac,android,ios")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")

@task(kind="python", pythons="3", platforms="windows")
def unpack_windows(c):
    c.clean()
    c.var("version", win_version)

    if (c.root / "unpacked" / "cpython-mingw").exists():
        c.run("git clone {{ c.root }}/unpacked/cpython-mingw")
    else:
        c.run("git clone https://github.com/msys2-contrib/cpython-mingw")

    c.chdir("cpython-mingw")
    c.run("git checkout mingw-v{{ version }}")

@task(kind="python", pythons="3", platforms="linux,mac,ios")
def patch_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("python3/no-multiarch.diff")
    c.patch("python3/cross-darwin.diff")
    c.patch("python3/fix-ssl-dont-use-enum_certificates.diff")

    c.run(""" autoreconf -vfi """)

# @task(kind="python", pythons="2", platforms="ios")
# def patch_ios(c):
#     c.var("version", version)

#     c.chdir("Python-{{ version }}")
#     c.patch("ios-python2/posixmodule.patch")

#     c.run("cp {{patches}}/ios-python2/_scproxy.pyx Modules")
#     c.chdir("Modules")
#     c.run("cython _scproxy.pyx")

@task(kind="python", pythons="3", platforms="windows")
def patch_windows(c):
    c.var("version", win_version)

    c.chdir("cpython-mingw")
    c.patch("python3/no-multiarch.diff")
    c.patch("python3/allow-old-mingw.diff")
    c.patch("python3/single-dllmain.diff")
    c.patch("python3/fix-overlapped-conflict.diff")

    c.run(""" autoreconf -vfi """)


# @task(kind="python", pythons="2", platforms="android")
# def patch_android(c):
#     c.var("version", version)

#     c.chdir("Python-{{ version }}")
#     c.patchdir("android-python2")
#     c.patch("mingw-w64-python2/0001-fix-_nt_quote_args-using-subprocess-list2cmdline.patch")
#     c.patch("python2-utf8.diff")
#     c.patch("mingw-w64-python2/0855-mingw-fix-ssl-dont-use-enum_certificates.patch")

#     c.run(""" autoreconf -vfi """)



def common(c):
    c.var("version", version)

    if c.platform == "windows":
        c.chdir("cpython-mingw")
    else:
        c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

    c.env("CONFIG_SITE", "config.site")
    c.env("PYTHON_FOR_BUILD", "{{ host }}/bin/python3")


@task(kind="python", pythons="3", platforms="linux,mac")
def build_posix(c):

    common(c)

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --enable-ipv6""")
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")
    c.run("""{{ make }}""")
    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")


@task(kind="python", pythons="3", platforms="ios")
def build_ios(c):
    common(c)

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_little_endian_double=yes\n")
        f.write("ac_cv_header_langinfo_h=no\n")
        f.write("ac_cv_func_getentropy=no\n")
        f.write("ac_cv_have_long_long_format=yes\n")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --disable-toolbox-glue --enable-ipv6""")
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")
    c.run("""{{ make }} """)
    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python2", "{{ install }}/bin/hostpython2")


@task(kind="python", pythons="3", platforms="android")
def build_android(c):
    common(c)

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_little_endian_double=yes\n")
        f.write("ac_cv_header_langinfo_h=no\n")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --enable-ipv6""")
    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")
    c.run("""{{ make }}""")
    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")


@task(kind="python", pythons="3", platforms="windows")
def build_windows(c):
    common(c)

    c.env("MSYSTEM", "MINGW")
    c.env("LDFLAGS", "{{ LDFLAGS }} -static-libgcc")
    c.env("CFLAGS", "{{ CFLAGS }} ")

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_func_mktime=yes")

    # Force a recompile.
    with open(c.path("Modules/timemodule.c"), "a") as f:
        f.write("/* MKTIME FIX */\n")

    c.run("""./configure {{ cross_config }} --enable-shared --prefix="{{ install }}" --with-threads --with-system-ffi""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }}""")
    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")


@task(kind="python", pythons="3", always=True)
def pip(c):
    c.run("{{ install }}/bin/hostpython3 -s -m ensurepip")
    c.run("{{ install }}/bin/hostpython3 -s -m pip install --upgrade future==0.18.2 six==1.12.0 rsa==3.4.2 pyasn1==0.4.2 ecdsa==0.17.0")
    c.run("{{ install }}/bin/hostpython3 -s -m pip install --upgrade urllib3==1.22 certifi idna==2.6 requests==2.20.0")
