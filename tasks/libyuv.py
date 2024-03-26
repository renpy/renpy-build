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

    if c.platform == "freebsd":
        c.env("CC", "ccache gcc13 {{ CFLAGS }}")
        c.env("CXX", "ccache g++13 {{ CXXFLAGS }}")
        c.env("CPP", "ccache cpp13 {{ CPPFLAGS }}")
        c.env("C_INCLUDE_PATH", "/usr/include:/usr/local/include")
        c.env("CFLAGS", "{{ CFLAGS }} -L/usr/lib -L/usr/local/lib/gcc13")
        # fix a weird linking bug where these system files were hardcoded
        c.run("cp -rf /usr/lib/crt1.o .")
        c.run("cp -rf /usr/lib/crti.o .")
        c.run("cp -rf /usr/lib/crtbegin.o .")
        c.run("cp -rf /usr/lib/crtend.o .")
        c.run("cp -rf /usr/lib/crtn.o .")

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

    c.run("{{ make }} install")
