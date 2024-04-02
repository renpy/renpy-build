from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c : Context):

    c.var("commit", "331c361581896292fb46c8c6905e41262b7ca95f")

    if c.path("{{ tmp }}/source/libyuv").exists():
        c.chdir("{{ tmp }}/source/libyuv")
        c.run("git reset --hard")
        c.run("git checkout main")
        c.run("git pull")
        c.run("git checkout {{ commit }}")

    else:

        c.clean("{{ tmp }}/source/libyuv")
        c.chdir("{{ tmp }}/source")

        c.run("git clone https://chromium.googlesource.com/libyuv/libyuv")
        c.chdir("{{ tmp }}/source/libyuv")
        c.run("git checkout {{ commit }}")

    c.patch("libyuv-noshared.diff")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.run("""
        {{ cmake }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DBUILD_SHARED_LIBS=0
        {% if platform == "web" %}
        -DCMAKE_SIZEOF_VOID_P=4
        {% endif %}
        {{ tmp }}/source/libyuv
        """)

    try:
        c.run("{{ make }}")
    except:
        c.run("{{ make }} VERBOSE=1")

    c.run("{{ make_exec }} install")
