from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c : Context):

    if c.path.exists("{{ tmp }}/source/aom"):
        c.chdir("{{ tmp }}/source/aom")
        c.run("git pull")
        return

    c.clean("{{ tmp }}/source/aom")
    c.chdir("{{ tmp }}/source")

    c.run("git clone --branch v3.5.0 https://aomedia.googlesource.com/aom")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.run("""
        {{ cmake }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DCONFIG_AV1_ENCODER=0
        -DCONFIG_LIBYUV=0
        -DENABLE_EXAMPLES=0
        -DENABLE_TOOLS=0
        -DENABLE_TESTS=0
        -DCONFIG_PIC=1
        {% if platform == "android" or platform == "ios" %}
        -DCONFIG_RUNTIME_CPU_DETECT=0
        {% endif %}
        {{ tmp }}/source/aom
        """)

    try:
        c.run("{{ make }}")
    except:
        c.run("make VERBOSE=1")

    c.run("make install")
