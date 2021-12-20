from renpybuild.model import task


@task(kind="python", always=True)
def renpysh(c):
    c.generate("{{ runtime }}/renpy.sh", "{{ dist }}/renpy{{ python }}.sh")
    c.run("chmod +x {{ dist }}/renpy{{ python }}.sh")

    if c.python == "2":
        c.copy("{{ dist }}/renpy{{ python }}.sh", "{{ dist }}/renpy.sh")
        