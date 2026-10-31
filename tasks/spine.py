# By Sebulsik <sebulsik.dev@gmail.com>

from renpybuild.context import Context
from renpybuild.task import task, annotator

# Spine 4.3.
# tars/spine-runtimes/spine-cpp
# tars/spine-runtimes/spine-c
# https://github.com/esotericsoftware/spine-runtimes


@annotator
def annotate(c: Context):
    c.include("{{ install }}/spine-c/include")
    c.env("SPINE", "{{ install }}/spine-c")


@task(kind="host", platforms="all")
def unpack(c: Context):
    c.clean()

    spine_cpp = c.path("{{ root }}/tars/spine-runtimes/spine-cpp")
    spine_c = c.path("{{ root }}/tars/spine-runtimes/spine-c")

    if (not spine_cpp.exists()) or (not spine_c.exists()):
        raise RuntimeError("Spine 4.3 sources missing from tars/spine-runtimes/")

    c.var("spine_cpp", spine_cpp)
    c.var("spine_c", spine_c)

    # (kind="host" sets install={{ host }}, so this is tmp/host/spine-4.3)
    c.run("install -d {{ host }}/spine-4.3/spine-cpp")
    c.run("install -d {{ host }}/spine-4.3/spine-c")

    c.run("cp -r {{ spine_cpp }}/include {{ host }}/spine-4.3/spine-cpp/")
    c.run("cp -r {{ spine_cpp }}/src {{ host }}/spine-4.3/spine-cpp/")

    c.run("cp -r {{ spine_c }}/include {{ host }}/spine-4.3/spine-c/")
    c.run("cp -r {{ spine_c }}/src {{ host }}/spine-4.3/spine-c/")


@task(platforms="linux,mac,windows,android")
def build(c: Context):
    """
    Build spine-c 4.3 (backed by spine-cpp) as a shared library for the
    target platform.
    """
    print(f"spine.build: Starting for {c.platform}-{c.arch}")
    c.clean()

    staged = c.path("{{ host }}/spine-4.3")
    if not staged.exists():
        print(f"spine.build: ERROR - staged spine sources not found at {staged}")
        print("spine.build: Run unpack task first")
        return

    # Copy sources to the build directory.
    c.run("cp -r {{ host }}/spine-4.3/spine-cpp spine-cpp")
    c.run("cp -r {{ host }}/spine-4.3/spine-c spine-c")

    # header install
    c.run("install -d {{ install }}/spine-c")
    c.run("cp -r spine-c/include {{ install }}/spine-c/")
    c.run("rm -rf {{ install }}/spine-c/src")
    c.run("cp -r spine-c/src {{ install }}/spine-c/src")
    c.run("find {{ install }}/spine-c/src -name '*.cpp' -delete")

    if c.platform == "windows":
        c.var("lib_name", "spine-c.dll")
    elif c.platform == "mac":
        c.var("lib_name", "libspine-c.dylib")
    else:  # linux, android
        c.var("lib_name", "libspine-c.so")

    # Collect the C++ sources (also avoid name-collisions)
    sources = []  # (source path, object name)

    for f in sorted(c.path("spine-cpp/src/spine").glob("*.cpp")):
        sources.append((f, "cpp_" + f.stem + ".o"))

    for f in sorted(c.path("spine-c/src").glob("*.cpp")):
        sources.append((f, "c_" + f.stem + ".o"))

    for f in sorted(c.path("spine-c/src/generated").glob("*.cpp")):
        sources.append((f, "gen_" + f.stem + ".o"))

    if not sources:
        print("spine.build: ERROR - no C++ sources found")
        return

    print(f"spine.build: Compiling {len(sources)} sources")

    if c.platform == "windows":
        # SPINE_C_API already expands to __declspec(dllexport) on Windows.
        c.var("pic_flags", "")
    else:
        c.var("pic_flags", "-fPIC -fvisibility=default")

    with c.run_group() as g:
        for source, object in sources:
            c.var("src", source)
            c.var("object", object)

            g.run("""
            {{ CXX }} {{ CXXFLAGS }}
            -std=c++11
            -fno-exceptions
            -fno-rtti
            {{ pic_flags }}
            -I spine-c/include
            -I spine-c/src
            -I spine-cpp/include
            -c {{ src }}
            -o {{ object }}
            """)

    objects = [object for _, object in sources]
    c.var("objects", " ".join(objects))

    with open(c.path("spine-c.map"), "w") as f:
        f.write("{ global: spine_*; local: *; };\n")

    # Link shared library.
    if c.platform == "linux":
        c.run("""
        {{ CXX }} {{ LDFLAGS }}
        -shared
        -static-libstdc++
        -Wl,-Bsymbolic
        -Wl,--exclude-libs,ALL
        -Wl,--version-script,spine-c.map
        -Wl,-soname,libspine-c.so
        -o {{ lib_name }}
        {{ objects }}
        -lm
        """)

    elif c.platform == "android":
        c.run("""
        {{ CXX }} {{ LDFLAGS }}
        -shared
        -static-libstdc++
        -Wl,-Bsymbolic
        -Wl,--exclude-libs,ALL
        -Wl,--version-script,spine-c.map
        -Wl,-soname,libspine-c.so
        -o {{ lib_name }}
        {{ objects }}
        -lm
        -llog
        """)

    elif c.platform == "mac":
        c.run("""
        {{ CXX }} {{ LDFLAGS }}
        -shared
        -Wl,-exported_symbol,_spine_*
        -o {{ lib_name }}
        -install_name @rpath/libspine-c.dylib
        {{ objects }}
        """)

    elif c.platform == "windows":
        c.run("""
        {{ CXX }} {{ LDFLAGS }}
        -shared
        -static-libstdc++
        -o {{ lib_name }}
        {{ objects }}
        {{cross}}/llvm-mingw/{{host_platform}}/lib/libunwind.a
        """)

    c.run("install -d {{ install }}/spine-c/lib")
    c.run("install {{ lib_name }} {{ install }}/spine-c/lib/")


@task(kind="arch", platforms="linux,windows", always=True)
def install_lib(c: Context):
    spine_lib = c.path("{{ install }}/spine-c/lib")
    if not spine_lib.exists():
        print("spine-c library not found - run build task first")
        return

    if c.platform == "windows":
        c.var("lib_name", "spine-c.dll")
    else:  # linux
        c.var("lib_name", "libspine-c.so")

    lib_file = spine_lib / c.expand("{{ lib_name }}")
    if not lib_file.exists():
        print(f"spine-c library file not found: {lib_file}")
        return

    c.run("cp {{ install }}/spine-c/lib/{{ lib_name }} {{ lib_name }}")

    # Strip for release
    if not c.args.nostrip:
        c.run("{{ STRIP }} --strip-unneeded {{ lib_name }}")

    c.run("install -d {{ dlpa }}")
    c.run("install {{ lib_name }} {{ dlpa }}/")


@task(kind="arch", platforms="android", always=True)
def install_android(c: Context):
    print(f"spine.install_android: Starting for {c.platform}-{c.arch}")

    spine_lib = c.path("{{ install }}/spine-c/lib")
    print(f"spine.install_android: Checking for library at {spine_lib}")

    if not spine_lib.exists():
        print(f"spine.install_android: ERROR - spine-c library directory not found at {spine_lib}")
        print("spine.install_android: Run build task first")
        return

    lib_file = spine_lib / "libspine-c.so"
    if not lib_file.exists():
        print(f"spine.install_android: ERROR - libspine-c.so not found at {lib_file}")
        return

    print(f"spine.install_android: Found library at {lib_file}")

    c.run("cp {{ install }}/spine-c/lib/libspine-c.so libspine-c.so")

    # Strip for release
    if not c.args.nostrip:
        c.run("{{ STRIP }} --strip-unneeded libspine-c.so")

    jniLibs_path = c.expand("{{ jniLibs }}")
    print(f"spine.install_android: Installing to jniLibs at {jniLibs_path}")
    c.run("install -d {{ jniLibs }}")
    c.run("install libspine-c.so {{ jniLibs }}/")

    # Verify installation
    import os
    installed_path = os.path.join(jniLibs_path, "libspine-c.so")
    if os.path.exists(installed_path):
        print(f"spine.install_android: VERIFIED - libspine-c.so exists at {installed_path}")
    else:
        print(f"spine.install_android: WARNING - libspine-c.so NOT FOUND at {installed_path}")

    print(f"spine.install_android: Successfully completed")


@task(kind="arch", platforms="mac", always=True)
def install_mac(c: Context):
    spine_lib = c.path("{{ install }}/spine-c/lib")
    if not spine_lib.exists():
        print("spine-c library not found - run build task first")
        return

    lib_file = spine_lib / "libspine-c.dylib"
    if not lib_file.exists():
        print(f"spine-c library file not found: {lib_file}")
        return

    c.run("install -d {{ install }}/mac")
    c.run("install {{ install }}/spine-c/lib/libspine-c.dylib {{ install }}/mac/")


@task(kind="platform", platforms="mac", always=True)
def lipo_mac(c: Context):
    x86_lib = c.path("{{ tmp }}/install.mac-x86_64/mac/libspine-c.dylib")
    arm_lib = c.path("{{ tmp }}/install.mac-arm64/mac/libspine-c.dylib")

    if not x86_lib.exists() and not arm_lib.exists():
        print("No spine-c libraries found for Mac - skipping lipo")
        return

    c.run("install -d {{ dlpa }}")

    if x86_lib.exists() and arm_lib.exists():
        c.run("""
            {{ lipo }} -create
            -output {{ dlpa }}/libspine-c.dylib
            {{ tmp }}/install.mac-x86_64/mac/libspine-c.dylib
            {{ tmp }}/install.mac-arm64/mac/libspine-c.dylib
            """)
    elif arm_lib.exists():
        c.run("cp {{ tmp }}/install.mac-arm64/mac/libspine-c.dylib {{ dlpa }}/libspine-c.dylib")
    elif x86_lib.exists():
        c.run("cp {{ tmp }}/install.mac-x86_64/mac/libspine-c.dylib {{ dlpa }}/libspine-c.dylib")
