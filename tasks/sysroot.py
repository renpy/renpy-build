from renpybuild.model import task


@task(platforms="linux")
def install_sysroot(c):

    if c.arch == "i686":
        deb_arch = "i386"
    elif c.arch == "x86_64":
        deb_arch = "amd64"

    c.var("deb_arch", deb_arch)

    c.run("""
sudo debootstrap
    --arch {{deb_arch}}
    --include build-essential
    trusty "{{ sysroot }}"
    """)
