Extensions
==========

The renpy-build system supports compiling C extensions, and including them
with the Ren'Py binary. This is intended to support your own C extensions,
rather than arbitrary third-party extensions.

The extensions are included into the Ren'Py binaries build for Windows,
macOS, Linux, Android, and iOS. (But not the web.) The extensions built
this way are loaded in the same way Ren'Py and pygame_sdl2 modules are.

Step 0
------

If your module is written in cython you'll need to mantually run cython
to turn it into a C file.

Step 1
------

Place the C file in this directory. Multiple C files can be used to create
a single extension.

Step 2
------

Edit Setup to add a line for your extension. The lines are::

    sample_extension sample_extension.c

Where the first thing is the extension name, and the rest of it are files
that are linked into the extension.

Step 3
------

Run renpy-build, as described in the main renpy-build README. Post-build,
the module can be imported with the import statement, eg., ``import sample_extension``.

The modules are rebuilt each time renpy-build is run.
