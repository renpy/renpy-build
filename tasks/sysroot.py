from renpybuild.context import Context
from renpybuild.task import task

PACKAGES = [
    'build-essential',
    'libasound2-dev',
    'libpulse-dev',
    'libaudio-dev',
    'libx11-dev',
    'libxext-dev',
    'libxrandr-dev',
    'libxcursor-dev',
    'libxi-dev',
    'libxinerama-dev',
    'libxxf86vm-dev',
    'libxss-dev',
    'libgl1-mesa-dev',
    'libesd0-dev',
    'libdbus-1-dev',
    'libudev-dev',
    'libgl1-mesa-dev',
    'libgles1-mesa-dev',
    'libgles2-mesa-dev',
    'libglu1-mesa-dev',
    'libegl1-mesa-dev',
    'libibus-1.0-dev',
    'fcitx-libs-dev',
    'libsamplerate0-dev',
    'libsndio-dev',
    'libxkbcommon-dev',
    "libusb-1.0-0-dev",
]


@task(platforms="linux", archs="x86_64,i686,aarch64", always=True)
def install_linux(c: Context):

    if c.arch == "i686":
        deb_arch = "i386"
        release = "xenial"
    elif c.arch == "x86_64":
        deb_arch = "amd64"
        release = "xenial"
    elif c.arch == "aarch64":
        deb_arch = "arm64"
        release = "focal"
    else:
        raise Exception("Unknown arch {}".format(c.arch))


    c.var("deb_arch", deb_arch)
    c.var("release", release)

    if not c.path("{{ sysroot }}").exists():

    #     c.run("""sudo rm -f {{sysroot}}/etc/resolv.conf""")
    #     c.run("""sudo cp /etc/resolv.conf {{sysroot}}/etc/resolv.conf""")
    #
    #     c.run("""sudo systemd-nspawn -D {{sysroot}} apt update""")
    #
    #     c.var("packages", " ".join(PACKAGES))
    #
    #     c.run("""sudo systemd-nspawn -D {{sysroot}} apt install -y {{ packages }} """)
    #
    # else:

        c.var("packages", ",".join(PACKAGES))

        c.run("""mkdir -p "{{ tmp }}/debs" """)
        c.run("""sudo debootstrap --cache-dir="{{ tmp }}/debs" --variant=minbase --include={{ packages }} --components=main,restricted,universe,multiverse --arch {{deb_arch}} xenial "{{ sysroot }}" """)
        c.run("""sudo {{source}}/make_links_relative.py {{sysroot}}""")


RASPI_PACKAGES = [
    'build-essential',
    'libasound2-dev',
    'libpulse-dev',
    'libaudio-dev',
    'libx11-dev',
    'libxext-dev',
    'libxrandr-dev',
    'libxcursor-dev',
    'libxi-dev',
    'libxinerama-dev',
    'libxxf86vm-dev',
    'libxss-dev',
    'libgl1-mesa-dev',
    'libesd0-dev',
    'libdbus-1-dev',
    'libudev-dev',
    'libgles2-mesa-dev',
    'libegl1-mesa-dev',
    'libibus-1.0-dev',
    'fcitx-libs-dev',
    'libsamplerate0-dev',
    'libsndio-dev',
    'libxkbcommon-dev',
    'libusb-1.0-0-dev',
]


@task(platforms="linux", archs="armv7l")
def install_linux_raspi(c: Context):

    if not c.path("{{ sysroot }}").exists():

        c.var("packages", ",".join(RASPI_PACKAGES))

        c.run("""mkdir -p "{{ tmp }}/debs" """)

        c.run("""
        sudo debootstrap
        --foreign
        --no-check-gpg
        --cache-dir={{ tmp }}/debs
        --variant=minbase
        --include={{ packages }}
        --components=main,contrib,firmware,rpi
        --arch armhf
        buster
        {{ sysroot }}
        http://archive.raspbian.org/raspbian
        """)

        c.run("""sudo cp /usr/bin/qemu-arm-static {{ sysroot }}/usr/bin """)

        c.run("""sudo chroot {{ sysroot }} /debootstrap/debootstrap --second-stage """)

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

    for i in c.path("{{source}}/wayland-pc-files/").glob("wayland*.pc"):
        c.copy(str(i), "{{ sysroot }}/usr/lib/{{architecture_name}}/pkgconfig/" + i.name)
