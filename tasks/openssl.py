from renpybuild.model import task

version = "1.1.1d"

PLATFORMS = """
android-arm
android-arm64
android-armeabi
android-mips
android-mips64
android-x86
android-x86_64


android64
android64-aarch64
android64-mips64
android64-x86_64
bsdi-elf-gcc
cc
darwin-i386-cc
darwin-ppc-cc
darwin64-ppc-cc
darwin64-x86_64-cc
gcc
haiku-x86
haiku-x86_64
hpux-ia64-cc
hpux-ia64-gcc
hpux-parisc-cc
hpux-parisc-gcc
hpux-parisc1_1-cc
hpux-parisc1_1-gcc
hpux64-ia64-cc
hpux64-ia64-gcc
hpux64-parisc2-cc
hpux64-parisc2-gcc
hurd-x86
ios-cross
ios-xcrun
ios64-cross
ios64-xcrun
iossimulator-xcrun
iphoneos-cross
irix-mips3-cc
irix-mips3-gcc
irix64-mips4-cc
irix64-mips4-gcc
linux-aarch64
linux-alpha-gcc
linux-aout
linux-arm64ilp32
linux-armv4
linux-c64xplus
linux-elf
linux-generic32
linux-generic64
linux-ia64
linux-mips32
linux-mips64
linux-ppc
linux-ppc64
linux-ppc64le
linux-sparcv8
linux-sparcv9
linux-x32
linux-x86
linux-x86-clang
linux-x86_64
linux-x86_64-clang
linux32-s390x
linux64-mips64
linux64-s390x
linux64-sparcv9
mingw
mingw64
nextstep
nextstep3.3
sco5-cc
sco5-gcc
solaris-sparcv7-cc
solaris-sparcv7-gcc
solaris-sparcv8-cc
solaris-sparcv8-gcc
solaris-sparcv9-cc
solaris-sparcv9-gcc
solaris-x86-gcc
solaris64-sparcv9-cc
solaris64-sparcv9-gcc
solaris64-x86_64-cc
solaris64-x86_64-gcc
tru64-alpha-cc
tru64-alpha-gcc
uClinux-dist
uClinux-dist64
unixware-2.0
unixware-2.1
unixware-7
unixware-7-gcc
vms-alpha
vms-alpha-p32
vms-alpha-p64
vms-ia64
vms-ia64-p32
vms-ia64-p64
vos-gcc
vxworks-mips
vxworks-ppc405
vxworks-ppc60x
vxworks-ppc750
vxworks-ppc750-debug
vxworks-ppc860
vxworks-ppcgen
vxworks-simlinux
"""


@task()
def unpack_openssl(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task()
def build_openssl(c):
    c.var("version", version)
    c.chdir("openssl-{{version}}")

    if c.platform == "mac":
        c.environ("KERNEL_BITS", "64")

    c.run("""
    ./Configure cc no-shared --prefix="{{ install }}"
    """)

    c.run("""make""")
    c.run("""make install""")
