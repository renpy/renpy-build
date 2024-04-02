Ren'Py Build
============

The purpose of the Ren'Py build system is to provide a single system that
can build the binary components of Ren'Py and all its dependencies, in
the same manner that is used to make official Ren'Py releases.

Requirements
-------------

Ren'Py Build requires a computer running Ubuntu 22.04. While it can run on
a desktop computer, portions of the build process must run at root, and the
whole process has security implications. My recommendation is to create a
virtual machine, install Ubuntu 22.04 on it, and run this procedure on
that machine.

The virtual machine must be provisioned with at least 64 GB of disk space.
I've compiled with 8 virtual CPUs and 16GB of RAM, though it may be possible
with less than that.

Setting up Ren'Py Build requires some Linux knowledge to complete.

I recommend dedicating a user to Ren'Py Build. In this example, I name the
user ``rb``, with a home directory of ``/home/rb``. Once that's done, you
will want to modify your computer so that user can use the ``sudo`` command
without a password. It's important that the username you chose does not have
a space in it.

That means first manually sudo-ing to root with the ``sudo -s`` command and
your user's password. Run the ``visudo`` command, and add the following line
to the bottom of the file:

    rb ALL = (ALL) NOPASSWD : ALL

Be sure to leave a blank line after it, then save the file with ctrl+X, and
use ``exit`` to get back to the non-root user. Note that this will allow
anyone who can log in as rb to become the superuser of this system.

There's also now a build system for building from FreeBSD 14.0. Consider this 
very experimental. It hasn't been fully tested with building for the other 
platforms but at least Linux should build fine without too many issues. 
Steam is not natively supported on that platform, so Steamworks support 
probably will not work at this time.

Preparing
---------

To get ready to build, log in as the rb user, and then run the following
commands to instal git and clone renpy-build::

    sudo apt install git
    git clone https://github.com/renpy/renpy-build

Change into the renpy-build directory, and run prepare.sh (for Ubuntu) or 
prepare-freebsd.sh (for FreeBSD)::

    cd ~/renpy-build
    ./prepare.sh

**This will globally change your system.**  It will install packages from Ubuntu
and LLVM repositories. Please make sure you're comfortable with
this change before continuing.

**For FreeBSD:** it will install comparible packages to those used in Ubuntu but 
will also download and build sysroot jails for compiling FreeBSD native libraries 
and binaries. Each of these will add around 2 GB to your hard drive space 
requirements. These will be comparible to the sysroot jails used by Ubuntu to 
build the engine. They also will be briefly owned by root during creation (this 
is required for pkg to install the extra tools needed). When finished, permissions 
will be reverted back. See `tasks/toolchain_freebsd.py` to see how it works.

This will first install all the packages required to build Ren'Py, and
then it will clone Ren'Py and pygame_sdl2. It will also create a python
virtual environment with the tools in it. If this completes successfully,
you are ready to build.

Finally, a number of files need to be downloaded from third parties. These
are listed in `tars/README.rst <tars/README.rst>`_ .

Building
---------

You'll need to be in the renpy-build directory to build. If you're not, run::

    cd ~/renpy-build

From the renpy-build directory, activate the virtualenv with the command::

    . tmp/virtualenv.py3/bin/activate

It should then be possible to build using the command::

    ./build.py

The build command can take some options:

`--python <version>`
    The python version to build. Can be "3" or "2", defaults to 3.

`--platform <name>`
    The platform to build for. One of linux, windows, mac, freebsd, android, ios, or web.

`--arch <name>`
    The architecture to build for. The architectures vary by platform,
    here is a copy of the table from build.py. ::

        # Python 2

        Platform("linux", "x86_64", "2")
        Platform("linux", "i686", "2")
        Platform("linux", "aarch64", "2")
        Platform("linux", "armv7l", "2")

        Platform("windows", "x86_64", "2")
        Platform("windows", "i686", "2")

        Platform("mac", "x86_64", "2")
        Platform("mac", "arm64", "2")

        Platform("android", "x86_64", "2")
        Platform("android", "arm64_v8a", "2")
        Platform("android", "armeabi_v7a", "2")

        Platform("ios", "arm64", "2")
        Platform("ios", "sim-x86_64", "2")
        Platform("ios", "sim-arm64", "2")

        Platform("web", "wasm", "2")

        Platform("freebsd", "x86_64", "2", experimental=True)
        Platform("freebsd", "i686", "2", experimental=True)


        # Python 3

        Platform("linux", "x86_64", "3")
        Platform("linux", "aarch64", "3")
        Platform("linux", "armv7l", "3")

        Platform("windows", "x86_64", "3")

        Platform("mac", "x86_64", "3")
        Platform("mac", "arm64", "3")

        Platform("android", "x86_64", "3")
        Platform("android", "arm64_v8a", "3")
        Platform("android", "armeabi_v7a", "3")

        Platform("ios", "arm64", "3")
        Platform("ios", "sim-x86_64", "3")
        Platform("ios", "sim-arm64", "3")

        Platform("web", "wasm", "3", experimental=True)

        Platform("freebsd", "x86_64", "3", experimental=True)
        Platform("freebsd", "i686", "3", experimental=True)

    `--experimental`
        This builds platforms marked as experimental.

A second build should be faster than the first, as it will only rebuild
Ren'Py, pygame_sdl2, and other components that are likely to frequently
change.

Updating
---------

It's possible to change renpy or pygame_sdl2 to be symlinks to your own
clones of those projects after the prepare step is complete. Updating
renpy-build itself may require deleting the tmp/ directory and a complete
rebuild, though simple changes may not require that. You may also need to
run prepare.sh again.

Note
----

Support for unofficial builds of Ren'Py will be limited.
