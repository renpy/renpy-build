from renpybuild.model import task, annotator
import shutil

version = "2.0.10"


@annotator
def annotate(c):
    c.include("{{ install }}/include/SDL2")


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2-{{version}}.tar.gz")

    if c.platform == "ios":
        c.chdir("SDL2-{{version}}")
        c.patch("sdl2-ios-configure.diff")
        c.run("./autogen.sh")


@task()
def build(c):
    c.var("version", version)
    c.chdir("SDL2-{{version}}")

    if c.platform == "ios":
        c.env("CFLAGS", "{{ CFLAGS }} -fobjc-arc")

    c.run("""
    ./configure {{ sdl_cross_config }}
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


@task(kind="arch-python", platforms="android", always=True)
def rapt(c):
    c.var("version", version)
    c.chdir("SDL2-{{version}}")

    c.run("""{{ CXX }} -std=c++11 -shared -o libhidapi.so src/hidapi/android/hid.cpp -llog""")
    c.run("""{{ STRIP }} --strip-unneeded libhidapi.so""")

    c.run("""install -d {{ jniLibs }}""")
    c.run("""install libhidapi.so {{ jniLibs }}""")
    c.run("""install {{ cross }}/android-ndk-r21/sources/cxx-stl/llvm-libc++/libs/{{ jni_arch }}/libc++_shared.so {{ jniLibs }}""")

    c.copytree("android-project/app/src/main/java/org/libsdl", "{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl")
