FROM renpy-build-base:latest

WORKDIR /build

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

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/build/renpy", "/build/dist", "/build/tmp"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--help"]
