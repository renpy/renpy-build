from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.0.7"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xjf {{source}}/fribidi-{{version}}.tar.bz2")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("fribidi-{{version}}")

    # fix for newer versions of FreeBSD
    if c.platform == "freebsd":
        c.var("config_dir", "/usr/local/share/libtools/build-aux")
    else:
        c.var("config_dir", "/usr/share/misc")
    c.run("""cp {{ config_dir }}/config.sub config.sub""")

    c.run("""{{configure}} {{ cross_config }} --disable-shared --prefix="{{ install }}" """)
    c.run("""{{ make }}""")
    c.run("""{{ make_exec }} install """)
