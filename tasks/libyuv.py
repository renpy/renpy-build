from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c: Context):
    c.var("commit", "331c361581896292fb46c8c6905e41262b7ca95f")

    c.clean("{{ tmp }}/source/libyuv")
    c.chdir("{{ tmp }}/source")

    c.clone("https://chromium.googlesource.com/libyuv/libyuv", "--revision {{ commit }}")

    c.chdir("{{ tmp }}/source/libyuv")
    c.patch("libyuv-noshared.diff")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.run("""
        {{ cmake_configure }} {{ cmake_args }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=0
        {% if platform == "web" %}
        -DCMAKE_SIZEOF_VOID_P=4
        {% endif %}
        {{ tmp }}/source/libyuv
        """)

    try:
        c.run("cmake --build .")
    except:
        c.run("cmake --build . -j 1 -v")

    c.run("cmake --install .")
