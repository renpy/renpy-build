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


@task(kind="python-only", always=True)
def android_module(c):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/__init__.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/apk.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
