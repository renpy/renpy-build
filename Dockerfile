FROM ubuntu:20.04

RUN echo "Updating Repos"; apt update

RUN echo "Installing sudo to allow scripts to work"; apt-get install -y sudo

RUN echo "Making renpy_build directory"; mkdir /renpy-build

# Needed to build things.
RUN apt-get install -y git build-essential ccache python-dev-is-python2 python3-dev unzip

# Needed to install python2 pip
RUN apt-get install -y curl

# Needed by renpy-build itself.
RUN apt-get install -y python3-jinja2

# Needed by sysroot.
RUN apt-get install -y debootstrap qemu-user-static

# Needed by gcc.
RUN apt-get install -y libgmp-dev libmpfr-dev libmpc-dev

# Needed by hostpython.
RUN apt-get install -y libssl-dev libbz2-dev

# Needed for windows.
RUN apt-get install -y mingw-w64 autoconf

# Needed for mac
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cmake clang libxml2-dev llvm

# Needed for web
RUN apt-get install -y quilt

# Install the standard set of packages needed to build Ren'Py.
RUN apt-get install -y \
    python-dev-is-python2 libavcodec-dev libavformat-dev \
    libavresample-dev libswresample-dev libswscale-dev libfreetype6-dev libglew1.6-dev \
    libfribidi-dev libsdl2-dev libsdl2-image-dev libsdl2-gfx-dev \
    libsdl2-mixer-dev libsdl2-ttf-dev libjpeg-turbo8-dev

# Add clang to the image itself
COPY "prebuilt/clang_rt.tar.gz" /tmp/clang_rt.tar.gz

RUN tar xzf "/tmp/clang_rt.tar.gz" -C /usr/lib/clang/10/lib/

RUN rm /tmp/clang_rt.tar.gz

RUN useradd --uid 1000 -m "rb"

# add rb to the sudoers so scripts will run
RUN printf "rb ALL = (ALL) NOPASSWD : ALL\n" >> /etc/sudoers.d/rb

USER rb

RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o /tmp/get-pip.py

RUN sudo python2 /tmp/get-pip.py

RUN pip2 install virtualenv

CMD "/usr/bin/bash"

