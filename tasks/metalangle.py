from renpybuild.context import Context
from renpybuild.task import task, annotator


@annotator
def annotate(c: Context):
    if c.platform == "ios":
        c.env("CFLAGS", "{{ CFLAGS }} -F {{install}} -framework MetalANGLE -DMETALANGLE -Wno-unused-command-line-argument")
        c.env("OBJCFLAGS", "{{ OBJCFLAGS }} -F {{install}} -framework MetalANGLE -DMETALANGLE  -Wno-unused-command-line-argument")
        c.env("CXXFLAGS", "{{ CXXFLAGS }} -F {{install}} -framework MetalANGLE -DMETALANGLE  -Wno-unused-command-line-argument")

@task(kind="python", platforms="ios")
def install(c: Context):
    c.clean("{{ install }}/MetalANGLE.framework")

    if c.arch.startswith("sim-"):
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.simulator.zip")
    else:
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.zip")
