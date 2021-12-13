from renpybuild.model import task, annotator

version = "3.10.1"

@annotator
def annotate(c):
    if c.python == "3":
        c.var("pythonver", "python3.10")
        c.include("{{ install }}/include/{{ pythonver }}")


@task(kind="python", pythons="3")
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/Python-{{version}}.tgz")

@task(kind="python", pythons="3", platforms="linux,mac,ios")
def patch_posix(c):
    c.var("version", version)

    c.chdir("Python-{{ version }}")
    c.patch("python3/no-multiarch.diff")
    c.patch("python3/cross-darwin.diff")

def common(c):
    c.var("version", version)
    c.chdir("Python-{{ version }}")

    with open(c.path("config.site"), "w") as f:
        f.write("ac_cv_file__dev_ptmx=no\n")
        f.write("ac_cv_file__dev_ptc=no\n")

    c.env("CONFIG_SITE", "config.site")

@task(kind="python", pythons="3", platforms="linux,mac")
def build_posix(c):

    common(c)

    c.env("CFLAGS", "{{ CFLAGS }} -DXML_POOR_ENTROPY=1 -DUSE_PYEXPAT_CAPI -DHAVE_EXPAT_CONFIG_H ")

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" --with-system-ffi --enable-ipv6""")

    c.generate("{{ source }}/Python-{{ version }}-Setup.local", "Modules/Setup.local")

    c.run("""{{ make }}""")
    
    c.run("""{{ make }} install""")

    c.copy("{{ host }}/bin/python3", "{{ install }}/bin/hostpython3")

    raise SystemExit(1)
    
    
