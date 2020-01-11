from renpybuild.model import task


@task(kind="host", always=True)
def renpysh(c):
    c.copy("{{ runtime }}/renpy.sh", "{{ dist }}/renpy.sh")
