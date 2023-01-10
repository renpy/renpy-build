from renpybuild.context import Context
from renpybuild.task import task

version = "1.2.4"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xzf {{source}}/libwebp-{{version}}.tar.gz")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("libwebp-{{version}}")

    c.run("""
    ./configure {{ cross_config }}
    --disable-shared
    --prefix="{{ install }}"

{% if (c.platform == "linux") and (c.arch == "armv7l") %}
    --disable-neon
{% endif %}
    """)
    c.run("""{{ make }}""")
    c.run("""make install """)
