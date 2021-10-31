from renpybuild.model import task
import sys


@task(kind="python", always=True)
def check(c):
    """
    Check that cython works.
    """

    c.clean()    
    c.run("""touch test.pyx""")

    try:
        c.run("""cython test.pyx""")
    except:
        print("", file=sys.stderr)
        print("Cython could not be run.", file=sys.stderr)
        raise SystemExit(1)