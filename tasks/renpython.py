from renpybuild.model import task
import os


@task(kind="python", always=True)
def clean(c):
    c.clean()


@task(kind="python", always=True)
def build(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\"
    -DARCH=\\"{{ c.arch }}\\"
    -DPYTHONVER=\\"{{ pythonver }}\\"
    -DPYCVER=\\"{{ pycver }}\\"
    -D{{ c.platform|upper }}

    -c -o librenpython.o
    {{ runtime }}/librenpython{{ c.python }}.c
    """)


@task(kind="python", always=True, platforms="android")
def build_android(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\"
    -DARCH=\\"{{ c.arch }}\\"
    -DPYTHONVER=\\"{{ pythonver }}\\"
    -DPYCVER=\\"{{ pycver }}\\"

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

    -lOpenSLES

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

    c.run("install -d {{ jni_unstripped }}")
    c.run("install librenpython.so {{ jni_unstripped }}")

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
    -v
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
    {% if c.arch == "arm64" %}
    -Wl,-framework,GameController
    -Wl,-framework,CoreHaptics
    {% endif %}
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

    # Striping breaks the code signatures on arm64 mac, so don't strip there.
    if not c.args.nostrip and not c.arch == "arm64":
        c.run("""{{ STRIP }} -S -x librenpython.dylib python renpy""")

    c.run("""install -d {{ install }}/mac{{python}}""")
    c.run("""install librenpython.dylib {{ install }}/mac{{python}}""")
    c.run("""install python {{ install }}/mac{{python}}/python""")
    c.run("""install python {{ install }}/mac{{python}}/pythonw""")
    c.run("""install renpy {{ install }}/mac{{python}}/renpy""")



@task(kind="host-python", platforms="mac", always=True)
def lipo_mac(c):

    c.var("dlpa", "{{distlib}}/py{{ python }}-{{ platform }}-universal")

    c.var("ac", "{{ renpy }}/renpy{{ python }}.app/Contents")
    c.var("acm", "{{ renpy }}/renpy{{ python }}.app/Contents/MacOS")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install -d {{ acm }}""")

    c.run("""install -d {{ ac }}/Resources""")
    c.run("""install {{ runtime }}/Info.plist {{ ac }}""")
    c.run("""install {{ runtime }}/icon.icns {{ ac }}/Resources""")

    def lipo(fn):
        c.var("fn", fn)
        c.run("""
            {{ lipo }} -create
            -output {{ dlpa }}/{{ fn }}
            {{tmp}}/install.mac-x86_64/mac{{python}}/{{fn}}
            {{tmp}}/install.mac-arm64/mac{{python}}/{{fn}}
            """)

        c.run("install {{ dlpa }}/{{ fn }} {{ acm }}/{{ fn }}")

    lipo("librenpython.dylib")
    lipo("python")
    lipo("pythonw")
    lipo("renpy")


def fix_pe(c, fn):
    """
    Sets the PE file characteristics to mark the relocations as stripped.
    """

    import sys
    print(sys.executable, sys.path)

    fn = str(c.path(fn))

    with open(c.path("fix_pe.py"), "w") as f:

        f.write("""\
import sys
print(sys.executable, sys.path)

import pefile
import sys

fn = sys.argv[1]

pe = pefile.PE(fn)
pe.FILE_HEADER.Characteristics = pe.FILE_HEADER.Characteristics | pefile.IMAGE_CHARACTERISTICS["IMAGE_FILE_RELOCS_STRIPPED"]
pe.OPTIONAL_HEADER.CheckSum = pe.generate_checksum()
pe.write(fn)
""")

    c.run("""{{ hostpython }} fix_pe.py """ + fn)

@task(kind="python", always=True, platforms="windows")
def link_windows(c):

    c.run("""
    {{ CC }} {{ LDFLAGS }}
    -shared
    -o librenpython.dll
    librenpython.o
    -lrenpy

    {{install}}/lib/libfribidi.a

    {% if c.python == "2" %}
    {{install}}/lib/{{ pythonver }}/config/lib{{ pythonver }}.dll.a
    {% else %}
    {{install}}/lib/lib{{ pythonver }}.dll.a
    {% endif %}

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
    -liphlpapi

    -ldinput8
    -ldxguid
    -ldxerr8
    -luser32
    -lgdi32
    -lwinmm
    -limm32
    -lcomdlg32
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
    -mconsole {% if c.python != '2' %}-municode {% endif %}
    -o python.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    renpy_icon.o
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows {% if c.python != '2' %}-municode {% endif %}
    -o pythonw.exe
    {{ runtime }}/renpython{{ c.python }}_win.c
    renpy_icon.o
    librenpython.dll
    """)

    c.run("""
    {{ CC }} {{ CDFLAGS }} {{ LDFLAGS }}
    -mwindows {% if c.python != '2' %}-municode {% endif %}
    -DPLATFORM=\\"{{ c.platform }}\\" -DARCH=\\"{{ c.arch }}\\"
    -o renpy.exe
    {{ runtime }}/launcher{{ c.python }}_win.c
    renpy_icon.o
    """)

    c.run("""install -m 755 {{install}}/bin/lib{{ pythonver }}.dll lib{{ pythonver }}.dll""")

    if not c.args.nostrip:
        c.run("""{{ STRIP }} --strip-unneeded lib{{ pythonver }}.dll librenpython.dll python.exe pythonw.exe renpy.exe""")

    c.run("""{{ STRIP }} -R .reloc python.exe pythonw.exe renpy.exe""")

    fix_pe(c, "python.exe")
    fix_pe(c, "pythonw.exe")
    fix_pe(c, "renpy.exe")

    c.run("""install -d {{ dlpa }}""")
    c.run("""install librenpython.dll python.exe pythonw.exe {{ dlpa }}""")
    c.run("""install lib{{ pythonver }}.dll  {{ dlpa }}""")
    c.run("""install renpy.exe {{ dlpa }}/renpy.exe""")

    if c.arch == "i686":
        for i in sorted(os.listdir("/usr/lib/gcc/i686-w64-mingw32")):
            if i.endswith("-win32"):
                c.var("mingw_version", i)

        c.copy("/usr/lib/gcc/i686-w64-mingw32/{{ mingw_version }}/libgcc_s_dw2-1.dll", "{{ dlpa }}/libgcc_s_dw2-1.dll")
        c.copy("/usr/i686-w64-mingw32/lib/libwinpthread-1.dll", "{{ dlpa }}/libwinpthread-1.dll")

        c.run("""install renpy.exe {{ renpy }}/renpy-32.exe""")

    elif c.arch == "x86_64":
        c.run("""install renpy.exe {{ renpy }}/renpy{{ python }}.exe""")

        if c.python == "2":
            c.run("""install renpy.exe {{ renpy }}/renpy.exe""")


@task(kind="python", always=True, platforms="ios")
def link_ios(c):

    c.run("""{{ AR }} -r librenpython.a librenpython.o""")
    c.run("""install -d {{install}}/lib""")
    c.run("""install librenpython.a {{ install }}/lib""")


@task(kind="python", platforms="web", pythons="3", always=True)
def build_web(c):

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\"
    -DARCH=\\"{{ c.arch }}\\"
    -DPYTHONVER=\\"{{ pythonver }}\\"
    -DPYCVER=\\"{{ pycver }}\\"
    -D{{ c.platform|upper }}

    -c -o librenpython.o
    {{ runtime }}/librenpython{{ c.python }}.c
    """)


@task(kind="python", platforms="web", pythons="3", always=True)
def link_web(c):

    c.var("debug_asyncify", True)


    c.run("""
    {{ CC }} {{ LDFLAGS }}

    {% if debug_asyncify %}
    -g2
    {% endif %}

    -o renpy.html
    librenpython.o
    {{ runtime }}/launcher{{ c.python }}_posix.c

    -l{{ pythonver }}

    -lrenpy

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

    -lbz2
    -lz
    -lm

    -lidbfs.js

    --preload-file {{ dist }}@/

    -sFULL_ES2=1
    -sMAX_WEBGL_VERSION=2
    --emit-symbol-map

    -sFILESYSTEM=1
    -sEXPORTED_RUNTIME_METHODS=['stackTrace','FS']

    -sASYNCIFY=1
    -sASYNCIFY_STACK_SIZE=65535

    -sINITIAL_MEMORY=192MB
    -sALLOW_MEMORY_GROWTH=1

    --shell-file {{ runtime }}/web/shell.html
    """)

    c.run("""install -d {{ renpy }}/web3""")
    c.run("""install renpy.html {{ renpy }}/web3/renpy.html""")
    c.run("""install renpy.html.symbols {{ renpy }}/web3/renpy.html.symbols""")
    c.run("""install {{ runtime }}/web/renpy-pre.js {{ renpy }}/web3/renpy-pre.js""")
    c.run("""install renpy.js {{ renpy }}/web3/renpy.js""")
    c.run("""install renpy.wasm {{ renpy }}/web3/renpy.wasm""")
    c.run("""install renpy.data {{ renpy }}/web3/renpy.data""")


    # -sASYNCIFY_IGNORE_INDIRECT=1
    # -sASSERTIONS=1
