from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python", platforms="windows", always=True)
def build(c: Context):
    c.run("{{CC}} -shared -o {{ dlpa }}/nvdrs.dll {{root}}/nvlib/nvdrs.c -I{{root}}/nvlib")
    c.run("{{STRIP}} {{ dlpa }}/nvdrs.dll")
