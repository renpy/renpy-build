# Upload the nightly build to the web.

pushd $BASE/renpy/dl

rm current
ln -s "$RENPY_NIGHTLY" current

rm renpy-nightly-sdk.zip
rm renpy-nightly-sdk.tar.bz2
ln -s current/renpy-*-sdk.zip renpy-nightly-sdk.zip
ln -s current/renpy-*-sdk.tar.bz2 renpy-nightly-sdk.tar.bz2

# Index the nightly.
$SCRIPTS/index_nightly.py /home/tom/magnetic/ab/WWW.nightly/

# Upload everything to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -av /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly --delete
fi

# Delete old nightlies.

if [ "$PRUNE" = 1 ]; then
    find /home/tom/magnetic/ab/WWW.nightly/ -ctime +30.5 -delete || true
fi

popd
