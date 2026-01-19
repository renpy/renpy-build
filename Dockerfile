FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONHASHSEED=0 \
    DOCKER_BUILD=1

WORKDIR /build

COPY prepare.sh /build/
RUN ./prepare.sh

# Copy build system files
COPY extensions/ /build/extensions/
COPY nvlib/ /build/nvlib/
COPY patches/ /build/patches/
COPY prebuilt/ /build/prebuilt/
COPY renios/ /build/renios/
COPY renpybuild/ /build/renpybuild/
COPY runtime/ /build/runtime/
COPY source/ /build/source/
COPY specs/ /build/specs/
COPY steamapi/ /build/steamapi/
COPY tars/ /build/tars/
COPY tasks/ /build/tasks/
COPY tools/ /build/tools/
COPY build.sh /build/

# Copy and set up entrypoint
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Ensure UV is in PATH
ENV PATH="/root/.local/bin:$PATH" \
    RENPY_DEPS_INSTALL=/usr::/usr/lib/x86_64-linux-gnu/

# Volumes for source code and outputs
VOLUME ["/build/renpy", "/build/dist", "/build/tmp"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--help"]
