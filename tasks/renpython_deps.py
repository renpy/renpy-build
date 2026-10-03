import re

from renpybuild.context import Context
from renpybuild.task import task

# Libraries the Ren'Py modules call directly; whole-archived into the deps DLL.
# assimp is deliberately not here: only renpy.gl2.assimp uses it, so it is
# linked statically into that module's pyd instead (module-private).
WHOLE_ARCHIVE_LIBS = [
    "SDL3",
    "SDL3_image",
    "harfbuzz",
    "freetype",
    "fribidi",
    "avformat",
    "avcodec",
    "swscale",
    "swresample",
    "avutil",
]


@task(kind="arch", always=True, platforms="windows")
def link(c: Context):
    dev = c.path("{{ dlpa }}/dev")
    c.rmtree(str(dev))
    dev.mkdir(parents=True)

    # Some of the libraries (freetype, SDL3_image, assimp) are built with
    # hidden visibility presets. Clang encodes that as -exclude-symbols
    # directives in .drectve sections, which lld honors even under
    # --export-all-symbols, so those libraries' symbols are missing from the
    # export table. A .def file overrides the exclusion, so relink with one
    # listing the first-pass exports plus every defined global of the
    # whole-archived libraries.
    code, data = set(), set()
    for lib in WHOLE_ARCHIVE_LIBS:
        out = c.run("{{ NM }} --defined-only {{install}}/lib/lib{{lib}}.a", lib=lib, capture=True)

        for line in out.splitlines():
            if len(parts := line.split()) != 3:
                continue

            _, typ, name = parts
            if name.startswith(("__imp_", ".refptr.")):
                continue

            if typ == "T":
                code.add(name)
            elif typ in ("D", "B", "R", "C", "S"):
                data.add(name)

    with c.path("librenpyall.def").open("w", encoding="utf-8") as f:
        print("LIBRARY librenpyall.dll", file=f)
        print("EXPORTS", file=f)
        for name in sorted(code):
            print(f"    {name}", file=f)
        for name in sorted(data):
            print(f"    {name} DATA", file=f)

    c.run(
        """
        {{ CXX }} {{ LDFLAGS }}
        -shared
        -Wl,--out-implib=librenpyall.dll.a
        -o librenpyall.dll
        -Wl,--export-all-symbols

        -Wl,--whole-archive
        {% for lib in WHOLE_ARCHIVE_LIBS %}
        -l{{ lib }}
        {% endfor %}
        -Wl,--no-whole-archive

        -lopengl32
        -lavif
        -laom
        -lyuv
        -ljpeg
        -lpng16
        -lwebp
        -lwebpmux
        -lwebpdemux
        -lsharpyuv
        -lbrotlidec
        -lbrotlicommon
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
        -lcrypt32

        librenpyall.def
        """,
        WHOLE_ARCHIVE_LIBS=WHOLE_ARCHIVE_LIBS,
    )

    # Install development files for librenpyall so it is possible to build pyd
    # that work with MSVC Python.
    (dev / "lib").mkdir()
    c.copy("librenpyall.dll", "{{ dlpa }}")
    c.copy("librenpyall.dll.a", "{{ dlpa }}/dev/lib")

    # assimp is the only C++ library we need to handle separately.
    c.copy("{{ install }}/lib/libassimp.a", "{{ dlpa }}/dev/lib")

    (dev / "include").mkdir()
    include_root = c.expand("{{ install }}/include")

    for path in c.path(include_root).iterdir():
        if not path.is_dir():
            c.copy(str(path), str(dev / "include" / path.name))
        elif not path.name.startswith("python"):
            c.copytree(str(path), str(dev / "include" / path.name))

    # Save all include directories that annotators adds.
    prefix = dev.relative_to(c.path("{{ renpy }}")).as_posix()
    with (dev / "include_dirs.txt").open("w", encoding="utf-8") as f:
        print(f"{prefix}/include", file=f)
        for m in re.compile(rf"\s*-I{include_root}/(\S+)").finditer(c.expand("{{ CFLAGS }}")):
            name = m.group(1)
            if not name.startswith("python"):
                print(f"{prefix}/include/{name}", file=f)
