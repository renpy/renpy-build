from renpybuild.context import Context
from renpybuild.task import task

PACKAGES = [
    "build-essential",
    "pkg-config",
    "libasound2-dev",
    "libpulse-dev",
    "libaudio-dev",
    "libfribidi-dev",
    "libjack-dev",
    "libsndio-dev",
    "libx11-dev",
    "libxext-dev",
    "libxrandr-dev",
    "libxcursor-dev",
    "libxfixes-dev",
    "libxi-dev",
    "libxss-dev",
    "libxtst-dev",
    "libxkbcommon-dev",
    "libdrm-dev",
    "libgbm-dev",
    "libgl1-mesa-dev",
    "libgles2-mesa-dev",
    "libegl1-mesa-dev",
    "libdbus-1-dev",
    "libibus-1.0-dev",
    "libudev-dev",
    "libthai-dev",
    "libpipewire-0.3-dev",
    "libwayland-dev",
    "libdecor-0-dev",
]


@task(platforms="linux", archs="x86_64,aarch64", always=True)
def install_linux(c: Context):

    if c.arch == "x86_64":
        deb_arch = "amd64"
        release = "jammy"
    elif c.arch == "aarch64":
        deb_arch = "arm64"
        release = "jammy"
    else:
        raise Exception("Unknown arch {}".format(c.arch))


    c.var("deb_arch", deb_arch)
    c.var("release", release)

    if not c.path("{{ sysroot }}").exists():

        c.var("packages", ",".join(PACKAGES))

        c.run("""mkdir -p "{{ tmp }}/debs" """)
        c.run("""sudo debootstrap --cache-dir="{{ tmp }}/debs" --variant=minbase --include={{ packages }} --components=main,restricted,universe,multiverse --arch {{deb_arch}} {{ release }} "{{ sysroot }}" """)
        c.run("""sudo {{source}}/make_links_relative.py {{sysroot}}""")


@task(platforms="linux")
def permissions(c: Context):
    import os

    c.var("uid", str(os.getuid()))
    c.var("gid", str(os.getgid()))

    c.run("""sudo chown -R {{uid}}:{{gid}} {{sysroot}}""")

@task(platforms="linux")
def fix_pkgconf_prefix(c: Context):
    """
    Replace prefix for .pc file in sysroot, so pkgconfig can pass right
    SYSROOT prefix to cflags. Set env PKG_CONFIG_SYSROOT_DIR isn't safe
    because it will prepend prefix to libraries outside of SYSROOT, see
    https://github.com/pkgconf/pkgconf/issues/213 and https://github.co
    m/pkgconf/pkgconf/pull/280.
    """

    c.run("""
          bash -c "grep -rl {{sysroot}} {{sysroot}}/usr/lib/{{architecture_name}}/pkgconfig > /dev/null || sed -i 's#/usr#{{sysroot}}/usr#g' $(grep -rl /usr {{sysroot}}/usr/lib/{{architecture_name}}/pkgconfig) $(grep -rl /usr {{sysroot}}/usr/share/pkgconfig)"
          """)

@task(platforms="linux")
def update_wayland_headers(c: Context):
    """
    This adds newer wayland headers to the systems we support. This
    is safe because wayland is dynamically loaded, and we don't use
    any of the newer features.
    """

    for i in c.path("{{source}}/wayland-headers/").glob("wayland*.h"):
        c.copy(str(i), "{{ sysroot }}/usr/include/" + i.name)

@task(platforms="linux")
def update_wayland_pkgconfig(c: Context):

    for i in c.path("{{source}}/wayland-pc-files/").glob("wayland*.pc"):
        c.copy(str(i), "{{ sysroot }}/usr/lib/{{architecture_name}}/pkgconfig/" + i.name)
