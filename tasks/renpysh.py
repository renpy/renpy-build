from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python", always=True)
def renpysh(c: Context):
    c.copy("{{ runtime }}/renpy.sh", "{{ dist }}/renpy.sh")
    c.run("chmod +x {{ dist }}/renpy.sh")
