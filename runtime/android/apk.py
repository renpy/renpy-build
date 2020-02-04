import os
import struct
import zipfile
import io


class SubFile(object):

    def __init__(self, name, base, length):
        self.f = None
        self.base = base
        self.offset = 0
        self.length = length

        self.name = name

    def open(self):
        if self.f is None:
            self.f = open(self.name, "rb")
            self.f.seek(self.base)

    def __enter__(self):
        return self

    def __exit__(self, _type, value, tb):
        self.close()
        return False

    def read(self, length=None):

        if self.f is None:
            self.open()

        maxlength = self.length - self.offset

        if length is not None:
            length = min(length, maxlength)
        else:
            length = maxlength

        if length:
            rv2 = self.f.read(length)
            self.offset += len(rv2)
        else:
            rv2 = ""

        return rv2

    def readline(self, length=None):

        if self.f is None:
            self.open()

        maxlength = self.length - self.offset
        if length is not None:
            length = min(length, maxlength)
        else:
            length = maxlength

        # Otherwise, let the system read the line all at once.
        rv = self.f.readline(length)
        self.offset += len(rv)

        return rv

    def readlines(self, length=None):
        rv = [ ]

        while True:
            l = self.readline(length)

            if not l:
                break

            if length is not None:
                length -= len(l)
                if l < 0:
                    break

            rv.append(l)

        return rv

    def xreadlines(self):
        return self

    def __iter__(self):
        return self

    def next(self):
        rv = self.readline()

        if not rv:
            raise StopIteration()

        return rv

    def flush(self):
        return

    def seek(self, offset, whence=0):
        if self.f is None:
            self.open()

        if whence == 0:
            offset = offset
        elif whence == 1:
            offset = self.offset + offset
        elif whence == 2:
            offset = self.length + offset

        if offset > self.length:
            offset = self.length

        self.offset = offset

        if offset < 0:
            offset = 0

        self.f.seek(offset + self.base)

    def tell(self):
        return self.offset

    def close(self):
        if self.f is not None:
            self.f.close()
            self.f = None

    def write(self, s):
        raise Exception("Write not supported by SubFile")


class APK(object):

    def __init__(self, apk=None, prefix="assets/"):
        """
        Opens an apk file, and lets you read the assets out of it.

        `apk`
            The path to the file to open. If this is None, it defaults to the
            apk file we are run out of.

        `prefix`
            The prefix inside the apk file to read.
        """

        if apk is None:
            apk = os.environ["ANDROID_APK"]
            print "Opening APK %r" % apk

        self.apk = apk

        self.zf = zipfile.ZipFile(apk, "r")

        # A map from unprefixed filename to ZipInfo object.
        self.info = { }

        for i in self.zf.infolist():
            fn = i.filename
            if not fn.startswith(prefix):
                continue

            fn = fn[len(prefix):]

            self.info[fn] = i

        f = file(self.apk, "rb")

        self.offset = { }

        import time
        start = time.time()

        for fn, info in self.info.items():
            f.seek(info.header_offset)

            h = struct.unpack(zipfile.structFileHeader, f.read(zipfile.sizeFileHeader))

            self.offset[fn] = (
                info.header_offset +
                zipfile.sizeFileHeader +
                h[zipfile._FH_FILENAME_LENGTH] +
                h[zipfile._FH_EXTRA_FIELD_LENGTH])

        f.close()

    def list(self):
        return sorted(self.info)

    def open(self, fn):

        if fn not in self.info:
            raise IOError("{0} not found in apk.".format(fn))

        info = self.info[fn]

        if info.compress_type == zipfile.ZIP_STORED:

            return SubFile(
                self.apk,
                self.offset[fn],
                info.file_size)

        return io.BytesIO(self.zf.read(info))
