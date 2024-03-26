from renpybuild.context import Context
from renpybuild.task import task

version = "1.1.1s"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("openssl-{{version}}")

    # force openssl to use the built version of openssl for the last step
    if c.platform == "freebsd":
        c.env("C_INCLUDE_PATH", "{{ host }}/include:/usr/include:/usr/local/include")
#        c.env("CFLAGS", "{{ CFLAGS }} -L{{ install }}/opt/lib -L/usr/lib -L/usr/local/lib -L/usr/local/lib/gcc13")
#        c.env("LDFLAGS", "-L{{ install }}/opt/lib {{ LDFLAGS }}")
#        # fix a weird linking bug where these system files were hardcoded
#        c.run("cp -rf /usr/lib/crt1.o .")
#        c.run("cp -rf /usr/lib/crti.o .")
#        c.run("cp -rf /usr/lib/crtbegin.o .")
#        c.run("cp -rf /usr/lib/crtend.o .")
#        c.run("cp -rf /usr/lib/crtn.o .")
#
    if c.platform == "mac":
        c.env("KERNEL_BITS", "64")

    if (c.platform == "windows") and (c.arch == "x86_64"):
        # c.env("CFLAGS", "{{ CFLAGS }} -DNOCRYPT")
        c.run("""./Configure mingw64 no-shared no-asm no-engine threads --prefix="{{ install }}" """)
    elif (c.platform == "windows") and (c.arch == "i686"):
        c.run("""./Configure mingw no-shared no-asm no-engine threads --prefix="{{ install }}" """)
    elif c.platform == "android":
         c.run("""./Configure cc no-shared no-asm no-engine threads --prefix="{{ install }}" """)
    elif c.platform == "web":
        c.run("""emconfigure ./Configure cc no-shared no-asm no-engine threads -lpthread --prefix="{{ install }}" """)
    elif c.platform == "freebsd":
        c.run("""./Configure cc no-shared no-asm no-engine threads no-async -lpthread --prefix="{{ install }}" """)
    else:
        c.run("""./Configure cc no-shared no-asm no-engine threads -lpthread --prefix="{{ install }}" """)

    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install_sw""")
