from renpybuild.model import task
import shutil
import time


@task(kind="platform", platforms="android", always=True)
def copy(c):
    c.copytree("{{ root }}/rapt", "{{ rapt }}2")
    c.copytree("{{ root }}/rapt", "{{ rapt }}3")

    with open(c.path("{{ rapt }}2/prototype/build.txt"), "w") as f:
        f.write(time.ctime())

    with open(c.path("{{ rapt }}3//prototype/build.txt"), "w") as f:
        f.write(time.ctime())
