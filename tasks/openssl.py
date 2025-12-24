from renpybuild.context import Context
from renpybuild.task import task

version = "3.3.2"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("openssl-{{version}}")

    if c.platform == "mac":
        c.env("KERNEL_BITS", "64")

    if (c.platform == "windows") and (c.arch == "x86_64"):
        # c.env("CFLAGS", "{{ CFLAGS }} -DNOCRYPT")
        c.run("""./Configure mingw64 no-shared no-asm no-engine threads --prefix="{{ install }}" """)
    elif c.platform == "android":
        c.run("""./Configure cc no-shared no-asm no-engine threads --prefix="{{ install }}" """)
    elif c.platform == "web":
        raise Exception("OpenSSL isn't configured to be build for web")
    else:
        c.run("""./Configure cc no-shared no-asm no-engine threads -lpthread --prefix="{{ install }}" """)

    c.run("""{{ make }}""")
    c.run("""make install_sw""")
