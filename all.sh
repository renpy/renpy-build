#!/bin/bash

set -e

./build.py --platform linux --arch x86_64 "$@"
./build.py --platform linux --arch i686 "$@"
./build.py --platform linux --arch armhf "$@"

./build.py --platform windows --arch x86_64 "$@"
./build.py --platform windows --arch i686 "$@"

./build.py --platform mac --arch x86_64 "$@"

