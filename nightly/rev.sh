pushd $BASE/renpy

# Figure out a reasonable version name.
REV=$(git rev-parse --short HEAD)
BRANCH=$(git rev-parse --abbrev-ref HEAD)

export RENPY_7_NIGHTLY="7-nightly-$(date +%Y-%m-%d)-$REV"
export RENPY_8_NIGHTLY="8-nightly-$(date +%Y-%m-%d)-$REV"

popd
