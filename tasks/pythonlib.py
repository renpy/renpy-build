from renpybuild.model import task

import shutil

PYTHON27_MODULES = """
./genericpath.pyo
./UserDict.pyo
./_abcoll.pyo
./linecache.pyo
./stat.pyo
./types.pyo
./pygame_sdl2/__init__.pyo
./pygame_sdl2/compat.pyo
./pygame_sdl2/time.pyo
./pygame_sdl2/version.pyo
./pygame_sdl2/sysfont.pyo
./pygame_sdl2/sprite.pyo
./warnings.pyo
./os.pyo
./copy_reg.pyo
./site.pyo
./ssl.pyo
./abc.pyo
./posixpath.pyo
./_weakrefset.pyo

./argparse.pyo
./ast.pyo
./atexit.pyo
./base64.pyo
./BaseHTTPServer.pyo
./bisect.pyo
./calendar.pyo
./cgi.pyo
./CGIHTTPServer.pyo
./chunk.pyo
./cmd.pyo
./codecs.pyo
./collections.pyo
./colorsys.pyo
./commands.pyo
./compileall.pyo
./contextlib.pyo
./cookielib.pyo
./Cookie.pyo
./copy.pyo
./cProfile.pyo

./ctypes/_endian.pyo
./ctypes/__init__.pyo

./ctypes/macholib/dyld.pyo
./ctypes/macholib/dylib.pyo
./ctypes/macholib/framework.pyo
./ctypes/macholib/__init__.pyo
./ctypes/util.pyo
./ctypes/wintypes.pyo

./decimal.pyo
./difflib.pyo
./dis.pyo
./dummy_threading.pyo
./dummy_thread.pyo

./email/base64mime.pyo
./email/charset.pyo
./email/encoders.pyo
./email/errors.pyo
./email/feedparser.pyo
./email/generator.pyo
./email/header.pyo
./email/__init__.pyo
./email/iterators.pyo
./email/message.pyo
./email/mime/audio.pyo
./email/mime/base.pyo
./email/mime/image.pyo
./email/mime/__init__.pyo
./email/mime/message.pyo
./email/mime/multipart.pyo
./email/mime/nonmultipart.pyo
./email/mime/text.pyo
./email/_parseaddr.pyo
./email/parser.pyo
./email/quoprimime.pyo
./email/utils.pyo

./encodings/aliases.pyo
./encodings/ascii.pyo
./encodings/base64_codec.pyo
./encodings/hex_codec.pyo
./encodings/idna.pyo
./encodings/__init__.pyo
./encodings/latin_1.pyo
./encodings/mbcs.pyo
./encodings/raw_unicode_escape.pyo
./encodings/string_escape.pyo
./encodings/unicode_escape.pyo
./encodings/utf_16_be.pyo
./encodings/utf_16_le.pyo
./encodings/utf_16.pyo
./encodings/utf_32_be.pyo
./encodings/utf_8.pyo
./encodings/zlib_codec.pyo

./fnmatch.pyo
./ftplib.pyo
./functools.pyo
./__future__.pyo
./getopt.pyo
./gettext.pyo
./glob.pyo
./gzip.pyo
./hashlib.pyo
./heapq.pyo
./hmac.pyo
./httplib.pyo
./imghdr.pyo
./importlib/__init__.pyo
./inspect.pyo
./io.pyo
./json/decoder.pyo
./json/encoder.pyo
./json/__init__.pyo
./json/scanner.pyo
./keyword.pyo
./locale.pyo
./logging/__init__.pyo
./_LWPCookieJar.pyo
./mimetools.pyo
./mimetypes.pyo
./_MozillaCookieJar.pyo
./nturl2path.pyo
./numbers.pyo
./opcode.pyo
./optparse.pyo
./pickle.pyo
./platform.pyo
./plistlib.pyo
./pstats.pyo

./pyasn1/codec/ber/decoder.pyo
./pyasn1/codec/ber/encoder.pyo
./pyasn1/codec/ber/eoo.pyo
./pyasn1/codec/ber/__init__.pyo
./pyasn1/codec/cer/decoder.pyo
./pyasn1/codec/cer/encoder.pyo
./pyasn1/codec/cer/__init__.pyo
./pyasn1/codec/der/decoder.pyo
./pyasn1/codec/der/encoder.pyo
./pyasn1/codec/der/__init__.pyo
./pyasn1/codec/__init__.pyo
./pyasn1/codec/native/decoder.pyo
./pyasn1/codec/native/encoder.pyo
./pyasn1/codec/native/__init__.pyo
./pyasn1/compat/binary.pyo
./pyasn1/compat/calling.pyo
./pyasn1/compat/dateandtime.pyo
./pyasn1/compat/__init__.pyo
./pyasn1/compat/integer.pyo
./pyasn1/compat/octets.pyo
./pyasn1/compat/string.pyo
./pyasn1/debug.pyo
./pyasn1/error.pyo
./pyasn1/__init__.pyo
./pyasn1/type/base.pyo
./pyasn1/type/char.pyo
./pyasn1/type/constraint.pyo
./pyasn1/type/error.pyo
./pyasn1/type/__init__.pyo
./pyasn1/type/namedtype.pyo
./pyasn1/type/namedval.pyo
./pyasn1/type/opentype.pyo
./pyasn1/type/tagmap.pyo
./pyasn1/type/tag.pyo
./pyasn1/type/univ.pyo
./pyasn1/type/useful.pyo


./py_compile.pyo
./Queue.pyo
./quopri.pyo
./random.pyo
./repr.pyo
./re.pyo
./rfc822.pyo

./rsa/asn1.pyo
./rsa/cli.pyo
./rsa/common.pyo
./rsa/_compat.pyo
./rsa/core.pyo
./rsa/__init__.pyo
./rsa/key.pyo
./rsa/machine_size.pyo
./rsa/parallel.pyo
./rsa/pem.pyo
./rsa/pkcs1.pyo
./rsa/pkcs1_v2.pyo
./rsa/prime.pyo
./rsa/randnum.pyo
./rsa/transform.pyo
./rsa/util.pyo



./shlex.pyo
./shutil.pyo
./SimpleHTTPServer.pyo
./socket.pyo
./SocketServer.pyo
./sre_compile.pyo
./sre_constants.pyo
./sre_parse.pyo
./StringIO.pyo
./stringprep.pyo
./string.pyo
./_strptime.pyo
./struct.pyo
./subprocess.pyo
./sunau.pyo
./tarfile.pyo
./tempfile.pyo
./textwrap.pyo
./_threading_local.pyo
./threading.pyo
./tokenize.pyo
./token.pyo
./traceback.pyo
./urllib2.pyo
./urllib.pyo
./urlparse.pyo
./UserList.pyo
./UserString.pyo
./uuid.pyo
./uu.pyo
./wave.pyo
./weakref.pyo
./webbrowser.pyo

./xml/etree/ElementPath.pyo
./xml/etree/ElementTree.pyo
./xml/etree/__init__.pyo
./xml/__init__.pyo
./xml/parsers/expat.pyo
./xml/parsers/__init__.pyo
./zipfile.pyo


builtins/__init__.pyo
copyreg/__init__.pyo
future/__init__.pyo
future/builtins/__init__.pyo
future/builtins/newsuper.pyo
future/builtins/newnext.pyo
future/builtins/newround.pyo
future/builtins/iterators.pyo
future/builtins/new_min_max.pyo
future/builtins/misc.pyo
future/builtins/disabled.pyo
future/backports/_markupbase.pyo
future/backports/http/cookies.pyo
future/backports/http/client.pyo
future/backports/http/__init__.pyo
future/backports/http/cookiejar.pyo
future/backports/http/server.pyo
future/backports/xmlrpc/client.pyo
future/backports/xmlrpc/__init__.pyo
future/backports/xmlrpc/server.pyo
future/backports/__init__.pyo
future/backports/socketserver.pyo
future/backports/html/__init__.pyo
future/backports/html/entities.pyo
future/backports/html/parser.pyo
future/backports/email/base64mime.pyo
future/backports/email/_encoded_words.pyo
future/backports/email/feedparser.pyo
future/backports/email/__init__.pyo
future/backports/email/utils.pyo
future/backports/email/_header_value_parser.pyo
future/backports/email/encoders.pyo
future/backports/email/headerregistry.pyo
future/backports/email/errors.pyo
future/backports/email/iterators.pyo
future/backports/email/mime/base.pyo
future/backports/email/mime/__init__.pyo
future/backports/email/mime/image.pyo
future/backports/email/mime/text.pyo
future/backports/email/mime/audio.pyo
future/backports/email/mime/application.pyo
future/backports/email/mime/multipart.pyo
future/backports/email/mime/nonmultipart.pyo
future/backports/email/mime/message.pyo
future/backports/email/parser.pyo
future/backports/email/_policybase.pyo
future/backports/email/_parseaddr.pyo
future/backports/email/message.pyo
future/backports/email/policy.pyo
future/backports/email/charset.pyo
future/backports/email/quoprimime.pyo
future/backports/email/generator.pyo
future/backports/email/header.pyo
future/backports/socket.pyo
future/backports/misc.pyo
future/backports/urllib/__init__.pyo
future/backports/urllib/response.pyo
future/backports/urllib/robotparser.pyo
future/backports/urllib/parse.pyo
future/backports/urllib/request.pyo
future/backports/urllib/error.pyo
future/backports/datetime.pyo
future/backports/total_ordering.pyo
future/standard_library/__init__.pyo
future/tests/base.pyo
future/tests/__init__.pyo
future/moves/itertools.pyo
future/moves/dbm/__init__.pyo
future/moves/dbm/ndbm.pyo
future/moves/dbm/gnu.pyo
future/moves/dbm/dumb.pyo
future/moves/_markupbase.pyo
future/moves/http/cookies.pyo
future/moves/http/client.pyo
future/moves/http/__init__.pyo
future/moves/http/cookiejar.pyo
future/moves/http/server.pyo
future/moves/__init__.pyo
future/moves/copyreg.pyo
future/moves/socketserver.pyo
future/moves/html/__init__.pyo
future/moves/html/entities.pyo
future/moves/html/parser.pyo
future/moves/configparser.pyo
future/moves/subprocess.pyo
future/moves/reprlib.pyo
future/moves/collections.pyo
future/moves/builtins.pyo
future/moves/winreg.pyo
future/moves/_thread.pyo
future/moves/queue.pyo
future/moves/test/__init__.pyo
future/moves/test/support.pyo
future/moves/urllib/__init__.pyo
future/moves/urllib/response.pyo
future/moves/urllib/robotparser.pyo
future/moves/urllib/parse.pyo
future/moves/urllib/request.pyo
future/moves/urllib/error.pyo
future/moves/sys.pyo
future/moves/pickle.pyo
future/moves/_dummy_thread.pyo
future/types/__init__.pyo
future/types/newobject.pyo
future/types/newrange.pyo
future/types/newopen.pyo
future/types/newmemoryview.pyo
future/types/newlist.pyo
future/types/newdict.pyo
future/types/newint.pyo
future/types/newbytes.pyo
future/types/newstr.pyo
future/utils/surrogateescape.pyo
future/utils/__init__.pyo
html/__init__.pyo
html/entities.pyo
html/parser.pyo
http/cookies.pyo
http/client.pyo
http/__init__.pyo
http/cookiejar.pyo
http/server.pyo
past/__init__.pyo
past/builtins/noniterators.pyo
past/builtins/__init__.pyo
past/builtins/misc.pyo
past/types/__init__.pyo
past/types/oldstr.pyo
past/types/basestring.pyo
past/types/olddict.pyo
past/utils/__init__.pyo
past/translation/__init__.pyo
queue/__init__.pyo
reprlib/__init__.pyo
socketserver/__init__.pyo
winreg/__init__.pyo
"""


@task(kind="python-only", pythons="2", always=True)
def python2(c):
    lib = c.path("{{ install }}/lib/{{ pythonver }}")
    site = lib / "site-packages"
    dist = c.path("{{ distlib }}/{{ pythonver }}")

    c.run("{{ hostpython }} -OO -m compileall {{ install }}/lib/{{ pythonver }}/site-packages")

    for i in PYTHON27_MODULES.split():

        if (lib / i).exists():
            src = lib / i
        elif (site / i).exists():
            src = site / i
        else:
            raise Exception(f"Can't find {i}.")

        dst = dist / i
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)

    c.copy("{{ runtime }}/site.py", "{{ distlib }}/{{ pythonver }}/site.py")
    c.run("{{ hostpython }} -OO -m compileall {{ distlib }}/{{ pythonver }}/site.py")

    print(lib, site)

