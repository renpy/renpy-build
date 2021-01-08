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

# The argv emulator code comes from py2app:
#
#     Copyright (c) 2004 Bob Ippolito.
#
# (py2app is also under the MIT license.)

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

# Look for a better Python executable to set sys.executable to. ################

base = os.path.dirname(sys.executable)

PYTHON_SEARCH = [
    os.path.join(base, "lib", RENPY_PLATFORM, "pythonw"),
    os.path.join(base, "lib", RENPY_PLATFORM, "python"),
    os.path.join(base, "lib", RENPY_PLATFORM, "pythonw.exe"),
    os.path.join(base, "lib", RENPY_PLATFORM, "python.exe"),
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
    os.path.join(base, "lib", RENPY_PLATFORM, "renpy"),
    os.path.join(base, "lib", RENPY_PLATFORM, "renpy.exe"),
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

# Mac Argv Emulation ###########################################################
# Taken from py2app.

if sys.version_info[0] == 3:

    def B(value):
        return value.encode('ascii')

else:

    def B(value):
        return value

import ctypes
import struct


class AEDesc (ctypes.Structure):
    _fields_ = [
        ('descKey', ctypes.c_int),
        ('descContent', ctypes.c_void_p),
    ]


class EventTypeSpec (ctypes.Structure):
    _fields_ = [
        ('eventClass', ctypes.c_int),
        ('eventKind', ctypes.c_uint),
    ]


def _ctypes_setup():
    carbon = ctypes.CDLL('/System/Library/Carbon.framework/Carbon')

    timer_func = ctypes.CFUNCTYPE(
        None, ctypes.c_void_p, ctypes.c_long)

    ae_callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p,
                                   ctypes.c_void_p, ctypes.c_void_p)
    carbon.AEInstallEventHandler.argtypes = [
        ctypes.c_int, ctypes.c_int, ae_callback,
        ctypes.c_void_p, ctypes.c_char ]
    carbon.AERemoveEventHandler.argtypes = [
        ctypes.c_int, ctypes.c_int, ae_callback,
        ctypes.c_char ]

    carbon.AEProcessEvent.restype = ctypes.c_int
    carbon.AEProcessEvent.argtypes = [ctypes.c_void_p]

    carbon.ReceiveNextEvent.restype = ctypes.c_int
    carbon.ReceiveNextEvent.argtypes = [
        ctypes.c_long, ctypes.POINTER(EventTypeSpec),
        ctypes.c_double, ctypes.c_char,
        ctypes.POINTER(ctypes.c_void_p)
    ]

    carbon.AEGetParamDesc.restype = ctypes.c_int
    carbon.AEGetParamDesc.argtypes = [
        ctypes.c_void_p, ctypes.c_int, ctypes.c_int,
        ctypes.POINTER(AEDesc)]

    carbon.AECountItems.restype = ctypes.c_int
    carbon.AECountItems.argtypes = [ ctypes.POINTER(AEDesc),
                                     ctypes.POINTER(ctypes.c_long) ]

    carbon.AEGetNthDesc.restype = ctypes.c_int
    carbon.AEGetNthDesc.argtypes = [
        ctypes.c_void_p, ctypes.c_long, ctypes.c_int,
        ctypes.c_void_p, ctypes.c_void_p ]

    carbon.AEGetDescDataSize.restype = ctypes.c_int
    carbon.AEGetDescDataSize.argtypes = [ ctypes.POINTER(AEDesc) ]

    carbon.AEGetDescData.restype = ctypes.c_int
    carbon.AEGetDescData.argtypes = [
        ctypes.POINTER(AEDesc),
        ctypes.c_void_p,
        ctypes.c_int,
        ]

    carbon.FSRefMakePath.restype = ctypes.c_int
    carbon.FSRefMakePath.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint]

    return carbon


def _run_argvemulator(timeout=60):

    # Configure ctypes
    carbon = _ctypes_setup()

    # Is the emulator running?
    running = [True]

    # Configure AppleEvent handlers
    ae_callback = carbon.AEInstallEventHandler.argtypes[2]

    kAEInternetSuite, = struct.unpack('>i', B('GURL'))
    kAEISGetURL, = struct.unpack('>i', B('GURL'))
    kCoreEventClass, = struct.unpack('>i', B('aevt'))
    kAEOpenApplication, = struct.unpack('>i', B('oapp'))
    kAEOpenDocuments, = struct.unpack('>i', B('odoc'))
    keyDirectObject, = struct.unpack('>i', B('----'))
    typeAEList, = struct.unpack('>i', B('list'))
    typeChar, = struct.unpack('>i', B('TEXT'))
    typeFSRef, = struct.unpack('>i', B('fsrf'))
    FALSE = B('\0')
    TRUE = B('\1')

    kEventClassAppleEvent, = struct.unpack('>i', B('eppc'))
    kEventAppleEvent = 1

    @ae_callback
    def open_app_handler(message, reply, refcon):
        running[0] = False
        return 0

    carbon.AEInstallEventHandler(kCoreEventClass, kAEOpenApplication,
                                 open_app_handler, 0, FALSE)

    @ae_callback
    def open_file_handler(message, reply, refcon):
        listdesc = AEDesc()
        sts = carbon.AEGetParamDesc(message, keyDirectObject, typeAEList,
                                    ctypes.byref(listdesc))
        if sts != 0:
            print >> sys.stderr, "argvemulator warning: cannot unpack open document event"
            running[0] = False
            return

        item_count = ctypes.c_long()
        sts = carbon.AECountItems(ctypes.byref(listdesc), ctypes.byref(item_count))
        if sts != 0:
            print >> sys.stderr, "argvemulator warning: cannot unpack open document event"
            running[0] = False
            return

        desc = AEDesc()
        for i in range(item_count.value):
            sts = carbon.AEGetNthDesc(ctypes.byref(listdesc), i + 1, typeFSRef, 0, ctypes.byref(desc))
            if sts != 0:
                print >> sys.stderr, "argvemulator warning: cannot unpack open document event"
                running[0] = False
                return

            sz = carbon.AEGetDescDataSize(ctypes.byref(desc))
            buf = ctypes.create_string_buffer(sz)
            sts = carbon.AEGetDescData(ctypes.byref(desc), buf, sz)
            if sts != 0:
                print >> sys.stderr, "argvemulator warning: cannot extract open document event"
                continue

            fsref = buf

            buf = ctypes.create_string_buffer(1024)
            sts = carbon.FSRefMakePath(ctypes.byref(fsref), buf, 1023)
            if sts != 0:
                print >> sys.stderr, "argvemulator warning: cannot extract open document event"
                continue

            print >> sys.stderr, "Adding: %s" % (repr(buf.value.decode('utf-8')),)

            if sys.version_info[0] > 2:
                sys.argv.append(buf.value.decode('utf-8'))
            else:
                sys.argv.append(buf.value)

        running[0] = False
        return 0

    carbon.AEInstallEventHandler(kCoreEventClass, kAEOpenDocuments,
                                 open_file_handler, 0, FALSE)

    @ae_callback
    def open_url_handler(message, reply, refcon):
        listdesc = AEDesc()
        ok = carbon.AEGetParamDesc(message, keyDirectObject, typeAEList,
                                   ctypes.byref(listdesc))
        if ok != 0:
            print >> sys.stderr, "argvemulator warning: cannot unpack open document event"
            running[0] = False
            return

        item_count = ctypes.c_long()
        sts = carbon.AECountItems(ctypes.byref(listdesc), ctypes.byref(item_count))
        if sts != 0:
            print >> sys.stderr, "argvemulator warning: cannot unpack open url event"
            running[0] = False
            return

        desc = AEDesc()
        for i in range(item_count.value):
            sts = carbon.AEGetNthDesc(ctypes.byref(listdesc), i + 1, typeChar, 0, ctypes.byref(desc))
            if sts != 0:
                print >> sys.stderr, "argvemulator warning: cannot unpack open URL event"
                running[0] = False
                return

            sz = carbon.AEGetDescDataSize(ctypes.byref(desc))
            buf = ctypes.create_string_buffer(sz)
            sts = carbon.AEGetDescData(ctypes.byref(desc), buf, sz)
            if sts != 0:
                print >> sys.stderr, "argvemulator warning: cannot extract open URL event"

            else:
                if sys.version_info[0] > 2:
                    sys.argv.append(buf.value.decode('utf-8'))
                else:
                    sys.argv.append(buf.value)

        running[0] = False
        return 0

    carbon.AEInstallEventHandler(kAEInternetSuite, kAEISGetURL,
                                 open_url_handler, 0, FALSE)

    start = time.time()
    now = time.time()
    eventType = EventTypeSpec()
    eventType.eventClass = kEventClassAppleEvent
    eventType.eventKind = kEventAppleEvent

    while running[0] and now - start < timeout:
        event = ctypes.c_void_p()

        sts = carbon.ReceiveNextEvent(1, ctypes.byref(eventType),
                                      start + timeout - now, TRUE, ctypes.byref(event))
        if sts != 0:
            print >> sys.stderr, "argvemulator warning: fetching events failed"
            break

        sts = carbon.AEProcessEvent(event)
        if sts != 0:
            print >> sys.stderr, "argvemulator warning: processing events failed"
            break

    carbon.AERemoveEventHandler(kCoreEventClass, kAEOpenApplication,
                                open_app_handler, FALSE)
    carbon.AERemoveEventHandler(kCoreEventClass, kAEOpenDocuments,
                                open_file_handler, FALSE)
    carbon.AERemoveEventHandler(kAEInternetSuite, kAEISGetURL,
                                open_url_handler, FALSE)


def _renpy_argv_emulation():

    # only use if started by LaunchServices
    for arg in sys.argv[1:]:
        if arg.startswith('-psn'):
            try:
                _run_argvemulator()
            except:
                pass

            # Remove the funny -psn_xxx_xxx argument
            if len(sys.argv) > 1 and sys.argv[1][:4] == '-psn':
                del sys.argv[1]

            break

# Platform specific python path. ###############################################


pythonlib = os.path.dirname(__file__)
sys.path = [ pythonlib + "/site-packages", pythonlib ]

if "RENPY_PLATFORM" in os.environ:
    sys.path.append(pythonlib + "/../" + os.environ["RENPY_PLATFORM"])

sys.path = [ os.path.abspath(i) for i in sys.path ]

