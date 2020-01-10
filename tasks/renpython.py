from renpybuild.model import task


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True, platforms="linux")
def build_linux(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ runtime }}/librenpython{{ c.python }}.c """)

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -Wl,-Bsymbolic

    -o librenpython{{ c.python }}.so
    librenpython{{ c.python }}.o

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
    -o python{{ c.python }}
    {{ runtime }}/renpython{{ c.python }}_posix.c


    librenpython{{ c.python }}.so
    -Wl,-rpath -Wl,$ORIGIN
    """)

    c.run("""install -d {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython{{ c.python }}.so python{{c.python}} {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")


@task(kind="python", always=True, platforms="mac")
def build_mac(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ runtime }}/librenpython{{ c.python }}.c """)

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython{{ c.python }}.dylib
    librenpython{{ c.python }}.o

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
    -o python{{ c.python }}
    {{ runtime }}/renpython{{ c.python }}_posix.c


    librenpython{{ c.python }}.dylib
    -Wl,-rpath -Wl,@executable_path
    """)

    c.run("""install -d {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython{{ c.python }}.dylib python{{c.python}} {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")


@task(kind="python", always=True, platforms="windows")
def build_windows(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ runtime }}/librenpython{{ c.python }}.c """)

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython{{ c.python }}.dll
    librenpython{{ c.python }}.o
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
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o python{{ c.python }}.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    librenpython{{ c.python }}.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -o pythonw{{ c.python }}.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    librenpython{{ c.python }}.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -DPLATFORM=\\"{{ c.platform }}\\"
    -DARCH=\\"{{ c.arch }}\\"
    -o renpy{{ c.python }}-{{ c.arch }}.exe
    {{ runtime }}/launcher{{ c.python }}_win.c
    """)

    c.run("""install -d {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython{{ c.python }}.dll python{{c.python}}.exe pythonw{{c.python}}.exe {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install {{install}}/bin/lib{{ pythonver }}.dll  {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install renpy{{ c.python }}-{{ c.arch }}.exe {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install renpy{{ c.python }}-{{ c.arch }}.exe {{dist}}""")

    if c.arch == "i686":
        c.copy("/usr/lib/gcc/i686-w64-mingw32/9.2-win32/libgcc_s_sjlj-1.dll", "{{dist}}/lib/{{ c.platform }}-{{ c.arch }}/libgcc_s_sjlj-1.dll")
        c.copy("/usr/i686-w64-mingw32/lib/libwinpthread-1.dll", "{{dist}}/lib/{{ c.platform }}-{{ c.arch }}/libwinpthread-1.dll")

        if c.python == "2":
            c.run("""install renpy{{ c.python }}-{{ c.arch }}.exe {{dist}}/renpy.exe""")

