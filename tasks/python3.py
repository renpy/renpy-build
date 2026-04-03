from renpybuild.context import Context
from renpybuild.task import annotator, task

version = "3.14.3"
win_version = "3.14.3"
web_version = "3.14.3"


@annotator
def annotate(c: Context):
    if c.python == "3":
        c.var("pythonver", "python3.14")
        c.var("pycver", "314")

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

    download_dir = c.expand("{{ tmp }}/downloads/cpython-mingw-{{ version }}")
    if not c.path(download_dir).exists():
        c.var("repo", "https://github.com/msys2-contrib/cpython-mingw")
        c.clone("{{ repo }}", "--branch mingw-v{{ version }}", directory=download_dir)

    c.copytree(download_dir, "cpython-mingw")


def patch_common(c: Context):
    c.copy(
        "{{ source }}/Python-{{ version }}-Setup.local",
        "Modules/Setup.local",
    )

    c.patch("Python-{{ version }}/static-hacl.diff")


@task(kind="python", pythons="3", platforms="linux,mac")
def patch_posix(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    patch_common(c)

    c.patch("Python-{{ version }}/cross-darwin.diff")

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


@task(kind="python", pythons="3", platforms="android")
def patch_android(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    patch_common(c)

    c.patch("Python-{{ version }}/3.14_armv7l_fix.patch")
    c.patch("Python-{{ version }}/3.14_fix_remote_debug.patch")

    c.run(""" autoreconf -vfi """)


@task(kind="python", pythons="3", platforms="windows")
def patch_windows(c: Context):
    c.var("version", win_version)

    c.chdir("cpython-mingw")

    patch_common(c)

    c.patch("Python-{{ version }}/single-dllmain.diff")

    c.run(""" autoreconf -vfi """)


def common(c: Context):
    c.var("version", version)
    c.env("CONFIG_SITE", "config.site")
    c.env("PYTHON_FOR_BUILD", "{{ host }}/bin/python3")
    c.env("MODULE_BUILDTYPE", "static")
    c.env("LIBHACL_LDEPS_LIBTYPE", "STATIC")

    if c.platform == "windows":
        c.chdir("cpython-mingw")
    else:
        c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")


def common_post(c: Context):
    c.run("""{{ make }}""")
    c.run("""{{ make }} install""")

    # Add things that Python does not archive into libpython.
    files: list[str] = []

    # HACL files.
    hacl_dir = c.path("{{ build }}/Python-{{ version }}/Modules/_hacl")
    files += [str(f) for f in hacl_dir.glob("*.o")]

    # Expat files.
    expat_dir = c.path("{{ build }}/Python-{{ version }}/Modules/expat")
    files += [str(f) for f in expat_dir.glob("*.o")]

    c.run("{{ AR }} rcs {{ install }}/lib/lib{{ pythonver }}.a " + " ".join(files))

    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")

    for i in ["_sysconfigdata__linux_x86_64-linux-gnu.py"]:
        c.var("i", i)

        c.copy("{{ host }}/lib/{{pythonver}}/{{ i }}", "{{ install }}/lib/{{pythonver}}/{{ i }}")


@task(kind="python", pythons="3", platforms="linux,mac")
def build_posix(c: Context):

    common(c)

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --with-build-python={{host}}/bin/python3
        --with-ensurepip=no
        --enable-ipv6
        --without-mimalloc
        --disable-test-modules
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
        --with-build-python={{host}}/bin/python3
        --with-ensurepip=no
        --enable-ipv6
        --without-mimalloc
        --disable-test-modules
        """)

    common_post(c)


@task(kind="python", pythons="3", platforms="windows")
def build_windows(c: Context):
    common(c)

    c.env("MSYSTEM", "MINGW")
    c.env("CFLAGS", "{{ CFLAGS }} ")
    c.env("LIBS", "-lws2_32 -lcrypt32")

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --with-build-python={{host}}/bin/python3
        --enable-shared
        --without-static-libpython
        --with-openssl={{ install }}
        --with-openssl-rpath=no
        --with-ensurepip=no
        --disable-ipv6
        --without-mimalloc
        --disable-test-modules
    """)

    common_post(c)


@task(kind="python", pythons="3", platforms="web")
def build_web(c: Context):
    c.var("version", web_version)

    c.clean()
    c.run("tar xaf {{source}}/Python-{{version}}.tar.xz")

    c.chdir("Python-{{ version }}")

    patch_common(c)

    c.run(""" autoreconf -vfi """)

    c.env("PYTHON_FOR_BUILD", "{{ host }}/web/bin/python3")
    c.env("CONFIG_SITE", "Tools/wasm/emscripten/config.site-wasm32-emscripten")
    c.env("CFLAGS", "{{ CFLAGS }} -DPY_CALL_TRAMPOLINE")
    c.env("CXXFLAGS", " {{ CXXFLAGS }} -DPY_CALL_TRAMPOLINE")
    c.env("PKG_CONFIG", "pkg-config")
    c.env("MODULE_BUILDTYPE", "static")
    c.env("LIBHACL_LDEPS_LIBTYPE", "STATIC")

    c.run("""
        {{configure}} {{ cross_config }}
        --prefix="{{ install }}"
        --with-build-python={{host}}/bin/python3
        --disable-shared
        --disable-ipv6
        --without-pymalloc
        --disable-test-modules
        """)

    c.run("""{{ make }}""")

    common_post(c)


@task(kind="python", pythons="3", platforms="all")
def pip(c: Context):
    c.run("{{ hostpython }} -s -m ensurepip")
    c.run("""
        {{ hostpython }} -s -m pip install --no-compile --upgrade
        --target {{ install }}/lib/{{ pythonver }}/site-packages
        legacy-cgi
        future==1.0.0
        six==1.16.0
        rsa==4.9
        pyasn1==0.6.1
        urllib3==2.6.3
        charset-normalizer==3.4.4
        certifi
        idna==3.11
        requests==2.32.5
        pefile==2022.5.30
        websockets==12.0
        setuptools==74.1.2
        pysocks==1.7.1
        """)
