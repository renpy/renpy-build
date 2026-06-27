FROM ubuntu:26.04

WORKDIR /tmp/prepare
ADD prepare.sh .
ADD prebuilt prebuilt
RUN chmod +x prepare.sh
RUN printf '#!/bin/sh\nexec "$@"\n' > /usr/local/bin/sudo \
    && chmod +x /usr/local/bin/sudo
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    ./prepare.sh
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /
