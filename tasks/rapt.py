from renpybuild.model import task
import shutil


@task(kind="platform", platforms="android", always=True)
def copy(c):
    c.copytree("{{ root }}/rapt", "{{ rapt }}2")
    c.copytree("{{ root }}/rapt", "{{ rapt }}3")
