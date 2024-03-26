from renpybuild.context import Context
from renpybuild.task import task

version = "1.6.37"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libpng-{{version}}.tar.gz")


@task()
def build(c: Context) :
    c.var("version", version)
    c.chdir("libpng-{{version}}")

    if c.platform == "freebsd":
        c.env("CC", "ccache gcc13 {{ CFLAGS }}")
        c.env("CXX", "ccache g++13 {{ CXXFLAGS }}")
        c.env("CPP", "ccache cpp13")

    c.env("CPPFLAGS", "{{ CPPFLAGS }} -DPNG_NO_CONSOLE_IO")

    c.run("""{{configure}} {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
