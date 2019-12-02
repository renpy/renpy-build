from renpybuild.model import task

python2_version = "2.7.17"


@task(kind="python", pythons="2")
def unpack_python2(c):
    c.clean()

    c.var("version", python2_version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")

    c.chdir("Python-{{ version }}")
    c.patch("{{ source }}/Python-2.7.17-no-multiarch.diff")


@task(kind="python", pythons="2")
def build_python2(c):
    c.var("version", python2_version)

    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

    c.env("CONFIG_SITE", "config.site")

    c.run("""./configure {{ config_cross }} --prefix="{{ install }}" --enable-ipv6""")

    c.run("""{{ make }}""")
    c.run("""make altinstall""")
