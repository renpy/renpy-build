from renpybuild.context import Context
from renpybuild.task import task


@task(kind="arch")
def clean(c: Context):
    c.clean()


@task(kind="host", always=True)
def gen_static3(c: Context):

    c.chdir("{{ renpy }}")
    c.env("RENPY_DEPS_INSTALL", "/usr::/usr/lib/x86_64-linux-gnu/")
    c.env("RENPY_STATIC", "1")
    c.env("RENPY_REGENERATE_CYTHON", "1")
    c.run("{{ hostpython }} setup.py generate")


@task(kind="arch", platforms="all", always=True)
def build(c: Context):

    c.env("CFLAGS", """{{ CFLAGS }} "-I{{ renpy }}/src" "-I{{renpy}}/tmp/gen3-static" """)
    c.env("CXXFLAGS", """{{ CXXFLAGS }} "-I{{ renpy }}/src" "-I{{renpy}}/tmp/gen3-static" """)

    gen = "gen3-static/"

    modules = []
    sources = []
    source_module = {}

    def read_setup(dn, suffix=""):
        with open(dn / ("Setup" + suffix)) as f:
            for line in f:
                line = line.partition("#")[0].strip()
                if not line:
                    continue
                parts = line.split()
                module_name = parts[0]
                modules.append(module_name)

                for i in parts[1:]:
                    if "libhydrogen" not in i:
                        i = i.replace("gen/", gen)

                    source = dn / i
                    sources.append(source)
                    source_module[source] = module_name

    read_setup(c.renpy / "src")
    read_setup(c.root / "extensions")

    if c.platform == "android":
        read_setup(c.path("{{ pytmp }}/pyjnius"))

    if c.platform == "ios" or c.platform == "mac":
        read_setup(c.path("{{ install }}/pyobjus"))

    if c.platform == "windows" or c.platform == "mac" or c.platform == "linux":
        read_setup(c.renpy / "src", ".tfd")

    if c.platform == "web":
        read_setup(c.path("{{ install }}/emscripten_pyx"))

    read_setup(c.path("{{ source }}/brotli"))

    objects = []

    with c.run_group() as g:
        for source in sources:
            name, _, ext = str(source.name).rpartition(".")

            object = name + ".o"
            objects.append(object)

            c.var("src", source)
            c.var("object", object)

            c.var("pyinit_define", "")
            if module_name := source_module.get(source):
                mangled = module_name.replace(".", "_")
                short = module_name.rpartition(".")[-1]
                c.var("pyinit_define", f"-DPyInit_{short}=PyInit_{mangled}")

            if ext == "c":
                g.run("{{ CC }} {{ CFLAGS }} {{ pyinit_define }} -c {{ src }} -o {{ object }}")
            else:
                g.run("{{ CXX }} {{ CXXFLAGS }} {{ pyinit_define }} -c {{ src }} -o {{ object }}")

        c.generate("{{ runtime }}/librenpy_inittab.c", "inittab.c", modules=modules)
        g.run("{{ CC }} {{ CFLAGS }} -c inittab.c -o inittab.o")
        objects.append("inittab.o")

    c.var("objects", " ".join(objects))

    c.unlink("librenpy.a")
    if c.platform in ("mac", "ios"):
        c.run("{{ AR }} --format=darwin r librenpy.a {{ objects }} inittab.o")
    else:
        c.run("{{ AR }} r librenpy.a {{ objects }} inittab.o")
    c.run("{{ RANLIB }} librenpy.a")

    c.copy("librenpy.a", "{{ install }}/lib/librenpy.a")
