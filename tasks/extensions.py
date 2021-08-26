from renpybuild.model import task


@task(kind="python", always=True)
def build(c):
    for i in c.path("{{ root }}/extensions").iterdir():
        if i.suffix != ".c":
            continue

        c.extension(str(i))
