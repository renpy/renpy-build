Ren'Py Build
============

The purpose of the Ren'Py build system is to provide a single system that
can build the binary components of Ren'Py and all its dependencies, in
the same manner that is used to make official Ren'Py releases.

Requirements
-------------

Ren'Py Build requires a computer running Ubuntu 20.04. While it can run on
a desktop computer, portions of the build process must run at root, and the
whole process has security implications. My recommendation is to create a
virtual machine, install Ubuntu 20.04 on it, and run this procedure on
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


Preparing
---------

To get ready to build, log in as the rb user, and then run the following
command to clone renpy-build::

    git clone https://github.com/renpy/renpy-build

Change into the renpy-build directory, and run::

    ./prepare.sh

This will first install all the packages required to build Ren'Py, and
then it will clone Ren'Py and pygame_sdl2. It will also create a python
virtual environment with the tools in it. If this completes successfully,
you are ready to build.

Finally, a number of files need to be downloaded from third parties. These
are listed in tars/README.rst.

Building
---------

From the renpy-build directory, activate the virtualenv with the command::

    . tmp/virtualenv.py2/bin/activate

It should then be possible to build using the command::

    ./build.py

The build command can take some options:

`--platform <name>`
    The platform to build for. One of linux, windows, mac, android, or ios.

`--arch <name>`
    The architecture to build for. The architectures vary by platform,
    here is a copy of the table from build.py. ::

        Platform("linux", "x86_64")
        Platform("linux", "i686")
        Platform("linux", "armv7l")

        Platform("windows", "x86_64")
        Platform("windows", "i686")

        Platform("mac", "x86_64")

        Platform("android", "x86_64")
        Platform("android", "arm64_v8a")
        Platform("android", "armeabi_v7a")

        Platform("ios", "arm64")
        Platform("ios", "armv7s")
        Platform("ios", "x86_64")

A second build should be faster than the first, as it will only rebuild
Ren'Py, pygame_sdl2, and other components that are likely to frequently
change.

Updating
---------

It's possible to change renpy or pygame_sdl2 to be symlinks to your own
clones of those projects after the prepare step is complete. Updating
renpy-build itself may require deleting the tmp/ directory and a complete
rebuild, though simple changes may not require that.


