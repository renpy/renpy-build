#!/bin/bash

set -e


ROOT=$(cd $(dirname $0); pwd)
REFS=$ROOT
BASE="$ROOT"

# Needed to build things.
sudo apt-get install -y git build-essential ccache python-dev-is-python2 python3-dev unzip

# Needed to install python2 pip
sudo apt-get install -y curl

# Needed by renpy-build itself.
sudo apt-get install -y python3-jinja2

# Needed by sysroot.
sudo apt-get install -y debootstrap qemu-user-static

# Needed by gcc.
sudo apt-get install -y libgmp-dev libmpfr-dev libmpc-dev

# Needed by hostpython.
sudo apt-get install -y libssl-dev libbz2-dev

# Needed for windows.
sudo apt-get install -y mingw-w64 autoconf

# Needed for mac
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y cmake clang libxml2-dev llvm

# Needed for web
sudo apt-get install -y quilt


# Install the standard set of packages needed to build Ren'Py.
sudo apt-get install -y \
    python-dev-is-python2 libavcodec-dev libavformat-dev \
    libavresample-dev libswresample-dev libswscale-dev libfreetype6-dev libglew1.6-dev \
    libfribidi-dev libsdl2-dev libsdl2-image-dev libsdl2-gfx-dev \
    libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-turbo8-dev

# Unpack clang.
sudo tar xzf "$BASE/prebuilt/clang_rt.tar.gz" -C /usr/lib/clang/10/lib/

mkdir -p "$BASE/tmp"

GET_PIP="$ROOT/tmp/get-pip.py"

if [ ! -e $GET_PIP ]; then
    curl https://bootstrap.pypa.io/get-pip.py -o $GET_PIP
    sudo python2 $GET_PIP
fi

pip2 install virtualenv

# Set up the environment variables.

VENV="$ROOT/tmp/virtualenv.py2"

export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

. $BASE/nightly/git.sh
. $BASE/nightly/python.sh

