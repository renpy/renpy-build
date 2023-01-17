from renpybuild.context import Context
from renpybuild.task import task

version = "4.3.1"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/ffmpeg-{{version}}.tar.gz")

    c.var("version", version)
    c.chdir("ffmpeg-{{version}}")

    c.patch("ffmpeg-4.3.1-sse.diff")
    c.patch("ffmpeg-4.3.1-ff_seek_frame_binary.diff")


@task()
def build(c: Context):

    if c.arch == "i686":
        c.var("arch", "x86")
    elif c.arch == "x86_64":
        c.var("arch", "x86_64")
    elif c.arch == "aarch64":
        c.var("arch", "aarch64")
    elif c.arch == "sim-x86_64":
        c.var("arch", "x86_64")
    elif c.arch == "armv7l":
        c.var("arch", "armhf")
    elif c.arch == "arm64_v8a":
        c.var("arch", "aarch64")
    elif c.arch == "arm64":
        c.var("arch", "aarch64")
    elif c.arch == "sim-arm64":
        c.var("arch", "aarch64")
    elif c.arch == "armeabi_v7a":
        c.var("arch", "arm")
    elif c.arch == "armv7s":
        c.var("arch", "arm")
    else:
        raise Exception(f"Unknown arch: {c.arch}")

    if c.platform == "linux":
        c.var("os", "linux")
    elif (c.platform == "windows") and (c.arch == "x86_64"):
        c.var("os", "mingw64")
    elif (c.platform == "windows") and (c.arch == "i686"):
        c.var("os", "mingw32")
    elif c.platform == "mac":
        c.var("os", "darwin")
    elif c.platform == "ios":
        c.var("os", "darwin")
    elif c.platform == "android":
        c.var("os", "android")
    else:
        raise Exception(f"Unknown os: {c.platform}")

    c.var("version", version)
    c.chdir("ffmpeg-{{version}}")

    c.run("""
    ./configure
        --prefix="{{ install }}"

        --arch={{ arch }}
        --target-os={{ os }}

        --cc="{{ CC }}"
        --cxx="{{ CXX }}"
        --ld="{{ CC }}"
        --ar="{{ AR }}"
        --ranlib="{{ RANLIB }}"
        --strip="{{ STRIP }}"
        --nm="{{ NM }}"

        --extra-cflags="{{ CFLAGS }}"
        --extra-cxxflags="{{ CFLAGS }}"
        --extra-ldflags="{{ LDFLAGS }}"
        --ranlib="{{ RANLIB }}"

        --enable-pic
        --enable-static

        --disable-all
        --disable-everything

        --enable-cross-compile
        --enable-runtime-cpudetect

{% if c.platform == "windows" %}
        --disable-pthreads
        --enable-w32threads
{% endif %}

        --disable-mmx
        --disable-mmxext

        --enable-ffmpeg
        --enable-ffplay
        --disable-doc
        --enable-avcodec
        --enable-avformat
        --enable-swresample
        --enable-swscale
        --enable-avfilter
        --enable-avresample
        --enable-libaom

        --disable-bzlib

        --enable-demuxer=au
        --enable-demuxer=avi
        --enable-demuxer=flac
        --enable-demuxer=m4v
        --enable-demuxer=matroska
        --enable-demuxer=mov
        --enable-demuxer=mp3
        --enable-demuxer=mpegps
        --enable-demuxer=mpegts
        --enable-demuxer=mpegtsraw
        --enable-demuxer=mpegvideo
        --enable-demuxer=ogg
        --enable-demuxer=wav
        --enable-demuxer=av1

        --enable-decoder=flac
        --enable-decoder=mp2
        --enable-decoder=mp3
        --enable-decoder=mp3on4
        --enable-decoder=mpeg1video
        --enable-decoder=mpeg2video
        --enable-decoder=mpegvideo
        --enable-decoder=msmpeg4v1
        --enable-decoder=msmpeg4v2
        --enable-decoder=msmpeg4v3
        --enable-decoder=mpeg4
        --enable-decoder=pcm_dvd
        --enable-decoder=pcm_s16be
        --enable-decoder=pcm_s16le
        --enable-decoder=pcm_s8
        --enable-decoder=pcm_u16be
        --enable-decoder=pcm_u16le
        --enable-decoder=pcm_u8
        --enable-decoder=theora
        --enable-decoder=vorbis
        --enable-decoder=opus
        --enable-decoder=vp3
        --enable-decoder=vp8
        --enable-decoder=vp9
        --enable-decoder=libaom_av1

        --enable-parser=mpegaudio
        --enable-parser=mpegvideo
        --enable-parser=mpeg4video
        --enable-parser=vp3
        --enable-parser=vp8
        --enable-parser=vp9
        --enable-parser=av1

        --disable-iconv
        --disable-alsa
        --disable-libxcb
        --disable-lzma
        --disable-sndio
        --disable-xlib


        --disable-amf
        --disable-audiotoolbox
        --disable-cuda-llvm
        --disable-d3d11va
        --disable-dxva2
        --disable-ffnvcodec
        --disable-nvdec
        --disable-nvenc
        --disable-v4l2-m2m
        --disable-vaapi
        --disable-vdpau
        --disable-videotoolbox
    """)

    c.run("""{{ make }} V=1""")
    c.run("""make install""")


@task(platforms="web")
def build_web(c: Context):

    c.var("version", version)
    c.chdir("ffmpeg-{{version}}")

    c.run("""
    ./configure
        --prefix="{{ install }}"

        --arch=emscripten
        --target-os=none

        --cc="{{ CC }}"
        --cxx="{{ CXX }}"
        --ld="{{ CC }}"
        --ar="{{ AR }}"
        --ranlib="{{ RANLIB }}"
        --strip="{{ STRIP }}"
        --nm="{{ NM }}"

        --extra-cflags="{{ CFLAGS }}"
        --extra-cxxflags="{{ CFLAGS }}"
        --extra-ldflags="{{ LDFLAGS }}"
        --ranlib="{{ RANLIB }}"

        --enable-pic
        --enable-static
        --disable-stripping

        --disable-pthreads

        --disable-all
        --disable-everything

        --enable-cross-compile
        --enable-runtime-cpudetect

        --disable-mmx
        --disable-mmxext

        --enable-ffmpeg
        --enable-ffplay
        --disable-doc
        --enable-avcodec
        --enable-avformat
        --enable-swresample
        --enable-swscale
        --enable-avfilter
        --enable-avresample

        --disable-bzlib

        --enable-demuxer=au
        --enable-demuxer=flac
        --enable-demuxer=mp3
        --enable-demuxer=ogg
        --enable-demuxer=wav

        --enable-decoder=flac
        --enable-decoder=mp2
        --enable-decoder=mp3
        --enable-decoder=pcm_dvd
        --enable-decoder=pcm_s16be
        --enable-decoder=pcm_s16le
        --enable-decoder=pcm_s8
        --enable-decoder=pcm_u16be
        --enable-decoder=pcm_u16le
        --enable-decoder=pcm_u8
        --enable-decoder=vorbis
        --enable-decoder=opus

        --disable-iconv
        --disable-alsa
        --disable-libxcb
        --disable-lzma
        --disable-sndio
        --disable-xlib

        --disable-amf
        --disable-audiotoolbox
        --disable-cuda-llvm
        --disable-d3d11va
        --disable-dxva2
        --disable-ffnvcodec
        --disable-nvdec
        --disable-nvenc
        --disable-v4l2-m2m
        --disable-vaapi
        --disable-vdpau
        --disable-videotoolbox
    """)

    c.run("""{{ make }} V=1""")
    c.run("""make install""")
