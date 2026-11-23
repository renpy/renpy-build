from renpybuild.context import Context
from renpybuild.task import task, annotator

cubism_zip = "CubismSdkForNative-5-r.5.zip"
cubism_dir = "CubismSdkForNative-5-r.5"


@annotator
def annotate(c: Context):
    # The Cubism SDK is optional, so only set CUBISM when its zip is present.
    if not c.path("{{ tars }}/" + cubism_zip).exists():
        return

    c.include("{{ install }}/cubism/Core/include")
    c.env("CUBISM", "{{ install }}/cubism")


@task(platforms="all")
def build(c: Context):
    c.clean()

    c.var("cubism_zip", cubism_zip)
    c.var("cubism_dir", cubism_dir)

    c.var("live2d", c.path("{{ root }}/live2d"))

    if not c.path("{{ tars }}/{{ cubism_zip }}").exists():
        return

    c.run("unzip -q {{ tars }}/{{ cubism_zip }}")

    c.rmtree("{{ install }}/cubism")
    c.run("mv {{cubism_dir}} {{ install }}/cubism")
