#!/usr/bin/env python2.7

import os
import sys
if 'rapt' in sys.modules:
    del sys.modules['rapt']
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'buildlib'))

import argparse

import rapt.interface as interface
import rapt.install_sdk as install_sdk

def main():

    # Change into our root directory.
    ROOT = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(ROOT)

    # Parse the arguments.
    ap = argparse.ArgumentParser(description="Build an android package.")
    ap.add_argument("command", help="The command to run. Only installsdk is supported.")

    args = ap.parse_args()

    iface = interface.Interface()

    if args.command == "installsdk":
        install_sdk.install_sdk(iface)
    else:
        ap.error("Unknown command: " + args.command)


if __name__ == "__main__":
    main()
