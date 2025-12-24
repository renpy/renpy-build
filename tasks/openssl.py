from renpybuild.context import Context
from renpybuild.task import task

version = "3.3.2"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task(platforms="all")
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
        c.run("""./Configure cc no-shared no-asm no-engine threads
              no-apps no-idea no-camellia no-seed no-bf no-cast
              no-des no-rc2 no-rc4 no-rc5 no-md2 no-md4
              no-ripemd no-mdc2 no-dsa no-dh no-ecdh
              no-sock no-ssl2 no-ssl3
              no-err no-engine no-hw no-cms no-capieng
              no-weak-ssl-ciphers
              --prefix="{{ install }}" """)
    else:
        c.run("""./Configure cc no-shared no-asm no-engine threads -lpthread --prefix="{{ install }}" """)

    c.run("""{{ make }}""")
    c.run("""make install_sw""")
