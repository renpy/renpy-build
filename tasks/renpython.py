from renpybuild.model import task


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True, platforms="linux")
def build_posix(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o renpython.o {{ source }}/renpython.c """)

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -o renpython{{ c.python }}
    renpython.o
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

    c.run("""install renpython{{ c.python }} {{ install }}/bin/renpython{{ c.python }}""")


@task(kind="python", always=True, platforms="windows")
def build_windows(c):

    c.run("""{{ CC }} {{ CFLAGS }} -c -o renpython.o {{ source }}/renpython.c """)

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -o renpython{{ c.python }}
    renpython.o
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

    -ldinput8 -ldxguid -ldxerr8 -luser32 -lgdi32 -lwinmm -limm32 -lole32 -loleaut32 -lshell32 -lsetupapi -lversion -luuid

    """)

    c.run("""install renpython{{ c.python }}.exe {{ install }}/bin/renpython{{ c.python }}.exe""")
