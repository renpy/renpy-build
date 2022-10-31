from renpybuild.model import task, annotator


@annotator
def annotate(c):
    c.include("{{ install }}/include/{{ pythonver }}/pygame_sdl2")


@task(kind="host-python", pythons="2", always=True)
def gen_static2(c):

    c.chdir("{{ pygame_sdl2 }}")
    c.env("PYGAME_SDL2_STATIC", "1")
    c.run("{{ hostpython }} setup.py generate")

@task(kind="host-python", pythons="3", platforms="all", always=True)
def gen_static3(c):

    c.chdir("{{ pygame_sdl2 }}")
    c.env("PYGAME_SDL2_STATIC", "1")
    c.run("{{ hostpython }} setup.py generate")



@task(kind="python", pythons="2", always=True)
def install2(c):
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install --single-version-externally-managed --record files.txt --no-extensions")
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install_headers")

@task(kind="python", platforms="all", pythons="3", always=True)
def install3(c):
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install --single-version-externally-managed --record files.txt --no-extensions")
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install_headers")
