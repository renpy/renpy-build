from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python")
def clean(c: Context):
    c.clean()



@task(kind="host-python", platforms="all", pythons="3", always=True)
def gen_static3(c: Context):

    c.chdir("{{ renpy }}")
    c.env("RENPY_DEPS_INSTALL", "/usr::/usr/lib/x86_64-linux-gnu/")
    c.env("RENPY_STATIC", "1")
    c.env("RENPY_REGENERATE_CYTHON", "1")
    c.run("{{ hostpython }} setup.py generate")


@task(kind="python", platforms="all", always=True)
def build(c: Context):

    if c.platform == "web" and c.python == "2":
        return

    c.env("CFLAGS", """{{ CFLAGS }} "-I{{ renpy }}/src" "-I{{renpy}}/tmp/gen3" """)
    c.env("CXXFLAGS", """{{ CXXFLAGS }} "-I{{ renpy }}/src" "-I{{renpy}}/tmp/gen3" """)

    gen = "gen3-static/"

    modules = [ ]
    sources = [ ]

    def read_setup(dn, suffix=""):

        with open(dn / ("Setup" + suffix)) as f:
            for l in f:
                l = l.partition("#")[0]
                l = l.strip()

                if not l:
                    continue

                parts = l.split()

                if parts[0] == "renpy.compat.dictviews" and c.python != "2":
                    continue

                modules.append(parts[0])

                for i in parts[1:]:
                    if "libhydrogen" not in i:
                        i = i.replace("gen/", gen)
                    sources.append(dn / i)

    read_setup(c.renpy / "src" )
    read_setup(c.root / "extensions")

    if c.platform == "android":
        read_setup(c.path("{{ pytmp }}/pyjnius"))

    if c.platform == "ios" or c.platform == "mac":
        read_setup(c.path("{{ install }}/pyobjus"))

    if c.platform == "windows" or c.platform == "mac" or c.platform == "linux":
        read_setup(c.renpy / "src", ".tfd")

    if c.platform != "web":
        read_setup(c.renpy / "src", ".ecs")

    if c.platform == "web" and c.python == "3":
        read_setup(c.path("{{ install }}/emscripten_pyx"))

    read_setup(c.path("{{ source }}/brotli"))

    objects = [ ]

    with c.run_group() as g:

        for source in sources:

            name, _, ext = str(source.name).rpartition(".")

            object = name + ".o"
            objects.append(object)

            c.var("src", source)
            c.var("object", object)

            if ext == "c":
                g.run("{{ CC }} {{ CFLAGS }} -c {{ src }} -o {{ object }}")
            else:
                g.run("{{ CXX }} {{ CXXFLAGS }} -c {{ src }} -o {{ object }}")

        c.generate("{{ runtime }}/librenpy_inittab{{ c.python }}.c", "inittab.c", modules=modules)
        g.run("{{ CC }} {{ CFLAGS }} -c inittab.c -o inittab.o")
        objects.append("inittab.o")

    c.var("objects", " ".join(objects))

    c.unlink("librenpy.a")
    c.run("{{ AR }} r librenpy.a {{ objects }} inittab.o")
    c.run("{{ RANLIB }} librenpy.a")

    c.copy("librenpy.a", "{{ install }}/lib/librenpy.a")
