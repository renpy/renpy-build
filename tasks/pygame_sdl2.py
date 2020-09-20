from renpybuild.model import task, annotator


@annotator
def annotate(c):
    c.include("{{ install }}/include/{{ pythonver }}/pygame_sdl2")


@task(kind="host-python", always=True)
def gen_static(c):

    c.chdir("{{ pygame_sdl2 }}")
    c.env("PYGAME_SDL2_STATIC", "1")
    c.run("{{ hostpython }} setup.py generate")


@task(kind="python", always=True)
def install(c):
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install --single-version-externally-managed --record files.txt --no-extensions")
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install_headers")
