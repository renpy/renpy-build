# Stub in just enough of the sysconfig module to make pydoc run.

import sys, os

PLATLIB = os.path.dirname(os.path.abspath(sys.executable))
PURELIB = os.path.dirname(os.path.abspath(__file__))

def get_path(name, scheme=None, vars=None, expand=None):
    if name in [ "stdlib", "purelib", "data" ]:
        return PURELIB

    if name in [ "platstdlib", "platlib", "scripts" ]:
        return PLATLIB

    raise ValueError("Ren'Py does not understand what to do with %r." % name)
