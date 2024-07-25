from renpybuild.context import Context
from renpybuild.task import task
import os
import time

@task(kind="python", always=True)
def clean(c: Context):
    c.clean()


@task(kind="python", always=True)
def build(c: Context):

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
def build_android(c: Context):

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
def link_linux(c: Context):

    c.run("""
    {{ CXX }} {{ LDFLAGS }}
    -shared
    -static-libstdc++
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
    -lavif
    -ldav1d
    -lyuv
    -ljpeg
    -lpng
    -lwebp
    -lsharpyuv
    -lfribidi
    -lharfbuzz
    -lbrotlidec
    -lfreetype
    -lffi
    -ldl
    -lssl
    -lcrypto
    -llzma
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
def link_android(c: Context):

    c.run("""
    {{ CXX }} {{ LDFLAGS }}
    -shared
    -static-libstdc++
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

    -lavif
    -ldav1d
    -lyuv
    -ljpeg
    -lpng
    -lwebp
    -lsharpyuv
    -lharfbuzz
    -lbrotlidec
    -lfribidi
    -lfreetype
    -lffi
    -ldl
    -lssl
    -lcrypto
    -llzma
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
def link_mac(c: Context):

    c.run("""
    {{ CXX }} {{ LDFLAGS }}
    -shared
    -static-libstdc++
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
    -lavif
    -ldav1d
    -lyuv
    -ljpeg
    -lpng
    -lwebp
    -lsharpyuv
    -lharfbuzz
    -lbrotlidec
    -lfribidi
    -lfreetype
    -lffi
    -lssl
    -lcrypto
    -llzma
    -lbz2
    -lz
    -lm

    -liconv
    -Wl,-framework,CoreAudio
    -Wl,-framework,AudioToolbox
    -Wl,-framework,ForceFeedback
    -Wl,-framework,GameController
    -Wl,-framework,CoreHaptics
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
        c.run("""{{ STRIP }} -S librenpython.dylib python renpy""")

    c.run("""install -d {{ install }}/mac{{python}}""")
    c.run("""install librenpython.dylib {{ install }}/mac{{python}}""")
    c.run("""install python {{ install }}/mac{{python}}/python""")
    c.run("""install python {{ install }}/mac{{python}}/pythonw""")
    c.run("""install renpy {{ install }}/mac{{python}}/renpy""")



@task(kind="host-python", platforms="mac", always=True)
def lipo_mac(c: Context):

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


def fix_pe(c: Context, fn):
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
def link_windows(c: Context):

    c.run("""
    {{ CXX }} {{ LDFLAGS }}
    -shared
    -static-libstdc++
    -o librenpython.dll
    librenpython.o
    -lrenpy

    -lfribidi

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
    -lavif
    -ldav1d
    -lyuv
    -ljpeg
    -lpng16
    -lwebp
    -lsharpyuv
    -lharfbuzz
    -lbrotlidec
    -lfreetype
    -lffi
    -lssl
    -lcrypto
    -llzma
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

    -Wl,--export-all-symbols
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
        c.copy("{{cross}}/llvm-mingw/i686-w64-mingw32/bin/libwinpthread-1.dll", "{{ dlpa }}/libwinpthread-1.dll")
        c.copy("{{cross}}/llvm-mingw/i686-w64-mingw32/share/mingw32/COPYING.winpthreads.txt", "{{ dlpa }}/libwinpthread-1.txt")

        c.run("""install renpy.exe {{ renpy }}/renpy-32.exe""")

    elif c.arch == "x86_64":
        c.run("""install renpy.exe {{ renpy }}/renpy{{ python }}.exe""")
        c.copy("{{cross}}/llvm-mingw/x86_64-w64-mingw32/bin/libwinpthread-1.dll", "{{ dlpa }}/libwinpthread-1.dll")
        c.copy("{{cross}}/llvm-mingw/x86_64-w64-mingw32/share/mingw32/COPYING.winpthreads.txt", "{{ dlpa }}/libwinpthread-1.txt")

        if c.python == "3":
            c.run("""install renpy.exe {{ renpy }}/renpy.exe""")


@task(kind="python", always=True, platforms="ios")
def link_ios(c: Context):

    c.run("""{{ AR }} -r librenpython.a librenpython.o""")
    c.run("""install -d {{install}}/lib""")
    c.run("""install librenpython.a {{ install }}/lib""")


@task(kind="python", platforms="web", pythons="3", always=True)
def build_web(c: Context):

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

    c.run("""
    {{ CC }} {{ CFLAGS }}

    -DPLATFORM=\\"{{ c.platform }}\\"
    -DARCH=\\"{{ c.arch }}\\"
    -DPYTHONVER=\\"{{ pythonver }}\\"
    -DPYCVER=\\"{{ pycver }}\\"
    -D{{ c.platform|upper }}

    -c -o launcher.o
    {{ runtime }}/launcher{{ c.python }}_posix.c
    """)

@task(kind="python", platforms="web", pythons="3", always=True)
def link_web(c: Context):

    debug_asyncify = False

    asyncify_only = [
        'PyEval_EvalCode',
        'PyImport_Import',
        'PyImport_ImportModule',

        'PyImport_ImportModuleLevelObject',
        'PyObject_Call',
        'PyObject_CallFunction',
        'PyObject_CallFunctionObjArgs',
        'PyObject_CallMethod',
        'PyObject_CallMethodObjArgs',
        'PyObject_CallNoArgs',
        'PyObject_CallObject',
        'PyObject_CallOneArg',
        'PyObject_Vectorcall',
        'PyVectorcall_Call',
        '_PyEval_EvalFrameDefault',
        '_PyEval_Vector',
        '_PyFunction_Vectorcall',
        '_PyObject_FastCall',
        '_PyObject_Call',
        '_PyObject_CallFunction_SizeT',
        '_PyObject_CallFunctionVa',
        '_PyObject_CallMethodId',
        '_PyObject_CallMethodIdObjArgs',
        '_PyObject_CallMethodIdOneArg',
        '_PyObject_CallMethod_SizeT',
        '_PyObject_Call_Prepend',
        '_PyObject_FastCallDictTstate',
        '_PyObject_MakeTpCall',
        '_PyRun_AnyFileObject',
        '_PyRun_SimpleFileObject',
        '_PyVectorcall_Call',
        '__pyx_pw_10emscripten_19sleep',
        'builtin___import__',
        'builtin_exec',
        'builtin_eval',
        'cfunction_vectorcall_FASTCALL_KEYWORDS',
        'cfunction_vectorcall_O',
        'main',
        'method_vectorcall',
        'object_vacall',
        'opfunc_*',
        'run_mod',
        'slot_tp_call',
        'byn$fpcast-emu$_PyFunction_Vectorcall',
        'byn$fpcast-emu$__pyx_pw_10emscripten_19sleep',
        'byn$fpcast-emu$builtin___import__',
        'byn$fpcast-emu$builtin_exec',
        'byn$fpcast-emu$builtin_eval',
        'byn$fpcast-emu$cfunction_vectorcall_FASTCALL_KEYWORDS',
        'byn$fpcast-emu$cfunction_vectorcall_O',
        'byn$fpcast-emu$method_vectorcall',
        'byn$fpcast-emu$slot_tp_call',
        'byn$fpcast-emu$opfunc_*',
        ]

    c.var("asyncify_only", repr(asyncify_only).replace(" ", ""))

    c.run("""
    {{ CXX }} {{ LDFLAGS }}

    {% if debug_asyncify %}
    -g2 -gsource-map --source-map-base ./
    {% else %}
    -g0
    {% endif %}

    -o renpy.html
    librenpython.o
    launcher.o

    -l{{ pythonver }}

    -lrenpy

    -lavformat
    -lavcodec
    -lswscale
    -lswresample
    -lavutil
    -lSDL2_image
    -lSDL2
    -lavif
    -ldav1d
    -lyuv
    -ljpeg
    -lpng
    -lwebp
    -lsharpyuv
    -lharfbuzz
    -lbrotlidec
    -lfribidi
    -lfreetype
    -llzma
    -lbz2
    -lz
    -lm

    -lidbfs.js

    --preload-file {{ dist }}@/

    -sFULL_ES2=1
    -sMAX_WEBGL_VERSION=2
    --emit-symbol-map

    -sFILESYSTEM=1
    -sEXPORTED_RUNTIME_METHODS=['stackTrace','FS','ccall']

    -sASYNCIFY=1
    -sASYNCIFY_STACK_SIZE=65535
    -sASYNCIFY_ONLY="{{ asyncify_only }}"
    -sINITIAL_MEMORY=192MB
    -sALLOW_MEMORY_GROWTH=1

    -sEXPORTED_FUNCTIONS=['_main']

    -sMINIFY_HTML=0

    --shell-file {{ runtime }}/web/shell.html
    """, debug_asyncify=debug_asyncify)

    c.run("""install -d {{ renpy }}/web3""")
    c.run("""install renpy.html {{ renpy }}/web3/index.html""")
    c.run("""install renpy.html.symbols {{ renpy }}/web3/index.html.symbols""")
    c.run("""install {{ runtime }}/web/renpy-pre.js {{ renpy }}/web3/renpy-pre.js""")
    c.run("""install renpy.js {{ renpy }}/web3/renpy.js""")
    c.run("""install renpy.wasm {{ renpy }}/web3/renpy.wasm""")
    c.run("""install renpy.data {{ renpy }}/web3/renpy.data""")
    c.run("""install {{runtime}}/web/web-presplash.jpg {{ renpy }}/web3/web-presplash.jpg""")
    c.run("""install {{runtime}}/web/web-icon.png {{ renpy }}/web3/web-icon.png""")
    c.run("""install {{runtime}}/web/manifest.json {{ renpy }}/web3/manifest.json""")
    c.run("""install {{runtime}}/web/service-worker.js {{ renpy }}/web3/service-worker.js""")

    if debug_asyncify:
        c.run("""install renpy.wasm.map {{ renpy }}/web3/renpy.wasm.map""")

    # -sASYNCIFY_IGNORE_INDIRECT=1
    # -sASSERTIONS=1
