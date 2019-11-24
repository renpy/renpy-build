from renpybuild.model import task

PACKAGES = [
    "build-essential",
]


@task(platforms="linux", archs="x86_64,i686")
def install_sysroot(c):

    if c.arch == "i686":
        deb_arch = "i386"
    elif c.arch == "x86_64":
        deb_arch = "amd64"

    c.var("deb_arch", deb_arch)
    c.var("packages", ",".join(PACKAGES))

    c.clean("{{ sysroot }}")

    c.run("""sudo debootstrap --arch {{deb_arch}} --include {{packages}} trusty "{{ sysroot }}" """)

