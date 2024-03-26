#!/bin/bash

set -e


ROOT=$(cd $(dirname $0); pwd)
REFS=$ROOT
BASE="$ROOT"

# Needed to build things.
sudo pkg install git ccache autoconf autoconf-archive automake cmake gmake libtool gcc bison flex

# Needed to build python things.
sudo pkg install -y python2 python3 python310 py39-virtualenv

# Needed to install python2 pip
sudo pkg install -y curl

# Needed by renpy-build itself.
sudo pkg install -y py39-jinja2

# Needed by sysroot.
sudo pkg install -y debootstrap qemu-user-static

# Needed by gcc.
sudo pkg install -y gmp mpfr mpc gmake

# Needed by llvm.
#sudo pkg install -y software-properties-common

# Needed by hostpython.
sudo pkg install -y openssl bzip2 lzma

# Needed by brotli.
#sudo pkg install -y bc

# Needed for mac
sudo pkg install -y cmake libxml2 llvm

# Needed for web
sudo pkg install -y quilt

# Install the standard set of packages needed to build Ren'Py.
sudo pkg install -y \
    ffmpeg gstreamer1-libav gstreamer1-plugins \
    gstreamer1-plugins-good gstreamer1-plugins-bad \
    gstreamer1-plugins-ugly freetype2 fribidi sdl2 \
    sdl2_image sdl2_gfx sdl2_mixer sdl2_ttf jpeg-turbo \
    harfbuzz

mkdir -p $ROOT/tmp

# Install the programs and virtualenvs.

VENV="$ROOT/tmp/virtualenv.py3"
# required to get the proper virtualenvironment set correctly until FreeBSD moves fully to Py3.10
python3 -m virtualenv -p "/usr/local/bin/python3.10" $VENV

# none of these should be directly installed to /usr with how FreeBSD handles software
export TOOLCHAIN=/opt/toolchain/x86_64-pc-freebsd/
export RENPY_DEPS_INSTALL=/usr/local::$TOOLCHAIN

. $BASE/nightly/git.sh
. $BASE/nightly/python.sh
