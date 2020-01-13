from renpybuild.model import task


@task(kind="python", platforms="windows")
def install(c):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/say.vbs {{ dlpa }}")
