Ren'Py Build
============

The purpose of the Ren'Py build system is to provide a single system that
can build the binary components of Ren'Py and all its dependencies, in
the same manner that is used to make official Ren'Py releases.

Requirements
-------------

Ren'Py Build requires a computer running Ubuntu 24.04. While it can run on
a desktop computer, portions of the build process must run at root, and the
whole process has security implications. My recommendation is to create a
virtual machine, install Ubuntu 24.04 on it, and run this procedure on
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
commands to instal git and clone renpy-build::

    sudo apt install git
    git clone https://github.com/renpy/renpy-build

Change into the renpy-build directory, and run prepare.sh::

    cd ~/renpy-build
    ./prepare.sh

**This will globally change your system.**  It will install packages from Ubuntu
and LLVM repositories, and the UV website. Please make sure you're comfortable with
this change before continuing.

This will first install all the packages required to build Ren'Py, and
then it will clone Ren'Py. It will also create a python
virtual environment with the tools in it. If this completes successfully,
you are ready to build.

Finally, a number of files need to be downloaded from third parties. These
are listed in `tars/README.rst <tars/README.rst>`_ .

Building
---------

You'll need to be in the renpy-build directory to build. If you're not, run::

    cd ~/renpy-build

It should then be possible to build using the command::

    ./build.sh

The build command can take some options:

`--platform <name>`
    The platform to build for. One of linux, windows, mac, android, ios, or web.

`--arch <name>`
    The architecture to build for. The architectures vary by platform,
    here is a copy of the table from build.py. ::


        Platform("linux", "x86_64")
        Platform("linux", "aarch64")

        Platform("windows", "x86_64")

        Platform("mac", "x86_64")
        Platform("mac", "arm64")

        Platform("android", "x86_64")
        Platform("android", "arm64_v8a")
        Platform("android", "armeabi_v7a")

        Platform("ios", "arm64")
        Platform("ios", "sim-x86_64")
        Platform("ios", "sim-arm64")

        Platform("web", "wasm")


A second build should be faster than the first, as it will only rebuild
Ren'Py and other components that are likely to frequently
change.

Cleaning
--------

To repeat part of a build without removing installed dependencies, use ``clean``
with a platform or architecture filter::

    ./build.sh clean --platform ios
    ./build.sh clean --platform ios --arch sim-arm64
    ./build.sh clean --arch x86_64

Filters can also appear before ``clean``. The plural aliases ``--platforms``
and ``--archs`` are supported, and each filter accepts comma-separated values.
If a filter is given both before and after ``clean``, the later value wins.
Platform and architecture filters are combined: architecture-specific state must
match both when both are supplied.

Filtered cleanup removes only matching task build directories in ``tmp/build``
and completion files in ``tmp/complete``, allowing those tasks to run again.
With an explicit platform filter, it also removes platform-wide build state,
even when an architecture filter is supplied. An architecture-only filter
preserves platform-wide state.

Host-wide and cross-toolchain build state is always preserved during filtered
cleanup. Sources, installed dependencies, SDKs, compilers, and generated or
packaged Ren'Py outputs are also preserved. If ``RENPY_BUILD_TMP`` is set, its
directory is used instead of ``tmp``.

Without either filter, ``./build.sh clean`` retains its full cleanup behavior:
it removes all task build directories and completion files, host tools,
unpacked sources, dependency installation directories, and the generated
``renpy/tmp/gen``, ``renpy/web``, ``renpy/renios``, and ``renpy/rapt``
directories. Cross-toolchain installation directories are not removed.

Run the cleanup regression tests with ``python -m unittest discover -s tests``
using a Python environment with the build system's dependencies installed.

Updating
---------

It's possible to change renpy/ to be a symlink to your own
clones of those projects after the prepare step is complete. Updating
renpy-build itself may require deleting the tmp/ directory and a complete
rebuild, though simple changes may not require that. You may also need to
run prepare.sh again.

iOS SDK Compatibility
---------------------

The iOS build uses SDL 3.4.18 with a downstream scene-orientation patch.
The current SDK inputs are iPhoneOS and iPhoneSimulator 27.1; the minimum
deployment target remains iOS 15.0. The SDK version used to compile an
application is distinct from the oldest iOS version it supports.

After changing the iOS support files or SDL patch, rebuild and package them::

    ./build.sh --platform ios rebuild sdl3 renios

This builds device arm64 and simulator arm64/x86_64 libraries and updates
``renpy/renios``. Do not use ``--sdl`` when validating a changed patch: that
option skips source unpacking and patch application. Rebuild invalidates
completion markers by task name, including matching markers for other platforms.

Create a new Xcode project with the launcher using the rebuilt iOS support.
New projects configure SDL's scene delegate in ``UIApplicationSceneManifest``.
The downstream SDL patch uses scene orientation and geometry updates, including
the period during launch when the orientation is not yet known. Native purchase
dialogs, review requests, and video use a foreground scene's application window.

Migrating Existing Xcode Projects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Update Xcode Project only refreshes game content in** ``base/``. It does not
update the native sources, prebuilt libraries, or ``Info.plist``. To migrate an
existing customized project:

1. Back up the project and create a fresh reference project using the rebuilt
   support package.
2. Merge the reference project's ``UIApplicationSceneManifest`` into the existing
   ``Info.plist``. It disables multiple scenes and configures
   ``SDLSceneConfiguration`` with ``SDLUIKitSceneDelegate`` for
   ``UIWindowSceneSessionRoleApplication``. Preserve app-specific plist values,
   supported orientations, and launch storyboard settings.
3. Merge changes to ``IAPHelper.m`` and ``VideoPlayer.m``, and include the new
   ``RenpyUIKit.h`` beside them. Preserve any custom native integrations.
4. Update the ``prebuilt/`` libraries from the reference project. Projects still
   using SDL2 need the SDL3 project/linker and entry-point changes as well;
   adding the scene manifest alone is not a migration from SDL2.
5. Compare the reference Xcode project's build settings and dependencies,
   including the iOS 15.0 deployment target. Clean and rebuild with Xcode 27.

Do not overwrite the entire plist or customized native sources without merging
their changes. Linux cross-builds and project-generation tests do not verify
UIKit launch or presentation behavior. Before shipping, test cold landscape
launch, rotation and touch alignment, background/resume, purchase dialogs,
review requests, and video on the target iOS runtimes, including older supported
versions. StoreKit controls whether a review prompt is actually shown.

Note
----

Support for unofficial builds of Ren'Py will be limited.
