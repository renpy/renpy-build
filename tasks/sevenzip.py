from renpybuild.model import task


@task(kind="python", platforms="windows")
def install(c):
    c.run("install {{ prebuilt }}/7z.sfx {{ renpy }}")
