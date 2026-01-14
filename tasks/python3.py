from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "3.12.8"
win_version = "3.12.7"
web_version = "3.12.8"

@annotator
def annotate(c: Context):
    if c.python == "3":

        c.var("pythonver", "python3.12")
        c.var("pycver", "312")

        c.include("{{ install }}/include/{{ pythonver }}")


@task(kind="python", pythons="3", platforms="linux,mac,android,ios")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/Python-{{version}}.tar.xz")


@task(kind="python", pythons="3", platforms="windows")
def unpack_windows(c: Context):
    c.clean()
    c.var("version", win_version)

    if (c.root / "unpacked" / "cpython-mingw").exists():
        c.run("git clone {{ c.root }}/unpacked/cpython-mingw")
    else:
        c.run("git clone https://github.com/msys2-contrib/cpython-mingw")

    c.chdir("cpython-mingw")
    c.run("git checkout mingw-v{{ version }}")

@task(kind="python", pythons="3", platforms="linux,mac,ios")
def patch_posix(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("Python-{{ version }}/cross-darwin.diff")

    # Needs to be here because we use the Linux version of ssl.py on windows,
    # during a full build, not the patched Windows version.
    c.patch("Python-{{ version }}/fix-ssl-dont-use-enum_certificates.diff")

    c.run(""" autoreconf -vfi """)


@task(kind="python", pythons="3", platforms="ios")
def patch_ios(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("Python-{{ version }}/ios-posixmodule.diff")

    c.run("cp {{patches}}/_scproxy.pyx Modules")
    c.chdir("Modules")
    c.run("rm -f _scproxy.c")
    c.run("cython _scproxy.pyx")


@task(kind="python", pythons="3", platforms="windows")
def patch_windows(c: Context):
    c.var("version", win_version)

    c.chdir("cpython-mingw")
    c.patch("Python-{{ version }}/single-dllmain.diff")
    c.patch("Python-{{ version }}/no-af-hyperv.diff")

    c.run(""" autoreconf -vfi """)


def common(c: Context):
    if c.platform == "web":
        c.var("version", web_version)
        c.env("CONFIG_SITE", "Tools/wasm/config.site-wasm32-emscripten")
        c.env("PYTHON_FOR_BUILD", "{{ host }}/web/bin/python3")
    else:
        c.var("version", version)
        c.env("CONFIG_SITE", "config.site")
        c.env("PYTHON_FOR_BUILD", "{{ host }}/bin/python3")

    if c.platform == "windows":
        c.chdir("cpython-mingw")
    else:
        c.chdir("Python-{{ version }}")

    if c.platform != "web":

        with open(c.path("config.site"), "w") as f:
            f.write("ac_cv_file__dev_ptmx=no\n")
            f.write("ac_cv_file__dev_ptc=no\n")


def common_post(c: Context):
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup.stdlib")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup")

    c.run("""{{ make }}""")

    c.run("""{{ make }} install""")

    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")

    for i in [ "_sysconfigdata__linux_x86_64-linux-gnu.py" ]:
        c.var("i", i)

        c.copy(
            "{{ host }}/lib/{{pythonver}}/{{ i }}",
            "{{ install }}/lib/{{pythonver}}/{{ i }}")


@task(kind="python", pythons="3", platforms="linux,mac")
def build_posix(c: Context):

    common(c)

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --enable-ipv6
        --with-build-python={{host}}/bin/python3
        --with-ensurepip=no
        """)

    common_post(c)


@task(kind="python", pythons="3", platforms="ios")
def build_ios(c: Context):
    common(c)

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_little_endian_double=yes\n")
        # f.write("ac_cv_header_langinfo_h=no\n")
        f.write("ac_cv_func_getentropy=no\n")
        f.write("ac_cv_have_long_long_format=yes\n")
        f.write("ac_cv_func_clock_settime=no")

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --disable-toolbox-glue
        --enable-ipv6
        --with-build-python={{host}}/bin/python3
        --with-ensurepip=no
    """)

    common_post(c)


@task(kind="python", pythons="3", platforms="android")
def build_android(c: Context):
    common(c)

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_little_endian_double=yes\n")
        f.write("ac_cv_header_langinfo_h=no\n")

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --enable-ipv6
        --with-build-python={{host}}/bin/python3
        --with-ensurepip=no
        """)

    common_post(c)


@task(kind="python", pythons="3", platforms="windows")
def build_windows(c: Context):
    common(c)

    c.env("MSYSTEM", "MINGW")
    c.env("CFLAGS", "{{ CFLAGS }} ")

    with open(c.path("config.site"), "a") as f:
        f.write("ac_cv_func_mktime=yes")

    # Force a recompile.
    with open(c.path("Modules/timemodule.c"), "a") as f:
        f.write("/* MKTIME FIX */\n")

    c.env("CFLAGS", "{{ CFLAGS }} -Wno-implicit-function-declaration")

    c.run("""
          {{configure}} {{ cross_config }}
          --enable-shared
          --prefix="{{ install }}"
          --with-build-python={{host}}/bin/python3
          --with-ensurepip=no
    """)

    common_post(c)

@task(kind="python", pythons="3", platforms="web")
def build_web(c: Context):

    c.var("version", web_version)

    c.clean()
    c.run("tar xaf {{source}}/Python-{{version}}.tar.xz")

    common(c)

    c.env("CONFIG_SITE", "Tools/wasm/config.site-wasm32-emscripten")

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --with-emscripten-target=browser
        --with-build-python={{host}}/bin/python3
        """)

    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup.stdlib")
    c.generate("{{ source }}/Python-{{ version }}-Setup.stdlib", "Modules/Setup")

    c.run("""{{ make }}""")

    c.run("""python3 {{ root }}/tools/opfunc/opfunc_transform.py Python/ceval.c""")

    c.run("""{{ make }}""")
    c.run("""{{ make }} install""")
    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")

    for i in [ "ssl.py", "_sysconfigdata__linux_x86_64-linux-gnu.py" ]:
        c.var("i", i)

        c.copy(
            "{{ host }}/lib/{{pythonver}}/{{ i }}",
            "{{ install }}/lib/{{pythonver}}/{{ i }}")

@task(kind="python", pythons="3", platforms="all")
def pip(c: Context):
    c.run("{{ install }}/bin/hostpython3 -s -m ensurepip")
    c.run("""{{ install }}/bin/hostpython3 -s -m pip install --no-compile --upgrade
        future==1.0.0
        six==1.16.0
        rsa==4.9
        pyasn1==0.6.1
        urllib3==2.2.2
        charset-normalizer==3.3.2
        chardet==5.2.0
        certifi
        idna==3.8
        requests==2.32.3
        pefile==2022.5.30
        websockets==12.0
        setuptools==74.1.2
        pysocks==1.7.1
        """)
