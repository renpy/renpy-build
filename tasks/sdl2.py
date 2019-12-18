from renpybuild.model import task, annotator

version = "2.0.10"


@annotator
def annotate(c):
    c.include("{{ install }}/include/SDL2")


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/SDL2-{{version}}.tar.gz")


@task()
def build(c):
    c.var("version", version)
    c.chdir("SDL2-{{version}}")

    c.run("""./configure {{ cross_config }} --disable-shared --disable-dependency-tracking --disable-wasapi --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""make install""")
