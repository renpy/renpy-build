from renpybuild.model import task


@task(kind="python")
def clean(c):
    c.clean()


@task(kind="host-python", always=True)
def gen_static(c):

    c.chdir("{{ renpy }}/module")
    c.env("RENPY_DEPS_INSTALL", "/usr::/usr/lib/x86_64-linux-gnu/")
    c.env("RENPY_STATIC", "1")
    c.run("{{ hostpython }} setup.py generate")


@task(kind="python", always=True)
def build(c):

    c.env("CFLAGS", """{{ CFLAGS }} "-I{{ pygame_sdl2 }}" "-I{{ pygame_sdl2 }}/src" "-I{{ renpy }}/module" """)

    if c.python == "3":
        gen = "gen3-static/"
    else:
        gen = "gen-static/"

    modules = [ ]
    sources = [ ]

    def read_setup(dn):

        with open(dn / "Setup") as f:
            for l in f:
                l = l.partition("#")[0]
                l = l.strip()

                if not l:
                    continue

                parts = l.split()

                modules.append(parts[0])

                for i in parts[1:]:
                    i = i.replace("gen/", gen)
                    sources.append(dn / i)

    read_setup(c.pygame_sdl2)
    read_setup(c.renpy / "module")

    if c.platform == "android":
        read_setup(c.path("{{ pytmp }}/pyjnius"))

    if c.platform == "ios":
        read_setup(c.path("{{ install }}/pyobjus"))

    objects = [ ]

    for source in sources:

        object = str(source.name)[:-2] + ".o"
        objects.append(object)

        c.var("src", source)
        c.var("object", object)
        c.run("{{ CC }} {{ CFLAGS }} -c {{ src }} -o {{ object }}", verbose=True)

    c.generate("{{ source }}/librenpy_inittab.c", "inittab.c", modules=modules)
    c.run("{{ CC }} {{ CFLAGS }} -c inittab.c -o inittab.o", verbose=True)
    objects.append("inittab.o")

    c.var("objects", " ".join(objects))

    c.run("{{ AR }} r librenpy.a {{ objects }} inittab.o", verbose=True)
    c.run("{{ RANLIB }} librenpy.a", verbose=True)

    c.copy("librenpy.a", "{{ install }}/lib/librenpy.a")
