from renpybuild.context import Context
from renpybuild.task import task, annotator


@annotator
def annotate(c: Context):
    # Only SDL3 build needs MetalANGLE headers and macro for iOS OpenGL ES shims.
    if (c.platform == "ios") and (c.name == "sdl3"):
        c.env("CFLAGS", "{{ CFLAGS }} -F {{install}} -DMETALANGLE -Wno-unused-command-line-argument")
        c.env("OBJCFLAGS", "{{ OBJCFLAGS }} -F {{install}} -DMETALANGLE -Wno-unused-command-line-argument")
        c.env("CXXFLAGS", "{{ CXXFLAGS }} -F {{install}} -DMETALANGLE -Wno-unused-command-line-argument")

@task(kind="arch", platforms="ios")
def install(c: Context):
    c.clean("{{ install }}/MetalANGLE.framework")

    if c.arch.startswith("sim-"):
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.simulator.zip")
    else:
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.zip")
