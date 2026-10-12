from renpybuild.context import Context
from renpybuild.task import task


@task(kind="host", platforms="linux,windows,mac")
def fetch_prism(c: Context):
    c.chdir("{{ renpy }}")
    c.run("python scripts/fetch_prism.py")
