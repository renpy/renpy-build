#!/bin/bash

set -e


ROOT=$(cd $(dirname $0); pwd)
REFS=$ROOT
BASE="$ROOT"
LLVM_MAJOR=22

export DEBIAN_FRONTEND=noninteractive

mkdir -p $ROOT/tmp

# Needed to install LLVM.
sudo apt install -y software-properties-common

# Clang is needed to compile for many platforms.
wget -O tmp/llvm.sh https://apt.llvm.org/llvm.sh
chmod +x tmp/llvm.sh
sudo tmp/llvm.sh $LLVM_MAJOR

sudo apt-get update

# Install all build and runtime dependencies in one command.
#   git build-essential ccache ... : build tools
#   llvm-22 clang-22 : needed to compile for many platforms
#   python3-dev python3-pip python3-venv : python build deps
#   curl : to install python2 pip
#   python3-jinja2 : needed by renpy-build itself
#   debootstrap qemu-user-binfmt : needed by sysroot
#   libgmp-dev libmpfr-dev libmpc-dev : needed by gcc
#   libssl-dev libbz2-dev liblzma-dev : needed by hostpython
#   bc : needed by brotli
#   ninja-build : needed for meson and cmake
#   libassimp-dev libavcodec-dev ... : OS deps required by Ren'Py
sudo apt-get install -y \
        git build-essential ccache unzip autoconf autoconf-archive automake libtool-bin pkg-config \
        llvm-$LLVM_MAJOR clang-$LLVM_MAJOR \
        python3-dev python3-pip python3-venv \
        curl \
        python3-jinja2 \
        debootstrap qemu-user-binfmt \
        libgmp-dev libmpfr-dev libmpc-dev \
        libssl-dev libbz2-dev liblzma-dev \
        bc \
        cmake ninja-build \
        libassimp-dev \
        libavcodec-dev \
        libavformat-dev \
        libswresample-dev \
        libswscale-dev \
        libharfbuzz-dev \
        libfreetype6-dev \
        libfribidi-dev \
        libsdl3-dev \
        libsdl3-image-dev \
        libjpeg-dev

# Darwin clang_rt is needed to prevent undefined symbol: __isPlatformVersionAtLeast
sudo tar xzf "$BASE/prebuilt/clang_rt.tar.gz" -C /usr/lib/clang/$LLVM_MAJOR/lib/

# UV
wget -qO- https://astral.sh/uv/install.sh | sh
uv python install 3.12

# Install the programs and virtualenvs (but not in a dev container - we use the
# presence of nightly to check.)
if [ -d "$ROOT/nightly" ]; then
    VENV="$ROOT/renpy/.venv"

    export RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

    . $BASE/nightly/git.sh
    . $BASE/nightly/python.sh
fi
