from renpybuild.model import task


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True, platforms="linux")
def build_linux(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ csource }}/librenpython{{ c.python }}.c """)

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
    {{ csource }}/renpython{{ c.python }}_posix.c


    librenpython{{ c.python }}.so
    -Wl,-rpath -Wl,$ORIGIN
    """)

    c.run("""install -d {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython{{ c.python }}.so python{{c.python}} {{dist}}/lib/{{ c.platform }}-{{ c.arch }}""")


@task(kind="python", always=True, platforms="mac")
def build_mac(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ csource }}/librenpython{{ c.python }}.c """)

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


@task(kind="python", always=True, platforms="windows")
def build_windows(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o librenpython{{ c.python }}.o {{ csource }}/librenpython{{ c.python }}.c """)

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
