#!/usr/bin/env python2.7

import os
import sys

RENIOS = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(RENIOS, 'buildlib'))

import argparse
import subprocess

import renios.interface as interface
import renios.create as create

def main():

    # Change into our root directory.
    ROOT = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ROOT)

    # Parse the arguments.
    ap = argparse.ArgumentParser(description="Set up an iOS application.")
    ap.add_argument("command", help="The command to run. One of init, ..., ... .")
    ap.add_argument("argument", nargs='*', help="The arguments to the selected command.")

    args = ap.parse_args()

    iface = interface.Interface()

    def check_args(n):
        if len(args.argument) != n:
            iface.fail("The {} command expects {} arguments.".format(args.command, n))

        return args.argument

    if args.command == "create":
        check_args(1)
        create.create_project(iface, args.argument[0])

    elif args.command == "test":
        iface.success("All systems go!")

    else:
        ap.error("Unknown command: " + args.command)

if __name__ == "__main__":
    main()

