from renpybuild.model import task
import os


@task(kind="host-python")
def copytree(c):
    c.copytree("{{ root }}/renios", "{{ renios }}")


def lipo_and_strip(c, namefilter):
    c.var("lipo", "{{ tmp }}/cross.ios-arm64/bin/arm-apple-darwin11-lipo")
    c.var("strip", "{{ tmp }}/cross.ios-arm64/bin/arm-apple-darwin11-strip")

    paths = [
        c.path("{{ tmp }}/install.ios-arm64/lib"),
        c.path("{{ tmp }}/install.ios-armv7s/lib"),
        ]

    c.var("paths", paths, expand=False)

    c.run("install -d {{ renios }}/prototype/prebuilt/release")

    for i in paths[0].glob("*.a"):
        if i.is_symlink():
            continue

        i = i.name

        if not namefilter(i):
            continue

        c.var("i", i)
        c.run("""
        {{ lipo }}
        -create
{% for p in paths %}
        {{ p }}/{{ i }}
{% endfor %}
        -output {{ renios }}/prototype/prebuilt/release/{{ i }}
        """)

        os.chmod(c.path("{{ renios }}/prototype/prebuilt/release/{{ i }}"), 0o755)

        c.run("{{ strip }} -S {{ renios }}/prototype/prebuilt/release/{{ i }}", quiet=True)

    # debug.

    paths = [
        c.path("{{ tmp }}/install.ios-x86_64/lib"),
        ]

    c.var("paths", paths, expand=False)

    c.run("install -d {{ renios }}/prototype/prebuilt/debug")

    for i in paths[0].glob("*.a"):
        if i.is_symlink():
            continue

        i = i.name

        if not namefilter(i):
            continue

        c.var("i", i)
        c.run("""
        {{ lipo }}
        -create
{% for p in paths %}
        {{ p }}/{{ i }}
{% endfor %}
        -output {{ renios }}/prototype/prebuilt/debug/{{ i }}
        """)

        os.chmod(c.path("{{ renios }}/prototype/prebuilt/debug/{{ i }}"), 0o755)

        c.run("{{ strip }} -S {{ renios }}/prototype/prebuilt/debug/{{ i }}", quiet=True)


@task(kind="host-python", platforms="ios")
def lipo(c):
    lipo_and_strip(c, lambda n : True)


@task(kind="host-python", platforms="ios", always=True)
def lipo_renpy(c):
    lipo_and_strip(c, lambda n : "librenpy" in n)
