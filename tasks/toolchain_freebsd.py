from renpybuild.context import Context
from renpybuild.task import task, annotator

import os

freebsd = "14.0.0"

@task(kind="toolchain", platforms="freebsd")
def unpack_toolchain(c: Context):
    c.clean()

    c.var("freebsd", freebsd)

    if c.arch == "x86_64":
        c.run("mkdir -p freebsd-{{freebsd}}-base")
        c.run("tar xJf {{ tmp }}/tars/freebsd-amd64-{{freebsd}}-base.tar.xz -C freebsd-{{freebsd}}-base")
    elif c.arch == "i686":
        c.run("mkdir -p freebsd-{{freebsd}}-base")
        c.run("tar xJf {{ tmp }}/tars/freebsd-i386-{{freebsd}}-base.tar.xz -C freebsd-{{freebsd}}-base")

# this is here to make setting sysroot easier; most of this will rely on it until the sysroot is finalized
@task(kind="toolchain", platforms="freebsd")
def set_sysroot(c: Context):
    c.var("freebsd", freebsd)
    c.var("sysroot", str(c.path("freebsd-{{freebsd}}-base")))
    return c

# we're building the sysroot jail here with the required libraries for cross-compiling
@task(kind="toolchain", platforms="freebsd")
def prepare_sysroot(c: Context):
    set_sysroot(c)

    # set sysroot to pull the latest packages; quarterly typically isn't new enough
    c.run("mkdir -p {{ sysroot }}/usr/local/etc/pkg/repos")
    c.run("cp -rf {{ sysroot }}/etc/pkg/FreeBSD.conf {{ sysroot }}/usr/local/etc/pkg/repos")

    # set up internal network stuff so pkg works
    c.run("cp -rf /etc/resolv.conf {{ sysroot }}/etc")
    c.run("cp -rf /etc/localtime {{ sysroot }}/etc")
    c.run("""
        sysrc -f {{ sysroot }}/etc/rc.conf hostname="base"
    """)

    c.run("""
        sed -i.orig 's/quarterly/latest/' {{ sysroot }}/usr/local/etc/pkg/repos/FreeBSD.conf
    """)

    # set the base as owned by root:wheel so that pkg will work correctly
    c.run("sudo chown -R root:wheel {{ sysroot }}")

    # mount required mount points for pkg to work; these only need to exist here
    c.run("sudo mount -t devfs devfs {{ sysroot }}/dev")
    c.run("sudo mount -t procfs procfs {{ sysroot }}/proc")

    # install required packages here
    c.run("""
        sudo chroot {{ sysroot }} /bin/sh -c '
            pkg install -y binutils gcc llvm15 pkgconf
        '
    """)

    # reset permissions back to $USER's so they can use the tools in the jail without sudo
    c.run("sudo chown -R {{ USER }} {{ sysroot }}")
    c.run("sudo umount {{ sysroot }}/dev")
    c.run("sudo umount {{ sysroot }}/proc")

    # make sysroot one that the build system can use
    c.var("platform", c.platform)
    c.var("arch", c.arch)
    c.var("main_sysroot", "{{ tmp }}/sysroot.{{ platform }}-{{ arch }}")

    # remove the old sysroot before replacing with new one
    if os.path.exists(str(c.path("{{ main_sysroot }}"))):
        c.run("rm -rf {{ main_sysroot }}")
    c.run("mv -v {{ sysroot }} {{ main_sysroot }}")

