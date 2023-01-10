from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python", platforms="windows")
def install(c: Context):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/say.vbs {{ dlpa }}")
