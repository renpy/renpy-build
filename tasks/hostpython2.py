from renpybuild.context import Context
from renpybuild.task import task

version = "2.7.18"


@task(kind="host", platforms="all", pythons="2")
def unpack_hostpython(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")

    c.chdir("Python-{{ version }}")


@task(kind="host", platforms="all", pythons="2")
def build_host(c: Context):
    c.var("version", version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""{{configure}} --prefix="{{ host }}" --enable-ipv6""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make_exec }} install""")
