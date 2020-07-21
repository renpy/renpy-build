from renpybuild.model import task, annotator


@annotator
def annotate(c):
    c.include("{{ install }}/cubism/Core/include")
    c.env("CUBISM", "{{ install }}/cubism")


@task()
def build(c):
    c.clean()

    c.var("cubism_zip", "CubismSdkForNative-4-r.1.zip")
    c.var("cubism_dir", "CubismSdkForNative-4-r.1")

    c.var("live2d", c.path("{{ root }}/live2d"))

    if not c.path("{{ tars }}/{{ cubism_zip }}").exists():
        return

    c.run("unzip -q {{ tars }}/{{ cubism_zip }}")

    c.rmtree("{{ install }}/cubism")
    c.run("mv {{cubism_dir}} {{ install }}/cubism")
