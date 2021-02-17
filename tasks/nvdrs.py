from renpybuild.model import task


@task(kind="python", platforms="windows", always=True)
def build(c):
    c.run("{{CC}} -shared -o {{ dlpa }}/nvdrs.dll {{root}}/nvlib/nvdrs.c -I{{root}}/nvlib")
    c.run("{{STRIP}} {{ dlpa }}/nvdrs.dll")
