from renpybuild.context import Context
from renpybuild.task import task

import shutil
import os
import re



PY3_MODULES = """
asyncio/
collections/
concurrent/
ctypes/
email/
encodings/
html/
http/
importlib/
json/
logging/
multiprocessing/
zoneinfo/
xml/

abc
argparse
ast
base64
binhex
bisect
_bootlocale
_bootsubprocess
bz2
calendar
cgi
chunk
cmd
code
codecs
codeop
_collections_abc
colorsys
_compat_pickle
compileall
_compression
configparser
contextlib
contextvars
copy
copyreg
cProfile
csv
dataclasses
datetime
decimal
difflib
dis
doctest
enum
filecmp
fileinput
fnmatch
formatter
fractions
ftplib
functools
__future__
genericpath
getopt
getpass
gettext
glob
graphlib
gzip
hashlib
heapq
hmac
imaplib
imghdr
imp
inspect
io
ipaddress
keyword
linecache
locale
lzma
_markupbase
mimetypes
modulefinder
netrc
ntpath
nturl2path
numbers
opcode
operator
optparse
os
_osx_support
pathlib
pdb
pickle
pickletools
pipes
pkgutil
platform
plistlib
poplib
posixpath
pprint
profile
pstats
pty
_py_abc
pyclbr
py_compile
_pydecimal
pydoc
_pyio
queue
quopri
random
re
reprlib
rlcompleter
runpy
sched
secrets
selectors
shelve
shlex
shutil
signal
_sitebuiltins
site
socket
socketserver
sre_compile
sre_constants
sre_parse
ssl
stat
statistics
string
stringprep
_strptime
struct
subprocess
sunau
symtable
tabnanny
tarfile
tempfile
textwrap
this
threading
_threading_local
timeit
token
tokenize
traceback
trace
tracemalloc
tty
types
typing
uu
uuid
warnings
wave
weakref
_weakrefset
webbrowser
zipapp
zipfile
zipimport

android/
certifi/
chardet/
ecdsa/
future/
idna/
past/
iossupport
six

pygame_sdl2/

requests/
rsa/
pyasn1/
urllib3/

urllib/

websockets/

zoneinfo/

jnius/
pyobjus/

pefile
ordlookup/

steamapi
"""


@task(kind="host-python", pythons="3", always=True)
def python3(c: Context):
    # Remove stdlib packages which include non-compilable code.
    c.rmtree("{{ install }}/lib/{{ pythonver }}/test")
    c.rmtree("{{ install }}/lib/{{ pythonver }}/lib2to3")

    # The list of rules.
    rules = set(PY3_MODULES.split())
    used_rules = set()

    if c.platform == "web":
        rules.remove("re")
        rules.add("re/")

    search = [
        c.path("{{ install }}/lib/{{ pythonver }}"),
        c.path("{{ install }}/lib/{{ pythonver }}/site-packages"),
        c.path("{{ pytmp }}/pyjnius"),
        c.path("{{ pytmp }}/pyobjus"),
        c.path("{{ pytmp }}/steam"),
        ]

    dist = c.path("{{ distlib }}/{{ pythonver }}")
    c.clean("{{ distlib }}/{{ pythonver }}")

    for base in search:
        c.compile(base)

        for fn in base.glob(c.expand("**/*.cpython-{{ pycver }}.pyc")):

            short = str(fn.relative_to(base))
            short = short.replace("__pycache__/", "")
            short = re.sub(r'\.cpython-.*.pyc$', '', short)

            matched = False

            for i in rules:

                if i[-1] == "/":
                    if short.startswith(i):
                        used_rules.add(i)
                        matched = True
                else:
                    if short == i:
                        used_rules.add(i)
                        matched = True

            if matched:
                dest = dist / (short + ".pyc")
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(fn, dest)

    # used_rules.add("steamapi")

    if rules - used_rules:
        if c.platform != "web":
            raise Exception(f"Unused rules: {rules - used_rules}")

    c.copy("{{ runtime }}/site3.py", "{{ distlib }}/{{ pythonver }}/sitecustomize.py")

    import socket
    if socket.gethostname() == "eileen":
        with open(c.path("{{ distlib }}/{{ pythonver }}/sitecustomize.py"), "a") as f:
            f.write("\n")
            f.write("import site\n")
            f.write("site.renpy_build_official = True\n")

    c.compile("{{ distlib }}/{{ pythonver }}/sitecustomize.py")
    c.unlink("{{ distlib }}/{{ pythonver }}/sitecustomize.py")

    c.copy("{{ runtime }}/sysconfig.py", "{{ distlib }}/{{ pythonver }}/sysconfig.py")
    c.compile("{{ distlib }}/{{ pythonver }}/sysconfig.py")
    c.unlink("{{ distlib }}/{{ pythonver }}/sysconfig.py")

    c.run("mkdir -p {{ distlib }}/{{ pythonver }}/lib-dynload")
    with open(c.path("{{ distlib }}/{{ pythonver }}/lib-dynload/empty.txt"), "w") as f:
        f.write("lib-dynload needs to exist to stop an exec_prefix error.\n")

    c.run("cp {{ install }}/lib/{{ pythonver }}/site-packages/certifi/cacert.pem {{ distlib }}/{{ pythonver }}/certifi/cacert.pem")


@task(kind="python", platforms="web", pythons="3", always=True)
def python3_web(c: Context):
    """
    This should do the same work as Python 3, but for the web version of Python.
    """

    python3(c)
