import shlex

from renpybuild.context import Context
from renpybuild.task import task

version = "1.5.4"


@task(kind="host", platforms="all")
def download(c: Context):
    c.var("version", version)
    c.download(
        "https://downloads.videolan.org/pub/videolan/dav1d/{{ version }}/dav1d-{{ version }}.tar.xz",
        "dav1d-{{ version }}.tar.xz",
    )


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xJf {{ tmp }}/tars/dav1d-{{ version }}.tar.xz")


MESON_SYSTEM = {
    "windows": "windows",
    "linux": "linux",
    "mac": "darwin",
    "ios": "darwin",
    "android": "android",
    "web": "emscripten",
}

MESON_CPU = {
    "x86_64": ("x86_64", "x86_64"),
    "sim-x86_64": ("x86_64", "x86_64"),
    "aarch64": ("aarch64", "aarch64"),
    "arm64": ("aarch64", "aarch64"),
    "arm64_v8a": ("aarch64", "aarch64"),
    "sim-arm64": ("aarch64", "aarch64"),
    "armv7l": ("arm", "armv7"),
    "armeabi_v7a": ("arm", "armv7"),
    "wasm": ("wasm32", "wasm32"),
}


def meson_list(command: str) -> str:
    """
    Turns a command line such as "ccache clang -target x" into a meson list.
    """

    return "[" + ", ".join(repr(i) for i in shlex.split(command)) + "]"


def write_cross_file(c: Context):
    env = c.environ

    family, cpu = MESON_CPU[c.arch]
    system = MESON_SYSTEM[c.platform]

    cflags = shlex.split(env.get("CFLAGS", ""))
    ldflags = shlex.split(env.get("LDFLAGS", ""))

    # Meson's compiler checks use -Werror=unused-command-line-argument, so
    # -fuse-ld goes in the link arguments.
    cc = shlex.split(env["CC"])
    ldflags = [i for i in cc if i.startswith("-fuse-ld=")] + ldflags
    cc = [i for i in cc if not i.startswith("-fuse-ld=")]

    lines = [
        "[binaries]",
        f"c = {cc!r}",
        f"ar = {meson_list(env['AR'])}",
        f"strip = {meson_list(env['STRIP'])}",
        "pkg-config = 'pkg-config'",
        "nasm = 'nasm'",
    ]

    if c.platform == "windows" and "WINDRES" in env:
        lines.append(f"windres = {meson_list(env['WINDRES'])}")

    lines += [
        "",
        "[built-in options]",
        f"c_args = {cflags!r}",
        f"c_link_args = {ldflags!r}",
        "",
        "[host_machine]",
        f"system = '{system}'",
        f"cpu_family = '{family}'",
        f"cpu = '{cpu}'",
        "endian = 'little'",
        "",
    ]

    path = c.path("{{ install }}/meson_cross_dav1d.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines))


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("dav1d-{{ version }}")

    write_cross_file(c)

    c.run("""
        meson setup build
        --cross-file={{ install }}/meson_cross_dav1d.txt
        --prefix={{ install }}
        --libdir=lib
        --buildtype=release
        --default-library=static
        -Denable_tools=false
        -Denable_tests=false
        -Denable_examples=false
        {% if c.platform == "web" or (c.platform == "ios" and c.arch == "sim-x86_64") %}
        -Denable_asm=false
        {% endif %}
        """)

    try:
        c.run("meson compile -C build")
    except Exception:
        c.run("meson compile -C build -j 1 -v")

    c.run("meson install -C build")
