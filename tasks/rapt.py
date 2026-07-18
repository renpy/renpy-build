import os
import time
import zipfile

from renpybuild.context import Context
from renpybuild.task import task

markupsafe_version = "3.0.3"
jinja_version = "3.1.6"


@task(kind="host")
def download(c: Context):
    c.var("version", markupsafe_version)

    url = "https://github.com/pallets/markupsafe/releases/download/{{ version }}/markupsafe-{{ version }}.tar.gz"
    dest = c.expand("markupsafe-{{ version }}.tar.gz")

    c.download(url, dest)

    c.var("version", jinja_version)

    url = "https://github.com/pallets/jinja/releases/download/{{ version }}/jinja2-{{ version }}-py3-none-any.whl"
    dest = c.expand("jinja2-{{ version }}-py3-none-any.whl")

    c.download(url, dest)


@task(kind="host")
def unpack(c: Context):
    c.var("version", markupsafe_version)
    c.clean("{{ tmp }}/source/markupsafe-{{ version }}")
    c.chdir("{{ tmp }}/source")
    c.run("tar xzf {{ tmp }}/tars/markupsafe-{{ version }}.tar.gz")

    c.var("version", jinja_version)
    c.clean("{{ tmp }}/source/jinja2-{{ version }}")

    with zipfile.ZipFile(c.path("{{ tmp }}/tars/jinja2-{{ version }}-py3-none-any.whl")) as zf:
        zf.extractall(c.path("{{ tmp }}/source/jinja2-{{ version }}"))


@task(kind="host", always=True)
def copy(c: Context):
    c.copytree("{{ root }}/rapt", "{{ rapt }}")

    c.var("version", markupsafe_version)
    c.copytree("{{ tmp }}/source/markupsafe-{{ version }}/src/markupsafe", "{{ rapt }}/buildlib/markupsafe")

    c.var("version", jinja_version)
    c.copytree("{{ tmp }}/source/jinja2-{{ version }}/jinja2", "{{ rapt }}/buildlib/jinja2")

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
