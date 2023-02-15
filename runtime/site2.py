# Copyright 2013-2020 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import sys
import os
import time
import locale

# Set the default encoding to utf-8.
sys.setdefaultencoding("utf-8")

def getpreferredencoding(do_setlocale=True):
    return "utf-8"


locale.getpreferredencoding = getpreferredencoding

# A variable giving the Ren'Py platform ########################################

RENPY_PLATFORM = os.environ.get("RENPY_PLATFORM", "unknown-unknown")
PY_RENPY_PLATFORM = "py2-" + RENPY_PLATFORM

# Look for a better Python executable to set sys.executable to. ################

base = os.path.dirname(sys.executable)

PYTHON_SEARCH = [
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "pythonw"),
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "python"),
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "pythonw.exe"),
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "python.exe"),
    os.path.join(base, "pythonw"),
    os.path.join(base, "python"),
    os.path.join(base, "pythonw.exe"),
    os.path.join(base, "python.exe"),
    ]

for fn in PYTHON_SEARCH:
    if os.path.isfile(fn):
        sys.executable = fn
        break

# And the same thing for Ren'Py.

RENPY_SEARCH = [
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "renpy"),
    os.path.join(base, "lib", PY_RENPY_PLATFORM, "renpy.exe"),
    os.path.join(base, "renpy"),
    os.path.join(base, "renpy.exe"),
    ]

for fn in RENPY_SEARCH:
    if os.path.isfile(fn):
        sys.renpy_executable = fn
        break

# Submodule importing ##########################################################

# Allow Python to import submodules.
import imp


class BuiltinSubmoduleImporter(object):

    def find_module(self, name, path=None):
        if path is None:
            return None

        if "." not in name:
            return None

        if name in sys.builtin_module_names:
            return self

        return None

    def load_module(self, name):
        f, pathname, desc = imp.find_module(name, None)
        return imp.load_module(name, f, pathname, desc)


sys.meta_path.append(BuiltinSubmoduleImporter())

# Android Startup ##############################################################

if RENPY_PLATFORM.startswith("android-"):
    import androidembed

    class LogFile(object):

        def __init__(self):
            self.buffer = ''

        def write(self, s):
            s = s.replace("\0", "\\0")
            s = self.buffer + s

            lines = s.split("\n")

            for l in lines[:-1]:
                androidembed.log(l)

            self.buffer = lines[-1]

        def flush(self):
            return

    sys.stdout = sys.stderr = LogFile()

    print("Logging start.")

# iOS Startup ##############################################################

if RENPY_PLATFORM.startswith("ios-"):
    import iossupport

# Alias queue to queue. ########################################################

import Queue
sys.modules["queue"] = Queue

# Platform specific python path. ###############################################


pythonlib = os.path.dirname(__file__)
sys.path = [ pythonlib + "/site-packages", pythonlib ]

if "RENPY_PLATFORM" in os.environ:
    sys.path.append(pythonlib + "/../" + os.environ["RENPY_PLATFORM"])

# Look for binary libraries in MacOS on mac.
if RENPY_PLATFORM.startswith("mac-"):
    sys.path.append(os.path.dirname(sys.executable))

sys.path = [ os.path.abspath(i) for i in sys.path ]
