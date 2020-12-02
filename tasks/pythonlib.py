from renpybuild.model import task

import shutil

PYTHON27_MODULES = """
genericpath.pyo
UserDict.pyo
_abcoll.pyo
linecache.pyo
stat.pyo
types.pyo
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
platform.pyo
plistlib.pyo
pstats.pyo
py_compile.pyo
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
queue/
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
requests/

iossupport.pyo

six.pyo

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
def python2(c):

    search = [
        c.path("{{ install }}/lib/{{ pythonver }}"),
        c.path("{{ install }}/lib/{{ pythonver }}/site-packages"),
        c.path("{{ pytmp }}/pyjnius"),
        c.path("{{ pytmp }}/pyobjus"),
        ]

    dist = c.path("{{ distlib }}/{{ pythonver }}")

    c.clean("{{ distlib }}/{{ pythonver }}")
    c.run("{{ hostpython }} -OO -m compileall {{ install }}/lib/{{ pythonver }}/site-packages")

    for i in PYTHON27_MODULES.split():

        for d in search:
            src = d / i
            if src.exists():
                break
        else:
            raise Exception(f"Can't find {i}.")

        dst = dist / i
        pyo_copy(src, dst)

    c.copy("{{ runtime }}/site.py", "{{ distlib }}/{{ pythonver }}/site.py")
    c.run("{{ hostpython }} -OO -m compileall {{ distlib }}/{{ pythonver }}/site.py")

    c.run("mkdir -p {{ distlib }}/{{ pythonver }}/lib-dynload")
    with open(c.path("{{ distlib }}/{{ pythonver }}/lib-dynload/empty.txt"), "w") as f:
        f.write("lib-dynload needs to exist to stop an exec_prefix error.\n")

