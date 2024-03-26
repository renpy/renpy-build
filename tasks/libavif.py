from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c : Context):
    c.clean("{{ tmp }}/source/libavif")
    c.chdir("{{ tmp }}/source")

    c.run("git clone --branch v0.11.1 https://github.com/AOMediaCodec/libavif")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.run("""
        {{ cmake }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DAVIF_CODEC_AOM=1
        -DAVIF_CODEC_AOM_ENCODE=0
        -DBUILD_SHARED_LIBS=0
        {{ tmp }}/source/libavif
        """)

    try:
        c.run("{{ make }}")
    except:
        c.run("{{ make }} VERBOSE=1")

    c.run("{{ make_exec }} install")
