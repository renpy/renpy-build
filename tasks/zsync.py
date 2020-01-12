from renpybuild.model import task

version = "0.6.2"


@task()
def unpack(c):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/zsync-{{version}}.tar.bz2")


@task(platforms="linux,mac")
def build(c):

    c.var("version", version)
    c.chdir("zsync-{{ version }}")

    c.patch("zsync-no-isastty.diff", p=1)
    c.patch("zsync-compress-5.diff", p=0)

    c.run("""./configure {{ cross_config }} --prefix="{{ install }}" """)
    c.run("""{{ make }}""")

    c.run("install -d {{ dlpa }}")
    c.run("install zsync zsyncmake {{ dlpa }}")


@task(platforms="windows")
def install(c):
    c.run("install -d {{ dlpa }}")
    c.run("install {{ prebuilt }}/zsync.exe {{ prebuilt}}/zsyncmake.exe {{ dlpa }}")

