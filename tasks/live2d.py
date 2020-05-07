from renpybuild.model import task, annotator


@task(always=True)
def build(c):
    c.clean()

    c.var("cubism_zip", "Cubism3SDKforNative-beta12.zip")
    c.var("cubism_dir", "Cubism3SDKforNative-beta12")

    c.var("live2d", c.path("{{ root }}/live2d"))

    c.env("RENPY", "{{ renpy }}")
    c.env("CUBISM", c.path("{{ cubism_dir }}"))

    if not c.path("{{ live2d }}").is_dir():
        return

    if not c.path("{{ tars }}/{{ cubism_zip }}").exists():
        return

    c.run("unzip -q {{ tars }}/{{ cubism_zip }}")

    c.copy("{{live2d}}/live2dmodel.pyx", "live2dmodel.pyx")
    c.copy("{{live2d}}/live2dcsm.pxi", "live2dcsm.pxi")

    c.run("cython live2dmodel.pyx -I {{ renpy }}")

    c.extension("live2dmodel.c", "-I{{ CUBISM }}/Core/include")
