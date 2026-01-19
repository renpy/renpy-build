#!/bin/bash

set -e

ROOT=$(cd $(dirname $0); pwd)
REFS=$ROOT
BASE="$ROOT"

# If we're running inside Docker, we are root.
if [ -f /.dockerenv ] || [ -n "$DOCKER_BUILD" ]; then
    IS_DOCKER=1
    SUDO=""
else
    IS_DOCKER=0
    SUDO="sudo"
fi

# Function to install apt packages
install_apt() {
    if [ $IS_DOCKER -eq 1 ]; then
        apt-get update && apt-get install -y "$@" && rm -rf /var/lib/apt/lists/*
    else
        sudo apt-get install -y "$@"
    fi
}

# Needed to build things.
install_apt git build-essential ccache unzip autoconf autoconf-archive automake libtool-bin

# Needed to build python things.
install_apt python3-dev python3-pip python3-venv

# Needed to install python2 pip
install_apt curl

# Needed by renpy-build itself.
install_apt python3-jinja2

# Needed by sysroot.
install_apt debootstrap qemu-user-static

# Needed by gcc.
install_apt libgmp-dev libmpfr-dev libmpc-dev

# Needed by llvm.
install_apt software-properties-common

# Needed by hostpython.
install_apt libssl-dev libbz2-dev liblzma-dev

# Needed by brotli.
install_apt bc

# Needed for mac
install_apt cmake clang libxml2-dev llvm

# Needed for web
install_apt quilt

# Needed for meson and cmake
install_apt ninja-build

# Install the standard set of packages needed to build Ren'Py.
install_apt \
    libavcodec-dev libavformat-dev \
    libswresample-dev libswscale-dev libfreetype6-dev libfribidi-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-gfx-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev \
    libharfbuzz-dev libassimp-dev

mkdir -p $ROOT/tmp

# Clang is needed to compile for many platforms.
if [ ! -f tmp/llvm.sh ]; then
    wget -O tmp/llvm.sh https://apt.llvm.org/llvm.sh
fi
chmod +x tmp/llvm.sh
$SUDO tmp/llvm.sh 18

# Darwin clang_rt is needed to prevent undefined symbol: __isPlatformVersionAtLeast
if [ -f "$BASE/prebuilt/clang_rt.tar.gz" ]; then
    $SUDO tar xzf "$BASE/prebuilt/clang_rt.tar.gz" -C /usr/lib/clang/18/lib/
fi

# UV
if [ $IS_DOCKER -eq 1 ]; then
    wget -qO- https://astral.sh/uv/install.sh | sh
    export PATH="/root/.local/bin:$PATH"
else
    wget -qO- https://astral.sh/uv/install.sh | sh
fi

# Install the programs and virtualenvs.
if [ $IS_DOCKER -eq 0 ]; then
    export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/
    . $BASE/nightly/git.sh
    . $BASE/nightly/python.sh
fi
