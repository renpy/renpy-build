# Upload the nightly build to the web.

pushd $BASE/renpy/dl

SSH="ssh"

# Upload the built distro to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" --progress -av /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly
fi

# Index the nightly.
$SCRIPTS/index_nightly.py /home/tom/magnetic/ab/WWW.nightly/

rm current
ln -s "$RENPY_7_NIGHTLY" current
ln -s "$RENPY_7_NIGHTLY" current-7
ln -s "$RENPY_8_NIGHTLY" current-8

rm renpy-nightly-sdk.zip
rm renpy-nightly-sdk.tar.bz2
ln -s current/renpy-*-sdk.zip renpy-nightly-sdk.zip
ln -s current/renpy-*-sdk.tar.bz2 renpy-nightly-sdk.tar.bz2

# Upload the index to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" --progress -av /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly --delete
fi

# Delete old nightlies.

if [ "$PRUNE" = 1 ]; then
    find /home/tom/magnetic/ab/WWW.nightly/ -ctime +30.5 -delete || true
fi

popd
