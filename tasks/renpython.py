from renpybuild.model import task
import os


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True)
def build(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\" -D{{ c.platform|upper }}

    -c -o librenpython.o
    {{ runtime }}/librenpython{{ c.python }}.c
    """)


@task(kind="python", always=True, platforms="android")
def build_android(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\"

    -c -o librenpython_android.o
    {{ runtime }}/librenpython{{ c.python }}_android.c
    """)


@task(kind="python", always=True, platforms="linux")
def link_linux(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -Wl,-Bsymbolic

    -o librenpython.so
    librenpython.o

    -lrenpy
    -l{{ pythonver }}

    -lavformat
    -lavcodec
    -lswscale
    -lswresample
    -lavutil

    -lSDL2_image
    -lSDL2
    -lGL
    -ljpeg
    -lpng
    -lwebp
    -lfribidi
    -lfreetype
    -lffi
    -ldl
    -lssl
    -lcrypto
    -lbz2
    -lutil
    -lz
    -lpthread
    -lm
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o python
    {{ runtime }}/renpython{{ c.python }}_posix.c

    librenpython.so
    -Wl,-rpath -Wl,$ORIGIN
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o renpy
    {{ runtime }}/launcher{{ c.python }}_posix.c

    librenpython.so
    -Wl,-rpath -Wl,$ORIGIN
    """)

    if not c.args.nostrip:
        c.run("""{{ STRIP }} --strip-unneeded librenpython.so python renpy""")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install librenpython.so {{ dlpa }}""")
    c.run("""install python {{ dlpa }}/python""")
    c.run("""install python {{ dlpa }}/pythonw""")
    c.run("""install renpy {{ dlpa }}/renpy""")


@task(kind="python", always=True, platforms="android")
def link_android(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -Wl,-Bsymbolic
    -Wl,--no-undefined

    -o librenpython.so
    librenpython_android.o

    -lrenpy
    -l{{ pythonver }}

    -lavformat
    -lavcodec
    -lswscale
    -lswresample
    -lavutil

    -lSDL2_image
    -lSDL2

    -lGLESv1_CM
    -lGLESv2

    -ljpeg
    -lpng
    -lwebp
    -lfribidi
    -lfreetype
    -lffi
    -ldl
    -lssl
    -lcrypto
    -lbz2
    -lz
    -lm

    -llog
    -landroid
    """)

    if not c.args.nostrip:
        c.run("""{{ STRIP }} --strip-unneeded librenpython.so""")

    c.run("install -d {{ jniLibs }}")
    c.run("install librenpython.so {{ jniLibs }}")


@task(kind="python", always=True, platforms="mac")
def link_mac(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython.dylib
    -install_name @executable_path/librenpython.dylib
    librenpython.o

    -lrenpy
    -l{{ pythonver }}

    -lavformat
    -lavcodec
    -lswscale
    -lswresample
    -lavutil

    -lSDL2_image
    -lSDL2
    -ljpeg
    -lpng
    -lwebp
    -lfribidi
    -lfreetype
    -lffi
    -lssl
    -lcrypto
    -lbz2
    -lz
    -lm

    -liconv
    -Wl,-framework,CoreAudio
    -Wl,-framework,AudioToolbox
    -Wl,-framework,ForceFeedback
    -lobjc
    -Wl,-framework,CoreVideo
    -Wl,-framework,Cocoa
    -Wl,-framework,Carbon
    -Wl,-framework,IOKit
    -Wl,-framework,SystemConfiguration
    -Wl,-framework,CoreFoundation
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o python
    {{ runtime }}/renpython{{ c.python }}_posix.c

    librenpython.dylib
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o renpy
    {{ runtime }}/launcher{{ c.python }}_posix.c

    librenpython.dylib
    """)

    if not c.args.nostrip:
        c.run("""{{ STRIP }} -S -x librenpython.dylib python renpy""")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install librenpython.dylib {{ dlpa }}""")
    c.run("""install python {{ dlpa }}/python""")
    c.run("""install python {{ dlpa }}/pythonw""")
    c.run("""install renpy {{ dlpa }}/renpy""")

    # renpy.app/Contents/MacOS:
    c.var("acm", "{{ renpy }}/renpy.app/Contents/MacOS")

    c.run("""install -d {{ acm }}""")
    c.run("""install librenpython.dylib {{ acm }}""")
    c.run("""install python {{ acm }}/python""")
    c.run("""install python {{ acm }}/pythonw""")
    c.run("""install renpy {{ acm }}/renpy""")


@task(kind="python", always=True, platforms="windows")
def link_windows(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython.dll
    librenpython.o
    -lrenpy

    {{install}}/lib/libfribidi.a
    {{install}}/lib/{{ pythonver }}/config/lib{{ pythonver }}.dll.a

    -lavformat
    -lavcodec
    -lswscale
    -lswresample
    -lavutil

    -lSDL2_image
    -lSDL2
    -lopengl32
    -ljpeg
    -lpng
    -lwebp
    -lfreetype
    -lffi
    -lssl
    -lcrypto
    -lbz2
    -lbcrypt
    -lz
    -lm
    -lpthread
    -lws2_32

    -ldinput8
    -ldxguid
    -ldxerr8
    -luser32
    -lgdi32
    -lwinmm
    -limm32
    -lole32
    -loleaut32
    -lshell32
    -lsetupapi
    -lversion
    -luuid
    """)

    c.run("""
    {{ WINDRES }} {{ runtime }}/renpy_icon.rc renpy_icon.o
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o python.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    renpy_icon.o
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -o pythonw.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    renpy_icon.o
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\"
    -o renpy.exe
    {{ runtime }}/launcher{{ c.python }}_win.c
    renpy_icon.o
    """)

    c.run("""install -m 755 {{install}}/bin/lib{{ pythonver }}.dll lib{{ pythonver }}.dll""")

    if not c.args.nostrip:
        c.run("""{{ STRIP }} --strip-unneeded lib{{ pythonver }}.dll librenpython.dll python.exe pythonw.exe renpy.exe""")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install librenpython.dll python.exe pythonw.exe {{ dlpa }}""")
    c.run("""install lib{{ pythonver }}.dll  {{ dlpa }}""")
    c.run("""install renpy.exe {{ dlpa }}/renpy.exe""")

    if c.arch == "i686":
        for i in sorted(os.listdir("/usr/lib/gcc/i686-w64-mingw32")):
            if i.endswith("-win32"):
                c.var("mingw_version", i)

        c.copy("/usr/lib/gcc/i686-w64-mingw32/{{ mingw_version }}/libgcc_s_sjlj-1.dll", "{{ dlpa }}/libgcc_s_sjlj-1.dll")
        c.copy("/usr/i686-w64-mingw32/lib/libwinpthread-1.dll", "{{ dlpa }}/libwinpthread-1.dll")

        c.run("""install renpy.exe {{ renpy }}/renpy-32.exe""")

    elif c.arch == "x86_64":
        c.run("""install renpy.exe {{ renpy }}/renpy.exe""")


@task(kind="python", always=True, platforms="ios")
def link_ios(c):

    c.run("""{{ AR }} -r librenpython.a librenpython.o""")
    c.run("""install -d {{install}}/lib""")
    c.run("""install librenpython.a {{ install }}/lib""")
