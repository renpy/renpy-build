from renpybuild.model import task


def webtask(f, **kwargs):
    task(kind="host-python", **kwargs)(f)


@webtask
def links(c):
    c.unlink("{{ renpyweb }}/renpy")
    c.unlink("{{ renpyweb }}/pygame_sdl2")

    c.symlink("{{ renpy }}", "{{ renpyweb }}/renpy")
    c.symlink("{{ pygame_sdl2 }}", "{{ renpyweb }}/pygame_sdl2")
