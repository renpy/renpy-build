import jinja2
import shlex
import subprocess
import sys
import sysconfig


def build_environment(c):
    """
    Sets up the build environment inside the context.
    """

    c.var("make", "nice make -j 12")

    c.var("sysroot", c.tmp / f"sysroot.{c.platform}-{c.arch}")
    c.var("build_platform", sysconfig.get_config_var("HOST_GNU_TYPE"))

    c.env("CPPFLAGS", "-I{{ install }}/include")
    c.env("CFLAGS", "-I{{ install }}/include")

    c.env("PATH", "{{ host }}/bin:{{ PATH }}")

    if (c.platform == "linux") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-pc-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "i686"):
        c.var("host_platform", "i686-pc-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "armv7l"):
        c.var("host_platform", "arm-linux-gnueabihf")
    elif (c.platform == "windows") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-w64-mingw32")
    elif (c.platform == "windows") and (c.arch == "i686"):
        c.var("host_platform", "i686-w64-mingw32")
    elif (c.platform == "mac") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-apple-darwin14")
    elif (c.platform == "android") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-linux-android")
    elif (c.platform == "android") and (c.arch == "arm64_v8a"):
        c.var("host_platform", "aarch64-linux-android")
    elif (c.platform == "android") and (c.arch == "armeabi_v7a"):
        c.var("host_platform", "armv7a-linux-androideabi")
    elif (c.platform == "ios") and (c.arch == "arm64"):
        c.var("host_platform", "arm-apple-darwin")
    elif (c.platform == "ios") and (c.arch == "armv7s"):
        c.var("host_platform", "arm-apple-darwin")
    elif (c.platform == "ios") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-apple-darwin")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.var("sdl_host_platform", "arm-ios-darwin11")
    elif (c.platform == "ios") and (c.arch == "armv7s"):
        c.var("sdl_host_platform", "arm-ios-darwin11")
    elif (c.platform == "ios") and (c.arch == "x86_64"):
        c.var("sdl_host_platform", "x86_64-ios-darwin11")
    else:
        c.var("sdl_host_platform", "{{ host_platform }}")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.var("ffi_host_platform", "aarch64-ios-darwin11")
    else:
        c.var("ffi_host_platform", "{{ host_platform }}")

    c.env("LDFLAGS", "-L{{install}}/lib")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "9.0")
    elif (c.platform == "ios") and (c.arch == "armv7s"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "9.0")

    if c.kind == "host":

        c.env("CC", "ccache gcc -fPIC")
        c.env("CXX", "ccache g++ -fPIC")
        c.env("CPP", "ccache gcc -E")
        c.env("LD", "ccache ld")
        c.env("AR", "ccache ar")
        c.env("RANLIB", "ccache ranlib")

        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")

    elif c.kind == "cross":

        if (c.platform == "mac") or (c.platform == "ios"):

            c.env("CC", "ccache clang")
            c.env("CXX", "ccache clang++")
            c.env("CPP", "ccache clang -E")
            c.env("LD", "ccache llvm-ld")
            c.env("AR", "ccache llvm-ar")
            c.env("RANLIB", "ccache llvm-ranlib")

            c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")

        else:

            c.env("CC", "ccache gcc -fPIC")
            c.env("CXX", "ccache g++ -fPIC")
            c.env("CPP", "ccache gcc -E")
            c.env("LD", "ccache ld")
            c.env("AR", "ccache ar")
            c.env("RANLIB", "ccache ranlib")

            c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")

    elif (c.platform == "linux") and (c.arch == "x86_64"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform}}-")

        c.env("CC", "ccache {{ crossbin }}gcc -m64 -O3 -fPIC -pthread --sysroot {{ sysroot }}")
        c.env("CXX", "ccache {{ crossbin }}g++ -m64 -O3 -fPIC -pthread --sysroot {{ sysroot }}")
        c.env("CPP", "ccache {{ crossbin }}gcc -m64 -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld -fPIC")
        c.env("AR", "ccache {{ crossbin }}gcc-ar")
        c.env("RANLIB", "ccache {{ crossbin }}gcc-ranlib")
        c.env("STRIP", "ccache {{ cross }}/bin/strip")
        c.env("NM", "{{ cross }}/bin/nm")

        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/lib/x86_64-linux-gnu")
        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/usr/lib/x86_64-linux-gnu")
        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/usr/lib/x86_64-linux-gnu/mesa")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")

    elif (c.platform == "linux") and (c.arch == "i686"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}-")

        c.env("CC", "ccache {{ crossbin }}gcc -m32 -fPIC -O3 -pthread --sysroot {{ sysroot }}")
        c.env("CXX", "ccache {{ crossbin }}g++ -m32 -fPIC -O3 -pthread --sysroot {{ sysroot }}")
        c.env("CPP", "ccache {{ crossbin }}gcc -m32 -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld -fPIC")
        c.env("AR", "ccache {{ crossbin }}gcc-ar")
        c.env("RANLIB", "ccache {{ crossbin }}gcc-ranlib")
        c.env("STRIP", "ccache {{ crossbin }}strip")
        c.env("NM", "{{ crossbin }}nm")

        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/lib/i386-linux-gnu")
        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/usr/lib/i386-linux-gnu")
        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/usr/lib/i386-linux-gnu/mesa")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{ sysroot }}/usr/lib/i386-linux-gnu -L{{install}}/lib32")

    elif (c.platform == "linux") and (c.arch == "armv7l"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}-")

        c.env("CC", "ccache {{ crossbin }}gcc -fPIC -O3 -pthread --sysroot {{ sysroot }}")
        c.env("CXX", "ccache {{ crossbin }}g++ -fPIC -O3 -pthread --sysroot {{ sysroot }}")
        c.env("CPP", "ccache {{ crossbin }}gcc -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld -fPIC")
        c.env("AR", "ccache {{ crossbin }}gcc-ar")
        c.env("RANLIB", "ccache {{ crossbin }}gcc-ranlib")
        c.env("STRIP", "ccache {{ crossbin }}strip")
        c.env("NM", "{{ crossbin }}nm")

        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/lib/arm-linux-gnueabihf")
        c.env("LDFLAGS", "{{ LDFLAGS }} -Wl,-rpath-link -Wl,{{ sysroot }}/usr/lib/arm-linux-gnueabihf")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{ sysroot }}/usr/lib/i386-linux-gnu -L{{install}}/lib32 ")

    elif (c.platform == "windows") and (c.arch == "x86_64"):

        c.var("crossbin", "/usr/bin/{{ host_platform }}-")

        c.env("CC", "ccache {{ crossbin }}gcc -fPIC -O3")
        c.env("CXX", "ccache {{ crossbin }}g++ -fPIC -O3")
        c.env("CPP", "ccache {{ crossbin }}gcc -E")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}gcc-ar")
        c.env("RANLIB", "ccache {{ crossbin }}gcc-ranlib")
        c.env("WINDRES", "ccache {{ crossbin }}windres")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "windows") and (c.arch == "i686"):

        c.var("crossbin", "/usr/bin/{{ host_platform }}-")

        c.env("CC", "ccache {{ crossbin }}gcc -fPIC -O3")
        c.env("CXX", "ccache {{ crossbin }}g++ -fPIC -O3")
        c.env("CPP", "ccache {{ crossbin }}gcc -E")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("WINDRES", "ccache {{ crossbin }}windres")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "mac") and (c.arch == "x86_64"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}-")

        c.env("MACOSX_DEPLOYMENT_TARGET", "10.6")

        c.env("CC", "ccache {{ crossbin }}clang -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossbin }}clang++ -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossbin }}clang -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "mac") and (c.arch == "x86_64"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}-")

        c.env("MACOSX_DEPLOYMENT_TARGET", "10.6")

        c.env("CC", "ccache {{ crossbin }}clang -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossbin }}clang++ -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossbin }}clang -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "android") and (c.arch == "x86_64"):

        c.var("crossbin", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/{{ host_platform }}-")
        c.var("crossclang", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/{{ host_platform }}21-")

        c.env("CC", "ccache {{ crossclang }}clang -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossclang }}clang++ -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossclang }}clang -E")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

    elif (c.platform == "android") and (c.arch == "arm64_v8a"):

        c.var("crossbin", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/{{ host_platform }}-")
        c.var("crossclang", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/{{ host_platform }}21-")

        c.env("CC", "ccache {{ crossclang }}clang -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossclang }}clang++ -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossclang }}clang -E")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

    elif (c.platform == "android") and (c.arch == "armeabi_v7a"):

        c.var("crossbin", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/arm-linux-androideabi-")
        c.var("crossclang", "{{ cross }}/android-ndk-r21d/toolchains/llvm/prebuilt/linux-x86_64/bin/{{ host_platform }}21-")

        c.env("CC", "ccache {{ crossclang }}clang -fPIC -O3 -pthread -fno-integrated-as")
        c.env("CXX", "ccache {{ crossclang }}clang++ -fPIC -O3 -pthread  -fno-integrated-as")
        c.env("CPP", "ccache {{ crossclang }}clang -E")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

    elif (c.platform == "ios") and (c.arch == "arm64"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}11-")

        c.env("CC", "ccache {{ crossbin }}clang -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossbin }}clang++ -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossbin }}clang -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "ios") and (c.arch == "armv7s"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}11-")

        c.env("CC", "ccache {{ crossbin }}clang -arch armv7s -mfpu=neon -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossbin }}clang++ -arch armv7s -mfpu=neon -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossbin }}clang -arch armv7s -mfpu=neon -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    elif (c.platform == "ios") and (c.arch == "x86_64"):

        c.var("crossbin", "{{ cross }}/bin/{{ host_platform }}11-")

        c.env("CC", "ccache {{ crossbin }}clang -arch x86_64 -fPIC -O3 -pthread")
        c.env("CXX", "ccache {{ crossbin }}clang++ -arch x86_64 -fPIC -O3 -pthread")
        c.env("CPP", "ccache {{ crossbin }}clang -arch x86_64 -E --sysroot {{ sysroot }}")
        c.env("LD", "ccache {{ crossbin}}ld")
        c.env("AR", "ccache {{ crossbin }}ar")
        c.env("RANLIB", "ccache {{ crossbin }}ranlib")
        c.env("STRIP", "ccache  {{ crossbin }}strip")
        c.env("NM", "{{ crossbin}}nm")

    c.env("PKG_CONFIG_PATH", "{{ install }}/lib/pkgconfig")
    c.env("PKG_CONFIG", "pkg-config --static")

    c.env("CFLAGS", "{{ CFLAGS }} -DRENPY_BUILD")

    if c.kind != "host":
        c.var("cross_config", "--host={{ host_platform }} --build={{ build_platform }}")
        c.var("sdl_cross_config", "--host={{ sdl_host_platform }} --build={{ build_platform }}")
        c.var("ffi_cross_config", "--host={{ ffi_host_platform }} --build={{ build_platform }}")


def run(command, context, verbose=False, quiet=False):
    args = shlex.split(command)

    if verbose:
        print(" ".join(shlex.quote(i) for i in args))

    if not quiet:
        p = subprocess.run(args, cwd=context.cwd, env=context.environ)
    else:
        with open("/dev/null", "w") as f:
            p = subprocess.run(args, cwd=context.cwd, env=context.environ, stdout=f, stderr=f)

    if p.returncode != 0:
        print(f"{context.task_name}: process failed with {p.returncode}.")
        print("args:", args)
        import traceback
        traceback.print_stack()
        sys.exit(1)
