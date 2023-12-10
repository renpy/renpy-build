from renpybuild.context import Context
from renpybuild.task import task
import zipfile


@task(kind="host", platforms="all")
def unpack_sdk(c: Context):

    c.clean("{{ install }}/steam")

    if not c.path("{{ tars }}/steamworks_sdk_156.zip").exists():
        return

    zf = zipfile.ZipFile(c.path("{{ tars }}/steamworks_sdk_156.zip"))
    zf.extractall(c.path("{{ install }}/steam"))
    zf.close()


@task(kind="host", platforms="all")
def patch_sdk(c: Context):

    if not c.path("{{host}}/steam/sdk").exists():
        return

    c.chdir("{{ install }}/steam/sdk")
    # c.patch("steam-cdecl.diff")


@task(kind="python", platforms="linux,windows,mac", archs="x86_64,i686", always=True)
def build(c: Context):

    if not c.path("{{host}}/steam/sdk").exists():
        return

    if c.platform == "linux" and c.arch == "x86_64":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/linux64/libsteam_api.so")
    elif c.platform == "linux" and c.arch == "i686":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/linux32/libsteam_api.so")
    elif c.platform == "windows" and c.arch == "x86_64":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/win64/steam_api64.dll")
    elif c.platform == "windows" and c.arch == "i686":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/steam_api.dll")
    elif c.platform == "mac":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/osx/libsteam_api.dylib")
    else:
        return

    c.run("cp {{steamdll}} {{dlpa}}")

    c.run("install -d {{pytmp}}/steam")
    c.run("{{ root }}/steamapi/generate.py {{ host }}/steam/sdk/public/steam/steam_api.json {{ pytmp }}/steam/steamapi.py")
