from renpybuild.context import Context
from renpybuild.task import task

import shutil
import os
import re

PYTHON27_MODULES = """
genericpath.pyo
UserDict.pyo
_abcoll.pyo
linecache.pyo
stat.pyo
types.pyo
typing.pyo
pygame_sdl2/__init__.pyo
pygame_sdl2/compat.pyo
pygame_sdl2/time.pyo
pygame_sdl2/version.pyo
pygame_sdl2/sysfont.pyo
pygame_sdl2/sprite.pyo
warnings.pyo
os.pyo
copy_reg.pyo
site.pyo
ssl.pyo
abc.pyo
posixpath.pyo
_weakrefset.pyo

argparse.pyo
ast.pyo
atexit.pyo
base64.pyo
BaseHTTPServer.pyo
bisect.pyo
calendar.pyo
cgi.pyo
CGIHTTPServer.pyo
chunk.pyo
cmd.pyo
codecs.pyo
collections.pyo
colorsys.pyo
commands.pyo
compileall.pyo
contextlib.pyo
cookielib.pyo
Cookie.pyo
copy.pyo
cProfile.pyo

ctypes/_endian.pyo
ctypes/__init__.pyo
ctypes/macholib/dyld.pyo
ctypes/macholib/dylib.pyo
ctypes/macholib/framework.pyo
ctypes/macholib/__init__.pyo
ctypes/util.pyo
ctypes/wintypes.pyo

csv.pyo
decimal.pyo
difflib.pyo
dis.pyo
dummy_threading.pyo
dummy_thread.pyo

encodings/aliases.pyo
encodings/ascii.pyo
encodings/base64_codec.pyo
encodings/hex_codec.pyo
encodings/idna.pyo
encodings/__init__.pyo
encodings/latin_1.pyo
encodings/mbcs.pyo
encodings/raw_unicode_escape.pyo
encodings/string_escape.pyo
encodings/unicode_escape.pyo
encodings/utf_16_be.pyo
encodings/utf_16_le.pyo
encodings/utf_16.pyo
encodings/utf_32_be.pyo
encodings/utf_8.pyo
encodings/zlib_codec.pyo
encodings/cp437.pyo

fnmatch.pyo
ftplib.pyo
functools.pyo
__future__.pyo
getopt.pyo
gettext.pyo
glob.pyo
gzip.pyo
hashlib.pyo
heapq.pyo
hmac.pyo
httplib.pyo
imghdr.pyo
importlib/__init__.pyo
inspect.pyo
io.pyo
json/decoder.pyo
json/encoder.pyo
json/__init__.pyo
json/scanner.pyo
keyword.pyo
list2cmdline.pyo
locale.pyo
logging/__init__.pyo
_LWPCookieJar.pyo
mimetools.pyo
mimetypes.pyo
_MozillaCookieJar.pyo
ntpath.pyo
nturl2path.pyo
numbers.pyo
opcode.pyo
optparse.pyo
pickle.pyo
pkgutil.pyo
platform.pyo
plistlib.pyo
pstats.pyo
py_compile.pyo
pydoc.pyo
Queue.pyo
quopri.pyo
random.pyo
repr.pyo
re.pyo
rfc822.pyo
shlex.pyo
shutil.pyo
SimpleHTTPServer.pyo
socket.pyo
SocketServer.pyo
sre_compile.pyo
sre_constants.pyo
sre_parse.pyo
StringIO.pyo
stringprep.pyo
string.pyo
_strptime.pyo
struct.pyo
subprocess.pyo
sunau.pyo
tarfile.pyo
tempfile.pyo
textwrap.pyo
_threading_local.pyo
threading.pyo
tokenize.pyo
token.pyo
traceback.pyo
urllib2.pyo
urllib.pyo
urlparse.pyo
UserList.pyo
UserString.pyo
uuid.pyo
uu.pyo
wave.pyo
weakref.pyo
webbrowser.pyo

xml/etree/ElementPath.pyo
xml/etree/ElementTree.pyo
xml/etree/__init__.pyo
xml/__init__.pyo
xml/parsers/expat.pyo
xml/parsers/__init__.pyo
zipfile.pyo

rsa/
pyasn1/

builtins/
email/
copyreg/
future/
html/
http/
past/
reprlib/
socketserver/
winreg/

android
jnius/
pyobjus/

urllib3/
idna/
certifi/
chardet/
ecdsa/
requests/

iossupport.pyo

six.pyo

pefile.pyo
ordlookup/

steamapi.pyo
"""


def pyo_copy(src, dst):
    """
    Copies the pyo and pem files from `src` to `dst`.

    `src` and `dst` may be either directories or files.
    """

    if src.is_dir():
        for i in src.iterdir():
            pyo_copy(i, dst / i.name)
        return

    if not (str(src).endswith(".pyo") or str(src).endswith(".pem")):
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)


@task(kind="host-python", pythons="2", always=True)
def python2(c: Context):
    # Remove stdlib packages which include non-compilable code.
    c.rmtree("{{ install }}/lib/{{ pythonver }}/test")
    c.rmtree("{{ install }}/lib/{{ pythonver }}/lib2to3")

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

    for i in PYTHON27_MODULES.split():

        for d in search:
            src = d / i
            if src.exists():
                break
        else:
            raise Exception(f"Can't find {i}.")

        dst = dist / i
        pyo_copy(src, dst)

    c.copy("{{ runtime }}/site2.py", "{{ distlib }}/{{ pythonver }}/site.py")

    import socket
    if socket.gethostname() == "eileen":
        with open(c.path("{{ distlib }}/{{ pythonver }}/site.py"), "a") as f:
            f.write("\n")
            f.write("renpy_build_official = True\n")

    c.compile("{{ distlib }}/{{ pythonver }}/site.py")
    c.unlink("{{ distlib }}/{{ pythonver }}/site.py")

    c.run("mkdir -p {{ distlib }}/{{ pythonver }}/lib-dynload")
    with open(c.path("{{ distlib }}/{{ pythonver }}/lib-dynload/empty.txt"), "w") as f:
        f.write("lib-dynload needs to exist to stop an exec_prefix error.\n")


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
