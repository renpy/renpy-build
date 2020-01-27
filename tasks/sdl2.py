from renpybuild.model import task, annotator

version = "2.0.10"


@annotator
def annotate(c):
    c.include("{{ install }}/include/SDL2")


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("SDL2-{{version}}")

    c.run("""
    ./configure {{ cross_config }}
    --disable-shared
    --prefix="{{ install }}"

    --disable-dependency-tracking
    --disable-wasapi
    --disable-render-metal

{% if c.platform == "android" %}
    --disable-video-wayland
    --disable-video-x11

    --disable-oss
    --disable-alsa
    --disable-jack
    --disable-esd
    --disable-pulseaudio
    --disable-arts
    --disable-nas
    --disable-sndio
    --disable-fusionsound
{% endif %}

    """)

    c.run("""{{ make }}""")
    c.run("""make install""")
