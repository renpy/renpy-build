from renpybuild.model import task
import shutil
import time
import os


@task(kind="platform-python", platforms="android", always=True)
def copy(c):

    c.copytree("{{ root }}/rapt", "{{ raptver }}")

    with open(c.path("{{ raptver }}/prototype/build.txt"), "w") as f:
        f.write(time.ctime())

    try:
        shutil.rmtree(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl"))
    except FileNotFoundError:
        pass

    try:
        shutil.rmtree(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/jnius"))
    except FileNotFoundError:
        pass

    os.unlink(c.path("{{ raptver }}/prototype/app/build.gradle"))
    os.unlink(c.path("{{ raptver }}/prototype/app/src/main/AndroidManifest.xml"))
    os.unlink(c.path("{{ raptver }}/prototype/app/src/main/res/values/strings.xml"))
    os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/AndroidManifest.xml"))
    os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/res/values/strings.xml"))
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
def android_module(c):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/__init__.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/apk.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
