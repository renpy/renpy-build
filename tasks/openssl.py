from renpybuild.model import task

version = "1.1.1g"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/openssl-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("openssl-{{version}}")

    if c.platform == "mac":
        c.env("KERNEL_BITS", "64")

    if (c.platform == "windows") and (c.arch == "x86_64"):
        # c.env("CFLAGS", "{{ CFLAGS }} -DNOCRYPT")
        c.run("""./Configure mingw64 no-shared no-asm no-engine --prefix="{{ install }}" """)
    elif (c.platform == "windows") and (c.arch == "i686"):
        c.run("""./Configure mingw no-shared no-asm no-engine --prefix="{{ install }}" """)
    else:
        c.run("""./Configure cc no-shared no-asm no-engine --prefix="{{ install }}" """)

    c.run("""{{ make }}""")
    c.run("""make install_sw""")
