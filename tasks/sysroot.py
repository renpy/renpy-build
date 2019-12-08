from renpybuild.model import task

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
]


@task(platforms="linux", archs="x86_64,i686")
def install_sysroot(c):

    if c.arch == "i686":
        deb_arch = "i386"
    elif c.arch == "x86_64":
        deb_arch = "amd64"

    c.var("deb_arch", deb_arch)

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
