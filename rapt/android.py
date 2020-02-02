#!/usr/bin/env python2.7

import sys
sys.path.insert(0, 'buildlib')

import os
import argparse
import subprocess
import pygame_sdl2

import rapt.interface as interface
import rapt.install_sdk as install_sdk
import rapt.configure as configure
import rapt.build as build
import rapt.plat as plat


def main():

    # Change into our root directory.
    ROOT = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ROOT)

    # Parse the arguments.
    ap = argparse.ArgumentParser(description="Build an android package.")
    ap.add_argument("command", help="The command to run. One of installsdk, configure, or build.")
    ap.add_argument("argument", nargs='*', help="The arguments to the selected command.")
    ap.add_argument("--launch", action="store_true", help="If true, launch the app when build completes.")

    args = ap.parse_args()

    iface = interface.Interface()

    def check_args(n):
        if len(args.argument) != n:
            iface.fail("The {} command expects {} arguments.".format(args.command, n))

        return args.argument

    if args.command == "installsdk":
        check_args(0)
        install_sdk.install_sdk(iface)

    elif args.command == "configure":
        directory, = check_args(1)
        configure.configure(iface, directory)

    elif args.command == "setconfig":
        directory, var, value = check_args(3)
        configure.set_config(iface, directory, var, value)

    elif args.command == "build":
        if len(args.argument) < 2:
            iface.fail("The build command expects at least 2 arguments.")

        build.build(iface, args.argument[0], args.argument[1:], launch=args.launch)

    elif args.command == "logcat":
        subprocess.call([ plat.adb, "logcat", "-s", "python:*"] + args.argument)

    elif args.command == "test":
        iface.success("All systems go!")

    else:
        ap.error("Unknown command: " + args.command)


if __name__ == "__main__":
    main()
