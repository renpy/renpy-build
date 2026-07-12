from renpybuild.context import Context
from renpybuild.task import task

version = "1.6.0"


@task(platforms="all")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.download("https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-{{version}}.tar.gz", "libwebp-{{version}}.tar.gz")
    c.run("tar xzf {{ tmp }}/tars/libwebp-{{version}}.tar.gz")


@task(platforms="all")
def build(c: Context):
    c.var("version", version)
    c.chdir("libwebp-{{version}}")

    c.run("""
    {{configure}} {{ cross_config }}
    --disable-shared
    --prefix="{{ install }}"

{% if (c.platform == "linux") and (c.arch == "armv7l") %}
    --disable-neon
{% endif %}
    """)
    c.run("""{{ make }}""")
    c.run("""make install """)
