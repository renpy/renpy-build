from renpybuild.model import task
import zipfile


@task(kind="host")
def unpack_sdk(c):

    c.clean("{{ install }}/steam")

    if not c.path("{{ tars }}/steamworks_sdk_150.zip").exists:
        return

    zf = zipfile.ZipFile(c.path("{{ tars }}/steamworks_sdk_150.zip"))
    zf.extractall(c.path("{{ install }}/steam"))
    zf.close()


@task(kind="host")
def patch_sdk(c):

    if not c.path("{{host}}/steam/sdk").exists:
        return

    c.chdir("{{ install }}/steam/sdk")
    c.patch("steam-cdecl.diff")


@task(platforms="linux,windows,mac", archs="x86_64,i686", always=True)
def build(c):

    if not c.path("{{host}}/steam/sdk").exists:
        return

    if c.platform == "linux" and c.arch == "x86_64":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/linux64/libsteam_api.so")
        c.var("steamflags", "-L{{ host }}/steam/sdk/redistributable_bin/linux64/ -lsteam_api")
    elif c.platform == "linux" and c.arch == "i686":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/linux32/libsteam_api.so")
        c.var("steamflags", "-L{{ host }}/steam/sdk/redistributable_bin/linux32/ -lsteam_api")
    elif c.platform == "windows" and c.arch == "x86_64":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/win64/steam_api64.dll")
        c.var("steamflags", "-L{{ host }}/steam/sdk/redistributable_bin/win64/ -lsteam_api64")
    elif c.platform == "windows" and c.arch == "i686":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/steam_api.dll")
        c.var("steamflags", "-L{{ host }}/steam/sdk/redistributable_bin/ -lsteam_api")
    elif c.platform == "mac":
        c.var("steamdll", "{{ host }}/steam/sdk/redistributable_bin/osx/libsteam_api.dylib")
        c.var("steamflags", "-L{{ host }}/steam/sdk/redistributable_bin/osx -lsteam_api")
    else:
        return

    c.run("cp {{renpy}}/module/_renpysteam.pyx .")
    c.run("cp {{renpy}}/module/steamcallbacks.h .")
    c.run("cython --cplus _renpysteam.pyx")
    c.extension("_renpysteam.cpp", cflags="-I{{host}}/steam/sdk/public {{steamflags}}")
    c.run("cp {{steamdll}} {{dlpa}}")
