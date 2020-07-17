from renpybuild.model import task


@task(kind="python", platforms="windows")
def install(c):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/{{ c.arch}}/libGLESv2.dll {{ dlpa }}")
    c.run("install {{ prebuilt }}/{{ c.arch }}/libEGL.dll {{ dlpa }}")
    c.run("install {{ prebuilt }}/{{ c.arch }}/d3dcompiler_47.dll {{ dlpa }}")
