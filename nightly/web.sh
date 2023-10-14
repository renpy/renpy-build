
# Link the documentation to the website.
pushd $BASE/renpy/dl
rm -Rf doc || true
ln -s current-8/doc doc
popd

# Upload the nightly build to the web.
pushd $BASE/renpy/dl

SSH="ssh"

# Upload the built distro to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" -a --info=progress2 /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly || true
fi

# Add symlinks.
$SCRIPTS/link_nightly.py /home/tom/magnetic/ab/WWW.nightly/


# Index the nightly.
$SCRIPTS/index_nightly.py /home/tom/magnetic/ab/WWW.nightly/

# Upload the index to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" -a --info=progress2 /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly --delete || true
fi

# Delete old nightlies.

if [ "$PRUNE" = 1 ]; then
    $SCRIPTS/prune_nightly.py /home/tom/magnetic/ab/WWW.nightly/
fi

popd
