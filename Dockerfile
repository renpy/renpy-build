FROM ubuntu:24.04

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update && apt-get install --fix-missing --no-install-recommends -y \
    git build-essential ccache unzip libtool-bin \
    autoconf-archive m4 pkg-config\
    python3-dev python3-pip python3-venv \
    curl \
    python3-jinja2 \
    debootstrap qemu-user-static \
    libgmp-dev libmpfr-dev libmpc-dev \
    software-properties-common \
    libssl-dev libbz2-dev liblzma-dev \
    bc \
    cmake libxml2-dev \
    quilt \
    ninja-build \
    libavcodec-dev libavformat-dev \
    libswresample-dev libswscale-dev libfreetype6-dev libfribidi-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-gfx-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev \
    libharfbuzz-dev libassimp-dev

RUN curl -fsSL https://ftp.gnu.org/gnu/autoconf/autoconf-2.72.tar.xz | tar xJ && \
    cd autoconf-2.72 && \
    ./configure --prefix=/usr && \
    make && make install && \
    cd .. && rm -rf autoconf-2.72

RUN curl -fsSL https://ftp.gnu.org/gnu/automake/automake-1.17.tar.xz | tar xJ && \
    cd automake-1.17 && \
    ./configure --prefix=/usr && \
    make && make install && \
    cd .. && rm -rf automake-1.17

RUN wget -O /tmp/llvm.sh https://apt.llvm.org/llvm.sh && \
    chmod +x /tmp/llvm.sh && \
    /tmp/llvm.sh 18 && \
    rm /tmp/llvm.sh

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

RUN uv python install 3.14

RUN --mount=type=bind,source=prebuilt/clang_rt.tar.gz,target=/tmp/clang_rt.tar.gz \
    mkdir -p /usr/lib/llvm-18/lib/clang/18/lib/ && \
    tar xzf /tmp/clang_rt.tar.gz -C /usr/lib/llvm-18/lib/clang/18/lib/

COPY . /build
