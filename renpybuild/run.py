import os
import re
import shlex
import subprocess
import sys
import sysconfig

import jinja2

# This caches the results of emsdk_environment.
emsdk_cache : dict[str, str] = { }

def emsdk_environment(c):
    """
    Loads the emsdk environment into `c`.
    """

    emsdk = c.path("{{ cross }}/emsdk")

    if not emsdk.exists():
        return

    if not emsdk_cache:

        env = dict(os.environ)
        env["EMSDK_BASH"] = "1"
        env["EMSDK_QUIET"] = "1"

        bash = subprocess.check_output([ str(emsdk), "construct_env" ], env=env, text=True)

        for l in bash.split("\n"):
            m = re.match(r'export (\w+)=\"(.*?)\";?$', l)
            if m:
                emsdk_cache[m.group(1)] = m.group(2)

    for k, v in emsdk_cache.items():
        c.env(k, v)


def llvm(c, bin="", prefix="", suffix="-15", clang_args="", use_ld=True):

    if bin:
        c.env("PATH", bin + ":{{ PATH }}")
        if not bin.endswith("/"):
            bin += "/"

    c.var("llvm_bin", bin)
    c.var("llvm_prefix", prefix)
    c.var("llvm_suffix", suffix)

    ld = c.expand("{{llvm_bin}}lld{{llvm_suffix}}")

    if use_ld:
        if c.platform == "linux":
            clang_args = "-fuse-ld=" + ld + " -Wno-unused-command-line-argument " + clang_args
        else:
            clang_args = "-fuse-ld=lld -Wno-unused-command-line-argument " + clang_args

    if c.platform == "ios":
        c.var("cxx_clang_args", "-stdlib=libc++ -I{{cross}}/sdk/usr/include/c++")
    elif c.platform == "mac" or c.platform == "ios":
        c.var("cxx_clang_args", "-stdlib=libc++")
    else:
        c.var("cxx_clang_args", "")

    c.var("clang_args", clang_args)

    c.env("CC", "ccache {{llvm_bin}}{{llvm_prefix}}clang{{llvm_suffix}} {{ clang_args }} -std=gnu17")
    c.env("CXX", "ccache {{llvm_bin}}{{llvm_prefix}}clang++{{llvm_suffix}} {{ clang_args }} -std=gnu++17 {{ cxx_clang_args }}")
    c.env("CPP", "ccache {{llvm_bin}}{{llvm_prefix}}clang{{llvm_suffix}} {{ clang_args }} -E")

    # c.env("LD", "ccache " + ld)
    c.env("AR", "ccache {{llvm_bin}}llvm-ar{{llvm_suffix}}")
    c.env("RANLIB", "ccache {{llvm_bin}}llvm-ranlib{{llvm_suffix}}")
    c.env("STRIP", "ccache {{llvm_bin}}llvm-strip{{llvm_suffix}}")
    c.env("NM", "ccache {{llvm_bin}}llvm-nm{{llvm_suffix}}")
    c.env("READELF", "ccache {{llvm_bin}}llvm-readelf{{llvm_suffix}}")

    c.env("WINDRES", "{{llvm_bin}}{{llvm_prefix}}windres{{llvm_suffix}}")

    if c.platform == "windows":
        c.env("RC", "{{WINDRES}}")

def android_llvm(c, arch):

    if arch == "armv7a":
        eabi = "eabi"
    else:
        eabi = ""

    llvm(
        c,
        bin="{{cross}}/{{ndk_version}}/toolchains/llvm/prebuilt/linux-x86_64/bin",
        prefix=f"{arch}-linux-android{ eabi }21-",
        suffix="",
        clang_args="",
        use_ld=False,
    )

def build_environment(c):
    """
    Sets up the build environment inside the context.
    """

    if c.platform == "web" and c.kind not in ( "host",  "host-python", "cross" ):
        emsdk_environment(c)

    if c.platform == "android":
        c.var("ndk_version", "android-ndk-r25c")

    cpuccount = os.cpu_count()

    if cpuccount is None:
        cpuccount = 4

    if cpuccount > 12:
        cpuccount -= 4

    c.var("make", "nice make -j " + str(cpuccount))
    c.var("configure", "./configure")
    c.var("cmake", "cmake")

    c.var("meson_configure", "meson setup")
    c.var("meson_compile", "meson compile -j " + str(cpuccount))

    c.var("sysroot", c.tmp / f"sysroot.{c.platform}-{c.arch}")
    c.var("build_platform", sysconfig.get_config_var("HOST_GNU_TYPE"))

    c.env("CPPFLAGS", "-I{{ install }}/include")
    c.env("CFLAGS", "-O3 -I{{ install }}/include")
    c.env("LDFLAGS", "-O3 -L{{install}}/lib")

    c.env("PATH", "{{ host }}/bin:{{ PATH }}")

    if (c.platform == "linux") and (c.arch == "x86_64"):
        c.var("host_platform", "x86_64-pc-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "aarch64"):
        c.var("host_platform", "aarch64-pc-linux-gnu")
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
    elif (c.platform == "mac") and (c.arch == "arm64"):
        c.var("host_platform", "arm-apple-darwin21.6.0")
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
    elif (c.platform == "ios") and (c.arch == "sim-arm64"):
        c.var("host_platform", "arm-apple-darwin")
    elif (c.platform == "ios") and (c.arch == "sim-x86_64"):
        c.var("host_platform", "x86_64-apple-darwin")
    elif (c.platform == "web") and (c.arch == "wasm"):
        c.var("host_platform", "wasm32-unknown-emscripten")

    if (c.platform == "linux") and (c.arch == "x86_64"):
        c.var("architecture_name", "x86_64-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "aarch64"):
        c.var("architecture_name", "aarch64-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "i686"):
        c.var("architecture_name", "i386-linux-gnu")
    elif (c.platform == "linux") and (c.arch == "armv7l"):
        c.var("architecture_name", "arm-linux-gnueabihf")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.var("sdl_host_platform", "arm-ios-darwin21")
    elif (c.platform == "ios") and (c.arch == "armv7s"):
        c.var("sdl_host_platform", "arm-ios-darwin21")
    elif (c.platform == "ios") and (c.arch == "sim-arm64"):
        c.var("sdl_host_platform", "arm-ios-darwin21")
    elif (c.platform == "ios") and (c.arch == "sim-x86_64"):
        c.var("sdl_host_platform", "x86_64-ios-darwin21")
    else:
        c.var("sdl_host_platform", "{{ host_platform }}")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.var("ffi_host_platform", "aarch64-ios-darwin21")
    elif (c.platform == "ios") and (c.arch == "sim-arm64"):
        c.var("ffi_host_platform", "aarch64-ios-darwin21")
    elif (c.platform == "mac") and (c.arch == "arm64"):
        c.var("ffi_host_platform", "aarch64-apple-darwin21.6.0")
    else:
        c.var("ffi_host_platform", "{{ host_platform }}")

    if (c.platform == "ios") and (c.arch == "arm64"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "13.0")
    elif (c.platform == "ios") and (c.arch == "armv7s"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "13.0")
    elif (c.platform == "ios") and (c.arch == "sim-arm64"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "13.0")
    elif (c.platform == "ios") and (c.arch == "sim-x86_64"):
        c.env("IPHONEOS_DEPLOYMENT_TARGET", "13.0")

    c.var("lipo", "llvm-lipo-15")


    if c.kind == "host" or c.kind == "host-python" or c.kind == "cross":

        llvm(c)
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")
        c.env("PKG_CONFIG_PATH", "{{ install }}/lib/pkgconfig")

        # c.var("cmake_system_name", "Linux")
        # c.var("cmake_system_processor", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH={{ install }}")

    elif (c.platform == "linux") and (c.arch == "x86_64"):

        llvm(c, clang_args="-target {{ host_platform }} --sysroot {{ sysroot }} -fPIC -pthread")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")
        c.env("PKG_CONFIG_LIBDIR", "{{ sysroot }}/usr/lib/{{ architecture_name }}/pkgconfig:{{ sysroot }}/usr/share/pkgconfig")
        # c.env("PKG_CONFIG_SYSROOT_DIR", "{{ sysroot }}")

        c.var("cmake_system_name", "Linux")
        c.var("cmake_system_processor", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ sysroot }}' -DCMAKE_SYSROOT={{ sysroot }}")

        c.var("meson_cross_system", "linux")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "x86_64")
        c.var("meson_cross_cpu", "x86_64")

    elif (c.platform == "linux") and (c.arch == "aarch64"):

        llvm(c, clang_args="-target {{ host_platform }} --sysroot {{ sysroot }} -fPIC -pthread")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib64")
        c.env("PKG_CONFIG_LIBDIR", "{{ sysroot }}/usr/lib/{{ architecture_name }}/pkgconfig:{{ sysroot }}/usr/share/pkgconfig")
        # c.env("PKG_CONFIG_SYSROOT_DIR", "{{ sysroot }}")

        c.var("cmake_system_name", "Linux")
        c.var("cmake_system_processor", "aarch64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ sysroot }}' -DCMAKE_SYSROOT={{ sysroot }}")

        c.var("meson_cross_system", "linux")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "aarch64")
        c.var("meson_cross_cpu", "aarch64")

    elif (c.platform == "linux") and (c.arch == "i686"):

        llvm(c, clang_args="-target {{ host_platform }} --sysroot {{ sysroot }} -fPIC -pthread")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib32")
        c.env("PKG_CONFIG_LIBDIR", "{{ sysroot }}/usr/lib/{{ architecture_name }}/pkgconfig:{{ sysroot }}/usr/share/pkgconfig")
        # c.env("PKG_CONFIG_SYSROOT_DIR", "{{ sysroot }}")

        c.var("cmake_system_name", "Linux")
        c.var("cmake_system_processor", "i386")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ sysroot }}' -DCMAKE_SYSROOT={{ sysroot }}")

        c.var("meson_cross_system", "linux")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "x86")
        c.var("meson_cross_cpu", "i686")

    elif (c.platform == "linux") and (c.arch == "armv7l"):

        llvm(c, clang_args="-target {{ host_platform }} --sysroot {{ sysroot }} -fPIC -pthread -mfpu=neon -mfloat-abi=hard")
        c.env("LDFLAGS", "{{ LDFLAGS }} -L{{install}}/lib32")
        c.env("PKG_CONFIG_LIBDIR", "{{ sysroot }}/usr/lib/{{ architecture_name }}/pkgconfig:{{ sysroot }}/usr/share/pkgconfig")
        # c.env("PKG_CONFIG_SYSROOT_DIR", "{{ sysroot }}")

        c.var("cmake_system_name", "Linux")
        c.var("cmake_system_processor", "armv7")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ sysroot }}' -DCMAKE_SYSROOT={{ sysroot }}")

        c.var("meson_cross_system", "linux")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "arm")
        c.var("meson_cross_cpu", "armhf")

    elif (c.platform == "windows") and (c.arch == "x86_64"):

        llvm(
            c,
            bin="{{ cross }}/llvm-mingw/bin",
            prefix="x86_64-w64-mingw32-",
            suffix="",
            clang_args="-target {{ host_platform }} --sysroot {{ cross }}/llvm-mingw/x86_64-w64-mingw32 -fPIC -pthread",
            use_ld=False)

        c.var("cmake_system_name", "Windows")
        c.var("cmake_system_processor", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/llvm-mingw/x86_64-w64-mingw32' -DCMAKE_SYSROOT={{ cross }}/llvm-mingw/x86_64-w64-mingw32")

        c.var("meson_cross_system", "windows")
        c.var("meson_cross_kernel", "nt")
        c.var("meson_cross_cpu_family", "x86_64")
        c.var("meson_cross_cpu", "x86_64")

    elif (c.platform == "windows") and (c.arch == "i686"):

        llvm(
            c,
            bin="{{ cross }}/llvm-mingw/bin",
            prefix="i686-w64-mingw32-",
            suffix="",
            clang_args="-target {{ host_platform }} --sysroot {{ cross }}/llvm-mingw/i686-w64-mingw32 -fPIC -pthread",
            use_ld=False)

        c.var("cmake_system_name", "Windows")
        c.var("cmake_system_processor", "i386")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/llvm-mingw/i686-w64-mingw32' -DCMAKE_SYSROOT={{ cross }}/llvm-mingw/i686-w64-mingw32")

        c.var("meson_cross_system", "windows")
        c.var("meson_cross_kernel", "nt")
        c.var("meson_cross_cpu_family", "x86")
        c.var("meson_cross_cpu", "i686")

    elif (c.platform == "android") and (c.arch == "x86_64"):

        android_llvm(c, "x86_64")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

        c.var("cmake_system_name", "Android")
        c.var("cmake_system_processor", "x86_64")
        c.var("android_abi", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH={{ install }} -DCMAKE_TOOLCHAIN_FILE={{cross}}/{{ndk_version}}/build/cmake/android.toolchain.cmake -DANDROID_ABI={{ android_abi }} -DANDROID_PLATFORM=android-21 -DANDROID_USE_LEGACY_TOOLCHAIN_FILE=OFF")

        c.var("meson_cross_system", "android")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "x86_64")
        c.var("meson_cross_cpu", "x86_64")

    elif (c.platform == "android") and (c.arch == "arm64_v8a"):

        android_llvm(c, "aarch64")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

        c.var("cmake_system_name", "Android")
        c.var("cmake_system_processor", "aarch64")
        c.var("android_abi", "arm64-v8a")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH={{ install }} -DCMAKE_TOOLCHAIN_FILE={{cross}}/{{ndk_version}}/build/cmake/android.toolchain.cmake -DANDROID_ABI={{ android_abi }} -DANDROID_PLATFORM=android-21 -DANDROID_USE_LEGACY_TOOLCHAIN_FILE=OFF")

        c.var("meson_cross_system", "android")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "aarch64")
        c.var("meson_cross_cpu", "aarch64")

    elif (c.platform == "android") and (c.arch == "armeabi_v7a"):

        android_llvm(c, "armv7a")

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED")

        c.var("cmake_system_name", "Android")
        c.var("cmake_system_processor", "armv7-a")
        c.var("android_abi", "armeabi-v7a")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH={{ install }} -DCMAKE_TOOLCHAIN_FILE={{cross}}/{{ndk_version}}/build/cmake/android.toolchain.cmake -DANDROID_ABI={{ android_abi }} -DANDROID_PLATFORM=android-21 -DANDROID_USE_LEGACY_TOOLCHAIN_FILE=OFF")

        c.var("meson_cross_system", "android")
        c.var("meson_cross_kernel", "linux")
        c.var("meson_cross_cpu_family", "arm")
        c.var("meson_cross_cpu", "armv7")

    elif (c.platform == "mac") and (c.arch == "x86_64"):

        llvm(
            c,
            clang_args="-target x86_64-apple-darwin14 --sysroot {{cross}}/sdk",
        )

        c.env("MACOSX_DEPLOYMENT_TARGET", "10.10")
        c.env("CFLAGS", "{{ CFLAGS }} -mmacos-version-min=10.10")
        c.env("LDFLAGS", "{{ LDFLAGS }} -mmacos-version-min=10.10")

        c.var("cmake_system_name", "Darwin")
        c.var("cmake_system_processor", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/sdk' -DCMAKE_SYSROOT={{ cross }}/sdk")

        c.var("meson_cross_system", "darwin")
        c.var("meson_cross_subsystem", "macos")
        c.var("meson_cross_kernel", "xnu")
        c.var("meson_cross_cpu_family", "x86_64")
        c.var("meson_cross_cpu", "x86_64")

    elif (c.platform == "mac") and (c.arch == "arm64"):

        llvm(
            c,
            clang_args="-target arm64-apple-macos11 --sysroot {{cross}}/sdk",
        )

        c.env("MACOSX_DEPLOYMENT_TARGET", "11.0")
        c.env("CFLAGS", "{{ CFLAGS }} -mmacos-version-min=11.0")
        c.env("LDFLAGS", "{{ LDFLAGS }} -mmacos-version-min=11.0")

        c.var("cmake_system_name", "Darwin")
        c.var("cmake_system_processor", "aarch64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/sdk' -DCMAKE_SYSROOT={{ cross }}/sdk")

        c.var("meson_cross_system", "darwin")
        c.var("meson_cross_subsystem", "macos")
        c.var("meson_cross_kernel", "xnu")
        c.var("meson_cross_cpu_family", "aarch64")
        c.var("meson_cross_cpu", "arm64")

    elif (c.platform == "ios") and (c.arch == "arm64"):

        llvm(
            c,
            clang_args="-target arm64-apple-ios13.0 --sysroot {{cross}}/sdk",
        )

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED -miphoneos-version-min=13.0")
        c.env("LDFLAGS", "{{ LDFLAGS }} -miphoneos-version-min=13.0 -lmockrt")

        c.var("cmake_system_name", "Darwin")
        c.var("cmake_system_processor", "aarch64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/sdk' -DCMAKE_SYSROOT={{ cross }}/sdk")

        c.var("meson_cross_system", "darwin")
        c.var("meson_cross_subsystem", "ios")
        c.var("meson_cross_kernel", "xnu")
        c.var("meson_cross_cpu_family", "aarch64")
        c.var("meson_cross_cpu", "aarch64")

    elif (c.platform == "ios") and (c.arch == "sim-arm64"):

        llvm(
            c,
            clang_args="-target arm64-apple-ios13.0-simulator --sysroot {{cross}}/sdk",
        )

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED -mios-simulator-version-min=13.0")
        c.env("LDFLAGS", "{{ LDFLAGS }} -mios-version-min=13.0 -lmockrt")

        c.var("cmake_system_name", "Darwin")
        c.var("cmake_system_processor", "aarch64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/sdk' -DCMAKE_SYSROOT={{ cross }}/sdk")

        c.var("meson_cross_system", "darwin")
        c.var("meson_cross_subsystem", "ios-simulator")
        c.var("meson_cross_kernel", "xnu")
        c.var("meson_cross_cpu_family", "aarch64")
        c.var("meson_cross_cpu", "aarch64")

    elif (c.platform == "ios") and (c.arch == "sim-x86_64"):

        llvm(
            c,
            clang_args="-target x86_64-apple-ios13.0-simulator --sysroot {{cross}}/sdk",
        )

        c.env("CFLAGS", "{{ CFLAGS }} -DSDL_MAIN_HANDLED -mios-simulator-version-min=13.0")
        c.env("LDFLAGS", "{{ LDFLAGS }} -mios-simulator-version-min=13.0 -lmockrt")

        c.var("cmake_system_name", "Darwin")
        c.var("cmake_system_processor", "x86_64")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH='{{ install }};{{ cross }}/sdk' -DCMAKE_SYSROOT={{ cross }}/sdk")

        c.var("meson_cross_system", "darwin")
        c.var("meson_cross_subsystem", "ios-simulator")
        c.var("meson_cross_kernel", "xnu")
        c.var("meson_cross_cpu_family", "x86_64")
        c.var("meson_cross_cpu", "x86_64")

    elif (c.platform == "web") and (c.arch == "wasm") and (c.name != "web"):

        # Use emscripten wrapper to configure and build
        c.var("make", "emmake {{ make }}")
        c.var("configure", "emconfigure ./configure")
        c.var("cmake", "emcmake cmake")

        c.env("CFLAGS", "{{ CFLAGS }} -O3 -sUSE_SDL=2 -sUSE_LIBPNG -sUSE_LIBJPEG=1 -sUSE_BZIP2=1 -sUSE_ZLIB=1")
        c.env("LDFLAGS", "{{ LDFLAGS }} -O3 -sUSE_SDL=2 -sUSE_LIBPNG -sUSE_LIBJPEG=1 -sUSE_BZIP2=1 -sUSE_ZLIB=1 -sEMULATE_FUNCTION_POINTER_CASTS=1")

        c.var("emscriptenbin", "{{ cross }}/upstream/emscripten")
        c.var("crossbin", "{{ cross }}/upstream/bin")

        c.env("CC", "{{ emscriptenbin }}/emcc")
        c.env("CXX", "{{ emscriptenbin }}/em++")
        c.env("CPP", "{{ emscriptenbin }}/emcc -E")
        c.env("LD", "{{ emscriptenbin }}/emcc")
        c.env("LDSHARED", "{{ emscriptenbin }}/emcc")
        c.env("AR", "{{ emscriptenbin }}/emar")
        c.env("RANLIB", "{{ emscriptenbin }}/emranlib")
        c.env("STRIP", "{{ emscriptenbin }}/emstrip")
        c.env("NM", "{{ emscriptenbin }}/emnm")

        c.env("EMSCRIPTEN_TOOLS", "{{emscriptenbin}}/tools")
        c.env("EMSCRIPTEN", "{{emscriptenbin}}")

        c.env("PKG_CONFIG_LIBDIR", "{{cross}}/upstream/emscripten/cache/sysroot/lib/pkgconfig:{{cross}}/upstream/emscripten/system/lib/pkgconfig")
        # Add pkg-file search path for emscripten, since emscripten locked PKG_CONFIG_LIBDIR
        c.env("EM_PKG_CONFIG_PATH", "{{ install }}/lib/pkgconfig")

        # Tell emcc and em++ to use ccache when building
        c.env("EM_COMPILER_WRAPPER", "ccache")

        # Used to find sdl2-config.
        c.env("PATH", "{{cross}}/upstream/emscripten/system/bin/:{{PATH}}")

        c.var("cmake_system_name", "Emscripten")
        c.var("cmake_system_processor", "generic")
        c.var("cmake_args", "-DCMAKE_FIND_ROOT_PATH={{ install }}")

        c.var("meson_cross_system", "emscripten")
        c.var("meson_cross_kernel", "none")
        c.var("meson_cross_cpu_family", "wasm32")
        c.var("meson_cross_cpu", "wasm32")


    if c.kind not in ( "host", "host-python", "cross" ):
        c.env("PKG_CONFIG_LIBDIR", "{{ install }}/lib/pkgconfig:{{ PKG_CONFIG_LIBDIR }}")
        c.var("cmake_args", "{{cmake_args}} -DCMAKE_SYSTEM_NAME={{ cmake_system_name }} -DCMAKE_SYSTEM_PROCESSOR={{ cmake_system_processor }} -DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER -DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY -DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY -DCMAKE_FIND_ROOT_PATH_MODE_PACKAGE=ONLY")

    c.env("PKG_CONFIG", "pkg-config --static")

    c.env("CFLAGS", "{{ CFLAGS }} -DRENPY_BUILD")
    c.env("CXXFLAGS", "{{ CFLAGS }}")

    c.var("cmake", "{{cmake}} {{ cmake_args }} -DCMAKE_PROJECT_INCLUDE_BEFORE={{root}}/tools/cmake_build_variables.cmake -DCMAKE_BUILD_TYPE=Release")

    if not "meson_cross_subsystem" in c.variables:
        c.var("meson_cross_subsystem", "{{ meson_cross_system }} ")

    if c.kind not in ( "host", "host-python", "cross" ):
        c.var("meson_build_kind", "cross")
    else:
        c.var("meson_build_kind", "native")

    c.var("meson_config_file", "{{ install }}/meson_{{meson_build_kind}}_file.txt")
    c.var("meson_args", "--{{meson_build_kind}}-file={{meson_config_file}} --buildtype=release -Dc_std=gnu17 -Dcpp_std=gnu++17")

    # Used by zlib.
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
        print("args:", " ".join(repr(i) for i in args))
        import traceback
        traceback.print_stack()
        sys.exit(1)

class RunCommand(object):

    def __init__(self, command, context):
        command = context.expand(command)
        self.command = shlex.split(command)

        self.cwd = context.cwd
        self.environ = context.environ.copy()

        self.p = subprocess.Popen(self.command, cwd=self.cwd, env=self.environ, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")

    def wait(self):
        self.code = self.p.wait()
        self.output = self.p.stdout.read() # type: ignore

    def report(self):
        print ("-" * 78)

        for i in self.command:
            if " " in i:
                print(repr(i), end=" ")
            else:
                print(i, end=" ")

        print()
        print()
        print(self.output)

        if self.code != 0:
            print()
            print(f"Process failed with {self.code}.")

class RunGroup(object):

    def __init__(self, context):
        self.context = context
        self.tasks = [ ]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        for i in self.tasks:
            i.wait()

        good = [ i for i in self.tasks if i.code == 0 ]
        bad = [ i for i in self.tasks if i.code != 0 ]

        for i in good:
            i.report()

        for i in bad:
            i.report()

        if bad:
            print()
            print("{} tasks failed.".format(len(bad)))
            sys.exit(1)

    def run(self, command):
        self.tasks.append(RunCommand(command, self.context))
