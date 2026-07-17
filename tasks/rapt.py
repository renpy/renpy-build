from renpybuild.context import Context
from renpybuild.task import task
import shutil
import time
import os


@task(kind="host", always=True)
def copy(c: Context):

    c.copytree("{{ root }}/rapt", "{{ rapt }}")

    with open(c.path("{{ rapt }}/prototype/build.txt"), "w") as f:
        f.write(time.ctime())

    c.rmtree("{{ rapt }}/prototype/renpyandroid/src/main/java/org/libsdl")
    c.rmtree("{{ rapt }}/prototype/renpyandroid/src/main/java/org/jnius")

    os.unlink(c.path("{{ rapt }}/prototype/renpyandroid/src/main/java/org/renpy/android/Constants.java"))

    if c.path("{{ rapt }}/prototype/local.properties").exists():
        os.unlink(c.path("{{ rapt }}/prototype/local.properties"))

    c.rmtree("{{ rapt }}/prototype/app/src/main/res/mipmap-mdpi")
    c.rmtree("{{ rapt }}/prototype/app/src/main/res/mipmap-hdpi")
    c.rmtree("{{ rapt }}/prototype/app/src/main/res/mipmap-xhdpi")
    c.rmtree("{{ rapt }}/prototype/app/src/main/res/mipmap-xxhdpi")
    c.rmtree("{{ rapt }}/prototype/app/src/main/res/mipmap-xxxhdpi")

    c.rmtree("{{ rapt }}/prototype/renpyandroid/build/")
    c.rmtree("{{ rapt }}/prototype/app/build/")


@task(kind="platform", always=True)
def android_module(c: Context):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/__init__.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/apk.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
