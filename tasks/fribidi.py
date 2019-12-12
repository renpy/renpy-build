from renpybuild.model import task, annotator

version = "1.0.7"


@annotator
def annotate(c):
    c.include("{{ install }}/include/fribidi")


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/fribidi-{{version}}.tar.bz2")


@task()
def build(c):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install """)
