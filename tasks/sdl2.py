from renpybuild.model import task, annotator
import shutil

version = "2.0.12"


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

    c.env("ac_cv_header_libunwind_h", "no")

    c.run("""
    ./configure {{ sdl_cross_config }}
    --disable-shared
    --prefix="{{ install }}"

    --disable-wasapi
    --disable-render-metal
    --disable-jack

{% if c.platform in [ "linux", "windows", "mac" ] %}
    --enable-hidapi
{% endif %}

{% if c.platform == "android" %}
    --disable-video-wayland
    --disable-video-x11

    --disable-oss
    --disable-alsa
    --disable-esd
    --disable-pulseaudio
    --disable-arts
    --disable-nas
    --disable-sndio
    --disable-fusionsound
{% endif %}

    """)

    if c.platform == "ios":
        with open(c.path("include/SDL_config.h"), "a") as f:
            f.write("""
/* Enable system power support */
#define SDL_POWER_UIKIT 1

/* enable iPhone keyboard support */
#define SDL_IPHONE_KEYBOARD 1

/* enable iOS extended launch screen */
#define SDL_IPHONE_LAUNCHSCREEN 1

/* Set max recognized G-force from accelerometer
   See src/joystick/uikit/SDL_sysjoystick.m for notes on why this is needed
 */
#define SDL_IPHONE_MAX_GFORCE 5.0

/* enable filesystem support */
#define SDL_FILESYSTEM_COCOA   1
""")

    c.run("""{{ make }}""")
    c.run("""make install""")


@task(kind="arch-python", platforms="android")
def rapt(c):
    c.var("version", version)
    c.chdir("SDL2-{{version}}")

    c.run("""{{ CXX }} -std=c++11 -shared -o libhidapi.so src/hidapi/android/hid.cpp -llog""")
    c.run("""{{ STRIP }} --strip-unneeded libhidapi.so""")

    c.run("""install -d {{ jniLibs }}""")
    c.run("""install libhidapi.so {{ jniLibs }}""")
    c.run("""install {{ cross }}/android-ndk-r21d/sources/cxx-stl/llvm-libc++/libs/{{ jni_arch }}/libc++_shared.so {{ jniLibs }}""")

    c.copytree("android-project/app/src/main/java/org/libsdl", "{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl")
