#!/bin/bash

set -e


ROOT=$(cd $(dirname $0); pwd)
REFS=$ROOT
BASE="$ROOT"

# Needed to build things.
sudo apt-get install -y git build-essential ccache unzip autoconf autoconf-archive automake libtool-bin

# Needed to build python things.
sudo apt-get install -y python3-dev python3-pip python3-venv

# Needed to install python2 pip
sudo apt-get install -y curl

# Needed by renpy-build itself.
sudo apt-get install -y python3-jinja2

# Needed by sysroot.
sudo apt-get install -y debootstrap qemu-user-static

# Needed by gcc.
sudo apt-get install -y libgmp-dev libmpfr-dev libmpc-dev

# Needed by llvm.
sudo apt-get install -y software-properties-common

# Needed by hostpython.
sudo apt-get install -y libssl-dev libbz2-dev liblzma-dev

# Needed by brotli.
sudo apt-get install -y bc

# Needed for mac
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y cmake clang libxml2-dev llvm

# Needed for web
sudo apt-get install -y quilt

# Needed for meson and cmake
sudo apt-get install -y ninja-build

# Install the standard set of packages needed to build Ren'Py.
sudo apt-get install -y \
    libavcodec-dev libavformat-dev \
    libswresample-dev libswscale-dev libfreetype6-dev libfribidi-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-gfx-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev \
    libharfbuzz-dev libassimp-dev

mkdir -p $ROOT/tmp

# Clang is needed to compile for many platforms.
wget -O tmp/llvm.sh https://apt.llvm.org/llvm.sh
chmod +x tmp/llvm.sh
sudo tmp/llvm.sh 18

# Darwin clang_rt is needed to prevent undefined symbol: __isPlatformVersionAtLeast
sudo tar xzf "$BASE/prebuilt/clang_rt.tar.gz" -C /usr/lib/clang/18/lib/

# UV
wget -qO- https://astral.sh/uv/install.sh | sh

# Install the programs and virtualenvs.

VENV="$ROOT/.venv"

export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

. $BASE/nightly/git.sh
. $BASE/nightly/python.sh
