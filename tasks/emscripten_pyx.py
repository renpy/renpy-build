from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python", pythons="3", platforms="web", always=True)
def build(c: Context):

    c.run("cp {{runtime}}/emscripten.pyx emscripten.pyx")
    c.run("cython emscripten.pyx")

    c.run("install -d {{install}}/emscripten_pyx")
    c.run("install emscripten.c {{install}}/emscripten_pyx")

    with open(c.path("{{ install }}/emscripten_pyx/Setup"), "w") as f:
        f.write("emscripten emscripten.c\n")
