from renpybuild.context import Context
from renpybuild.task import task


@task(kind="python", always=True)
def renpysh(c: Context):
    c.generate("{{ runtime }}/renpy.sh", "{{ dist }}/renpy{{ python }}.sh")
    c.run("chmod +x {{ dist }}/renpy{{ python }}.sh")

    if c.python == "2":
        c.copy("{{ dist }}/renpy{{ python }}.sh", "{{ dist }}/renpy.sh")
        
