# Building with Docker
TODO

# Building with Podman
Building using containers makes it easier to create and tear down the build environment.
Currently only Podman is tested though it may work on Docker.
Though, running Docker on Windows will most likely not work.

The end goal of this container is to give you a bash shell that you can use to run the build commands.
This way you can easily tear down the build environment and reproduce it.

## Mounts
This container should be ran with a volume mount to your renpy-build directory.
This can be done using the `-v` parameter.

## Caviats
In podman you can not build renpy under an unprivlaged rootless container.
To build renpy with podman and use your local repos, the image must be built as root.
Remember to change the UID for the container user to match your non root user to allow volume mounts.

## Building with Podman
This is an example of a typical build path process.

```
# podman build -t renpy_build .

"This runs the container and drops you into a shell as the rb user with renpy-build mounted"
# podman run --name renpy_build -i --privileged -v /path/to/renpy-build/:/renpy-build -t renpy_build /bin/bash

$ cd renpy-build

$ ./prepare.sh

$ source tmp/virtualenv.py2/bin/activate

"Build for linux x86_64"
$ ./build.py --arch x86_64 --platform linux
```

Once your build is done you can find the output in the path that you mounted.
