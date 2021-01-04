from renpybuild.model import task, annotator
import shutil


def pick_version(c):
    if c.platform == "windows":
        version = "1.0.24"
    elif c.platform == "mac":
        # Mac doesn't support C11 yet.
        version = "1.0.23"

    c.var("version", version)


@task(platforms="windows,mac")
def unpack(c):

    pick_version(c)

    c.clean()
    c.run("tar xjf {{source}}/libusb-{{version}}.tar.bz2")

    c.chdir("libusb-{{version}}")

    if c.platform == "windows":
        c.patch("usb-calling-convention.diff")


@task(platforms="windows,mac")
def build(c):
    pick_version(c)

    c.chdir("libusb-{{version}}")

    c.run("""
    ./configure {{ cross_config }}
    --prefix="{{ install }}"
    """)

    c.run("""{{ make }}""")

    if c.platform == "windows":
        c.run("""install -d {{ dlpa }}""")
        c.run("""install libusb/.libs/libusb-1.0.dll {{ dlpa }}""")
    elif c.platform == "mac":
        c.run("""install -d {{ dlpa }}""")
        c.run("""install libusb/.libs/libusb-1.0.dylib {{ dlpa }}""")

