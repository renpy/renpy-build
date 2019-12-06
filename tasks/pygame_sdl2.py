from renpybuild.model import task, annotator


@annotator
def annotate(c):
    c.env("CFLAGS", """{{ CFLAGS }} "-I{{ install }}/include/{{ pythonver }}/pygame_sdl2" """)


@task(kind="python", always=True)
def install_pygame_sdl2(c):

    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install --no-extensions")
    c.run("{{ hostpython }} {{ pygame_sdl2 }}/setup.py install_headers")
