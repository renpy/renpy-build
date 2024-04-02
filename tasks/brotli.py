from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "1.0.9"

@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf {{source}}/brotli-{{version}}.tar.gz")

@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("brotli-{{version}}")

    c.run("""bash ./bootstrap""")

    c.run("""{{configure}} {{ cross_config }}
          --disable-shared
          --prefix="{{ install }}"
          """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")
