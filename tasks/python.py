from renpybuild.model import task

version = "1.2.11"


@task(always=True, kind="host")
def unpack_hostpython(c):
    c.clean()
    c.run("echo test")
