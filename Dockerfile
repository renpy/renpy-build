FROM ubuntu:26.04

WORKDIR /tmp/prepare
ADD prepare.sh .
ADD prebuilt prebuilt
RUN chmod +x prepare.sh
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    ./prepare.sh
