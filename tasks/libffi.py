from renpybuild.context import Context
from renpybuild.task import task

version = "3.4.2"


@task()
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libffi-{{version}}.tar.gz")


@task()
def build(c: Context):
    c.var("version", version)
    c.chdir("libffi-{{version}}")

    c.run("""{{configure}} {{ ffi_cross_config }} --disable-shared --enable-portable-binary --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install """)

    # symlink ffi.h for Freebsd hostpythons to compile properly
    if c.platform == "freebsd":
        c.run("ln -sf {{ install }}/include/ffi.h {{ host }}/include")
        c.run("ln -sf {{ install }}/include/ffitarget.h {{ host }}/include")

        if c.arch == "i686":
            c.run("mkdir -p {{ host }}/lib32")
            c.run("ln -sf {{ install }}/lib/libffi.a {{ host }}/lib32")
        elif c.arch == "x86_64":
            c.run("ln -sf {{ install }}/lib/libffi.a {{ host }}/lib")
