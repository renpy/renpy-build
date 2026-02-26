FROM ubuntu:24.04

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    rm -f /etc/apt/apt.conf.d/docker-clean && \
    apt-get update && apt-get install --fix-missing --no-install-recommends -y \
    git build-essential ccache unzip autoconf autoconf-archive automake libtool-bin \
    python3-dev python3-pip python3-venv \
    curl \
    python3-jinja2 \
    debootstrap qemu-user-static \
    libgmp-dev libmpfr-dev libmpc-dev \
    software-properties-common \
    libssl-dev libbz2-dev liblzma-dev \
    bc \
    cmake clang libxml2-dev llvm \
    quilt \
    ninja-build \
    libavcodec-dev libavformat-dev \
    libswresample-dev libswscale-dev libfreetype6-dev libfribidi-dev libsdl2-dev \
    libsdl2-image-dev libsdl2-gfx-dev libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-dev \
    libharfbuzz-dev libassimp-dev

RUN wget -O /tmp/llvm.sh https://apt.llvm.org/llvm.sh && \
    chmod +x /tmp/llvm.sh && \
    /tmp/llvm.sh 18 && \
    rm /tmp/llvm.sh

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

RUN uv python install 3.12

RUN --mount=type=bind,source=prebuilt/clang_rt.tar.gz,target=/tmp/clang_rt.tar.gz \
    tar xzf /tmp/clang_rt.tar.gz -C /usr/lib/llvm-18/lib/

COPY . /build

ENTRYPOINT ["/build/docker-entrypoint.sh"]
CMD ["--help"]
