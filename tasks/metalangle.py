from renpybuild.model import task, annotator


@annotator
def annotate(c):
    if c.platform == "ios":
        c.env("CFLAGS", "{{ CFLAGS }} -F {{install}} -framework MetalANGLE -DMETALANGLE")

@task(kind="python", platforms="ios")
def install(c):
    c.clean("{{ install }}/MetalANGLE.framework")

    if c.arch.startswith("sim-"):
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.simulator.zip")
    else:
        c.run("unzip -d {{ install }} {{ source }}/MetalANGLE.framework.ios.zip")
