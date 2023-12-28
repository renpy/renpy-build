from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def download(c : Context):

    if c.path("{{ tmp }}/source/aom").exists():
        c.chdir("{{ tmp }}/source/aom")
        c.run("git checkout master")
        c.run("git pull")
        c.run("git checkout v3.5.0")
        return

    c.clean("{{ tmp }}/source/aom")
    c.chdir("{{ tmp }}/source")

    c.run("git clone https://aomedia.googlesource.com/aom")
    c.chdir("{{ tmp }}/source/aom")
    c.run("git checkout v3.5.0")

@task(platforms="all")
def build(c : Context):
    c.clean()

    c.run("""
        {{ cmake }}
        -DCMAKE_INSTALL_PREFIX={{install}}
        -DCONFIG_AV1_ENCODER=0
        -DENABLE_EXAMPLES=0
        -DENABLE_TOOLS=0
        -DENABLE_TESTS=0
        -DCONFIG_PIC=1
        {% if platform == "android" or platform == "ios" or platform == "web" %}
        -DCONFIG_RUNTIME_CPU_DETECT=0
        {% endif %}
        {% if platform == "web" %}
        -DAOM_TARGET_CPU=generic
        {% endif %}
        {{ tmp }}/source/aom
        """)

    try:
        c.run("{{ make }}")
    except:
        c.run("make VERBOSE=1")

    c.run("make install")
