# Figure out a reasonable version name.
export RENPY_7_NIGHTLY="7-nightly-$(date +%Y-%m-%d)"
export RENPY_8_NIGHTLY="8-nightly-$(date +%Y-%m-%d)"

# Capture current renpy revision.
pushd $BASE/renpy
RENPY_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)
popd

# Capture current pygame_sdl2 revision.
pushd $BASE/pygame_sdl2
PYGAME_SDL2_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)
popd

# Capture current renpyweb revision.
pushd $BASE/renpyweb
RENPYWEB_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)
popd

pushd $BASE

# Capture current renpy-build revision.
RENPY_BUILD_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)

# Write revisions to file, renpy-build should always be last.
cat > tmp/vcs7.json <<-EOF
[
  ["renpy",       $RENPY_REV],
  ["pygame_sdl2", $PYGAME_SDL2_REV],
  ["renpyweb",    $RENPYWEB_REV],
  ["renpy-build", $RENPY_BUILD_REV]
]
EOF

cat > tmp/vcs8.json <<-EOF
[
  ["renpy",       $RENPY_REV],
  ["pygame_sdl2", $PYGAME_SDL2_REV],
  ["renpy-build", $RENPY_BUILD_REV]
]
EOF


popd
