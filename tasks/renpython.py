from renpybuild.model import task


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True)
def build(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\"

    -c -o librenpython.o
    {{ runtime }}/librenpython{{ c.python }}.c
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

    c.run("""install -d {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython.so {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/python""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/pythonw""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/renpy""")


@task(kind="python", always=True, platforms="mac")
def link_mac(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython.dylib
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
    -Wl,-rpath -Wl,@executable_path
    """)

    c.run("""install -d {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython.dylib {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/python""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/pythonw""")
    c.run("""install python {{distlib}}/{{ c.platform }}-{{ c.arch }}/renpy""")


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
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -o python.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -o pythonw.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows
    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\"
    -o launcher.exe
    {{ runtime }}/launcher{{ c.python }}_win.c
    """)

    c.run("""install -d {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install librenpython.dll python.exe pythonw.exe {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install {{install}}/bin/lib{{ pythonver }}.dll  {{distlib}}/{{ c.platform }}-{{ c.arch }}""")
    c.run("""install launcher.exe {{distlib}}/{{ c.platform }}-{{ c.arch }}/launcher.exe""")

    if c.arch == "i686":
        c.copy("/usr/lib/gcc/i686-w64-mingw32/9.2-win32/libgcc_s_sjlj-1.dll", "{{distlib}}/{{ c.platform }}-{{ c.arch }}/libgcc_s_sjlj-1.dll")
        c.copy("/usr/i686-w64-mingw32/lib/libwinpthread-1.dll", "{{distlib}}/{{ c.platform }}-{{ c.arch }}/libwinpthread-1.dll")

