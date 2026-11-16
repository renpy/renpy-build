#!/usr/bin/env python3

"""
Determines whether a nightly build has the same major.minor version as the current Ren'Py release.

The nightly scripts use this to decide whether a build's documentation should be uploaded to the main
documentation location on renpy.org. It exits 0 if the versions match, and 1 if they do not, or if the current
release could not be determined.
"""

import argparse
import sys

import requests


CHANNELS_URL: str = "https://www.renpy.org/channels.json"
"The URL of the JSON file that lists the Ren'Py update channels and their versions."


def get_release_major_minor(url: str) -> tuple[int, int]:
    """
    Retrieves the channel list from `url`, and returns the (major, minor) version of the "Release" channel.

    Raises an exception if the list cannot be retrieved or parsed, or has no "Release" channel.
    """

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    for channel in response.json()["releases"]:
        if channel["channel"] == "Release":
            major, minor = channel["split_version"][:2]
            return int(major), int(minor)

    raise ValueError(f"No Release channel found in {url}.")


def get_version_major_minor(version: str) -> tuple[int, int]:
    """
    Returns the (major, minor) version from a version string like "8.6.1.26111601+nightly".
    """

    major, minor = version.split(".")[:2]
    return int(major), int(minor)


def main() -> None:
    ap = argparse.ArgumentParser(description="Exits 0 if the version has the same major.minor as the current release.")
    ap.add_argument("version", help="The version of the nightly build, like 8.6.1.26111601+nightly.")
    ap.add_argument("--url", default=CHANNELS_URL, help="The URL of channels.json.")

    args = ap.parse_args()

    try:
        build = get_version_major_minor(args.version)
        release = get_release_major_minor(args.url)
    except Exception as e:
        print(f"Could not compare {args.version} to the current release: {e!r}", file=sys.stderr)
        sys.exit(1)

    print(f"Build version: {build[0]}.{build[1]}, release version: {release[0]}.{release[1]}.")

    if build != release:
        sys.exit(1)


if __name__ == "__main__":
    main()
