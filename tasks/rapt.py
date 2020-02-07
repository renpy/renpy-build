from renpybuild.model import task
import shutil
import time
import os


@task(kind="platform", platforms="android", always=True)
def copy(c):

    for i in [ "2", "3" ]:

        c.var("raptver", "{{ rapt }}" + i)

        c.copytree("{{ root }}/rapt", "{{ raptver }}")

        with open(c.path("{{ raptver }}/prototype/build.txt"), "w") as f:
            f.write(time.ctime())

        shutil.rmtree(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/libsdl"))
        shutil.rmtree(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/jnius"))

        os.unlink(c.path("{{ raptver }}/prototype/app/build.gradle"))
        os.unlink(c.path("{{ raptver }}/prototype/app/src/main/AndroidManifest.xml"))
        os.unlink(c.path("{{ raptver }}/prototype/app/src/main/res/values/strings.xml"))
        os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/AndroidManifest.xml"))
        os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/res/values/strings.xml"))
        os.unlink(c.path("{{ raptver }}/prototype/renpyandroid/src/main/java/org/renpy/android/Constants.java"))

        os.unlink(c.path("{{ raptver }}/prototype/app/local.properties"))

        shutil.rmtree(c.path("{{ raptver }}/app/src/main/res/mipmap-mdpi"))
        shutil.rmtree(c.path("{{ raptver }}/app/src/main/res/mipmap-hdpi"))
        shutil.rmtree(c.path("{{ raptver }}/app/src/main/res/mipmap-xhdpi"))
        shutil.rmtree(c.path("{{ raptver }}/app/src/main/res/mipmap-xxdpi"))
        shutil.rmtree(c.path("{{ raptver }}/app/src/main/res/mipmap-xxxdpi"))


@task(kind="python-only", always=True)
def android_module(c):
    c.run("""install -d {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/__init__.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
    c.run("""install {{ runtime }}/android/apk.py {{ install }}/lib/{{ pythonver }}/site-packages/android""")
