from renpybuild.context import Context
import sys
# The tasks to run, in order.

from . import cython

from . import env_sh

from . import sysroot
from . import toolchain

# build Freebsd toolchain prior to building everything else
if sys.platform.startswith('freebsd'):
    from . import toolchain_freebsd

from . import nasm

from . import metalangle

from . import zlib
from . import bzip2
from . import xz
from . import brotli

# build a native OpenSSL 1.1.1 due to FreeBSD deprecating a compatible version
if sys.platform.startswith('freebsd'):
    from . import openssl_freebsd
from . import openssl
from . import libffi

from . import libpng
from . import libjpeg_turbo
from . import libwebp

from . import libyuv
from . import aom
from . import libavif

from . import hostpython3
from . import hostpython2
from . import python2
from . import python3

from . import emscripten_pyx

from . import live2d

from . import rapt
from . import pyjnius
from . import pyobjus
from . import iossupport

from . import sdl2
from . import sdl2_image

from . import ffmpeg

from . import fribidi
from . import freetype
from . import harfbuzz
from . import freetypehb

from . import zsync
from . import sayvbs
from . import angle

from . import steam

from . import pygame_sdl2
from . import librenpy
from . import pythonlib
from . import renpython

from . import renpysh
from . import renios

from . import nvdrs
from . import sevenzip

from . import web
