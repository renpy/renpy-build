from renpybuild.context import Context
from renpybuild.task import task
import shutil
import time
import os


@task(kind="platform-python", platforms="android", always=True)
def copy(c: Context):

    c.copytree("{{ root }}/rapt", "{{ raptver }}")

    c.run("mv {{ raptver }}/blocklist3.txt {{ raptver }}/blocklist.txt")
    c.run("mv {{ raptver }}/keeplist3.txt {{ raptver }}/keeplist.txt")

    c.run("rm {{ raptver }}/blocklist2.txt")
    c.run("rm {{ raptver }}/keeplist2.txt")

    with open(c.path("{{ raptver }}/prototype/build.txt"), "w") as f:
        f.write(time.ctime())

    c.rmtree("{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl")
    c.rmtree("{{ raptver }}/prototype/renpyandroid/src/main/java/org/jnius")

    os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/renpy/android/Constants.java"))

    if c.path("{{ raptver }}/prototype/local.properties").exists():
        os.unlink(c.path("{{ raptver }}/prototype/local.properties"))

    c.rmtree("{{ raptver }}/prototype/app/src/main/res/mipmap-mdpi")
    c.rmtree("{{ raptver }}/prototype/app/src/main/res/mipmap-hdpi")
    c.rmtree("{{ raptver }}/prototype/app/src/main/res/mipmap-xhdpi")
    c.rmtree("{{ raptver }}/prototype/app/src/main/res/mipmap-xxhdpi")
    c.rmtree("{{ raptver }}/prototype/app/src/main/res/mipmap-xxxhdpi")

    c.rmtree("{{ raptver }}/prototype/renpyandroid/build/")
    c.rmtree("{{ raptver }}/prototype/app/build/")


@task(kind="host-python", always=True)
def android_module(c: Context):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/__init__.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/apk.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
