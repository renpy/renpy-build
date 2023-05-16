
# Copy the documentation to the website.
rm -Rf $BASE/renpy/dl/doc || true
cp -a $BASE/renpy/doc-web $BASE/renpy/dl/doc

# Upload the nightly build to the web.
pushd $BASE/renpy/dl

SSH="ssh"

# Upload the built distro to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" --progress -av /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly
fi

# Add symlinks.
$SCRIPTS/link_nightly.py /home/tom/magnetic/ab/WWW.nightly/


# Index the nightly.
$SCRIPTS/index_nightly.py /home/tom/magnetic/ab/WWW.nightly/

# Upload the index to the server.
if [ "$UPLOAD" = 1 ]; then
    rsync -e "$SSH" --progress -av /home/tom/magnetic/ab/WWW.nightly/ tom@abagail.onegeek.org:/home/tom/WWW.nightly --delete
fi

# Delete old nightlies.

if [ "$PRUNE" = 1 ]; then
    $SCRIPTS/prune_nightly.py /home/tom/magnetic/ab/WWW.nightly/
fi

popd
