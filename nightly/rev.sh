pushd $BASE/renpy

# Figure out a reasonable version name.
REV=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

export RENPY_NIGHTLY="nightly-$(date +%Y-%m-%d)-$REV"

popd

