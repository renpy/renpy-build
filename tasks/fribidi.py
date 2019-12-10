from renpybuild.model import task, annotator

version = "1.0.7"


@annotator
def annotate(c):
    if c.path("{{ install }}/include/fribidi").exists():
        c.env("CFLAGS", """{{ CFLAGS }} -I{{ install }}/include/fribidi """)


@task()
def unpack_fribidi(c):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/fribidi-{{version}}.tar.bz2")


@task()
def build_fribidi(c):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
