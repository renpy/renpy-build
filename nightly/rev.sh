# Capture current renpy revision.
pushd $BASE/renpy
RENPY_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)
popd

pushd $BASE

# Capture current renpy-build revision.
RENPY_BUILD_REV=$(git log -n1 --pretty='"%H", "%h"' HEAD)

cat > tmp/vcs8.json <<-EOF
[
  ["renpy",       $RENPY_REV],
  ["renpy-build", $RENPY_BUILD_REV]
]
EOF


popd
