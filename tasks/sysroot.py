from renpybuild.context import Context
from renpybuild.task import task

PACKAGES = [
    'build-essential',
    'git',
    'make',
    'pkg-config',
    'cmake',
    'ninja-build',
    'gnome-desktop-testing',
    'libasound2-dev',
    'libpulse-dev',
    'libaudio-dev',
    'libjack-dev',
    'libx11-dev',
    'libxext-dev',
    'libxrandr-dev',
    'libxcursor-dev',
    'libxfixes-dev',
    'libxi-dev',
    'libxinerama-dev',
    'libxxf86vm-dev',
    'libxss-dev',
    'libdbus-1-dev',
    'libudev-dev',
    'libdrm-dev',
    'libgbm-dev',
    'libgl1-mesa-dev',
    'libgles2-mesa-dev',
    'libglu1-mesa-dev',
    'libegl1-mesa-dev',
    'libibus-1.0-dev',
    'fcitx-libs-dev',
    'libsamplerate0-dev',
    'libsndio-dev',
    'libxkbcommon-dev',
    'libusb-dev',
    'libpipewire-0.3-dev',
    'libdecor-0-dev',
    'libsystemd-dev',
]


@task(platforms="linux", archs="x86_64,i686,aarch64", always=True)
def install_linux(c: Context):

    if c.arch == "i686":
        deb_arch = "i386"
        release = "jammy"
    elif c.arch == "x86_64":
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
        c.run("""sudo debootstrap --cache-dir="{{ tmp }}/debs" --variant=minbase --include={{ packages }} --components=main,restricted,universe,multiverse --arch {{deb_arch}} jammy "{{ sysroot }}" """)
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

    c.run("""sudo chown -R {{uid}}.{{gid}} {{sysroot}}""")

@task(platforms="linux")
def update_wayland_headers(c: Context):
    """
    This adds newer wayland headers to the systems we support. This
    is safe because wayland is dynamically loaded, and we don't use
    any of the newer features.
    """

    for i in c.path("{{source}}/wayland-headers/").glob("wayland*.h"):
        c.copy(str(i), "{{ sysroot }}/usr/include/" + i.name)
