from renpybuild.context import Context
from renpybuild.task import task, annotator


@annotator
def annotate(c: Context):
    if c.platform == "ios":
        c.env("CFLAGS", "{{ CFLAGS }} -F {{install}} -framework MetalANGLE -DMETALANGLE")

@task(kind="python", platforms="ios")
def install(c: Context):
    c.clean("{{ install }}/MetalANGLE.framework")

    if c.arch.startswith("sim-"):
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.simulator.zip")
    else:
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.zip")
