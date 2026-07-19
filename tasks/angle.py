from renpybuild.context import Context
from renpybuild.task import task


@task(kind="arch", platforms="windows", always=True)
def install(c: Context):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/{{ c.arch}}/libGLESv2.dll {{ dlpa }}")
    c.run("install {{ prebuilt }}/{{ c.arch }}/libEGL.dll {{ dlpa }}")
