from renpybuild.context import Context
from renpybuild.task import task
import sys


@task(kind="host-python", always=True)
def check(c: Context):
    """
    Check that cython works.
    """

    c.clean()
    c.run("""touch test.pyx""")

    try:
        c.run("""cython --3str test.pyx""")
    except:
        print("", file=sys.stderr)
        raise SystemExit("Cython could not be run.")
