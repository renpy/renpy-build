from renpybuild.context import Context
from renpybuild.task import task


@task(kind="host", platforms="all")
def download(c: Context):
    c.var("commit", "d23308a2a7442be8e559b1b471862fd7588d6a57")

    if c.path("{{ tmp }}/source/libyuv").exists():
        c.chdir("{{ tmp }}/source/libyuv")
        c.run("git reset --hard")
        c.run("git checkout main")
        c.run("git pull")
        c.run("git checkout {{ commit }}")

    else:
        c.clean("{{ tmp }}/source/libyuv")
        c.chdir("{{ tmp }}/source")

        c.clone("https://chromium.googlesource.com/libyuv/libyuv", minimal=False)
        c.chdir("{{ tmp }}/source/libyuv")
        c.run("git checkout {{ commit }}")

    c.patch("libyuv-noshared.diff")


@task(platforms="all")
def build(c: Context):
    c.clean()

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=0
        {% if platform == "linux" and arch == "aarch64" %}
        -DCMAKE_CXX_FLAGS=-DLIBYUV_DISABLE_SME
        {% endif %}
        {% if platform == "web" %}
        -DCMAKE_SIZEOF_VOID_P=4
        {% endif %}
        {{ tmp }}/source/libyuv
        """)

    try:
        c.run("cmake --build .")
    except Exception:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")
