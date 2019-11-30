from renpybuild.model import task

version = "1.1.1d"


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
    ./Configure cc no-shared no-asm --prefix="{{ install }}"
    """)

    c.run("""make""")
    c.run("""make install_sw""")
