Ren'Py-Build Concepts
=====================

The goal of Ren'Py-Build is to provide a program that manages the build of
Ren'Py on multiple machines. The primary goal is correctness, the secondary
goal is performance - minimizing the build time when little changes. It is
also intended to work without network filesystem support.

A *task* is a step in the build process. For example, a task might compile
a program or merge together libraries into a single file.

A *platform* is something that a build targets. This can be:

* An `os`-`architecture` combination, like linux-i686 or ios-armv7.
* An `os` alone, like linux or ios.
* A special name, like `master` that's used for tasks that aren't associated
  with a single target.

A *machine* is something that's capable of running tasks on a platform.
For now, there should be at most one machine running tasks for a platform,
but multiple platforms can be assigned to one machine. This represents a
conceptual machine, and you might have multiple Ren'Py-Build machines
assigned to a single physical machine, to allow portions of the build to
occur in parallel.

A *Join* operation waits for the machines for all of the platforms to be
idle. For example, this can be used to make sure that the platforms have
finished a build before copying the files to a central server to be
merged together.
