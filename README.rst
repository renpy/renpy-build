Ren'Py Build
============

The purpose of the Ren'Py build system is to provide a single system that
can build the binary components of Ren'Py and all its dependencies, in
the same manner that is used to make official Ren'Py releases.

Requirements
------------

- Python 3.12 or newer (available as ``python3`` in your PATH)
- `Podman <https://podman.io/docs/installation>`_ (with ``podman compose``)
- Git
- At least **64 GB** of free disk space
- Recommended: 8 CPU cores, 16 GB RAM

Quick Start
-----------

Clone this repository and the Ren'Py source::

    git clone https://github.com/renpy/renpy-build
    cd renpy-build
    git clone https://github.com/renpy/renpy

Download the required third-party archives listed in `tars/README.rst
<tars/README.rst>`_ and place them in the ``tars/`` directory.

Then build::

    ./run.sh build

On Windows, use ``run.ps1`` instead of ``run.sh``::

    .\run.ps1 build

This will:

1. Build the container image (first run only).
2. Run the full Ren'Py build inside the container.

Subsequent builds reuse the image and only rebuild components that changed.

Build Options
~~~~~~~~~~~~~

Options are passed before the ``build`` command::

    ./run.sh --platform linux --arch x86_64 build

``--platform <name>``
    The platform to build for. One of ``linux``, ``windows``, ``mac``,
    ``android``, ``ios``, or ``web``.

``--arch <name>``
    The architecture to build for. See the table below.

``--nostrip``
    Do not strip binaries.

``--experimental``
    Include experimental platforms.

``--stop <task>``
    Stop after the specified task.

Supported Platform / Architecture Combinations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Platform
     - Architecture
   * - linux
     - x86_64
   * - linux
     - aarch64
   * - windows
     - x86_64
   * - mac
     - x86_64
   * - mac
     - arm64
   * - android
     - x86_64
   * - android
     - arm64_v8a
   * - android
     - armeabi_v7a
   * - ios
     - arm64
   * - ios
     - sim-x86_64
   * - ios
     - sim-arm64
   * - web
     - wasm

Cleaning
~~~~~~~~

To perform a clean build, run::

    ./run.sh clean

Advanced Usage
--------------

Container Management
~~~~~~~~~~~~~~~~~~~~

``--no-cache``
    Rebuild the container image from scratch, ignoring the cache.

``--dry-run``
    Print the ``podman`` command that would be executed without running it.

Running Commands in the Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can run an arbitrary command (default: ``bash``) inside the build
container::

    ./run.sh exec
    ./run.sh exec ls /build

Exporting and Importing the Build Volume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The build state lives in a Podman volume. You can export it to a tarball
and re-import it later (e.g. to share a partial build)::

    ./run.sh export renpy-build-tmp.tar
    ./run.sh import renpy-build-tmp.tar

Developer Mode
~~~~~~~~~~~~~~

.. note::

   Dev mode is intended for people working on renpy-build itself, not for
   building Ren'Py from source.

Dev mode mounts the renpy-build source directories into the container so
that changes to build tasks and scripts are reflected without rebuilding
the image::

    ./run.sh --dev --platform linux build

Note
----

Support for unofficial builds of Ren'Py will be limited.
