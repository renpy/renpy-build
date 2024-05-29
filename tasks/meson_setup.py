from renpybuild.context import Context
from renpybuild.task import task

@task(kind="host", platforms="all")
def patch_meson(c: Context):

    # See https://github.com/pyodide/pyodide/discussions/4762, will be fixed in
    # meson 1.4.1
    import mesonbuild.coredata
    if mesonbuild.coredata.version <= '1.4.0':
        c.chdir(f"{mesonbuild.__path__[0]}/..")
        c.patch("meson-fix-emscripten-std.patch")

@task(platforms="all")
def unpack(c: Context):

    # Remove flags for compiler and set them using meson's method
    for compiler_var in ("CC", "CXX", "CPP"):
        updated_var = c.environ[compiler_var].replace("-fuse-ld=lld -Wno-unused-command-line-argument ", "")

        if compiler_var == "CXX":
            updated_var = updated_var.replace(" -std=gnu++17", "")
        else:
            updated_var = updated_var.replace(" -std=gnu17", "")

        c.env(compiler_var, updated_var)

    # Set linker type
    c.env("CC_LD", "lld")
    c.env("CXX_LD", "lld")

    if c.platform == "mac" or c.platform == "ios":
        c.env("OBJC_LD", "lld")
        c.env("OBJCXX_LD", "lld")

    c.run("""
        {{ meson }} env2mfile --cross
        -o "{{ install }}/meson_cross_file.txt"
        --system={{ meson_cross_system }}
        --subsystem={{ meson_cross_subsystem }}
        --kernel={{ meson_cross_kernel }}
        --cpu-family={{ meson_cross_cpu_family }}
        --cpu={{ meson_cross_cpu }}
        """)

    # Delete option if its value is "none"
    c.run(""" sed -i "/'none'/d" "{{ install }}/meson_cross_file.txt" """)

@task(kind="host", platforms="all")
def unpack(c: Context):

    # Remove flags for compiler and set them using meson's method
    for compiler_var in ("CC", "CXX", "CPP"):
        updated_var = c.environ[compiler_var].replace("-fuse-ld=lld -Wno-unused-command-line-argument ", "")

        if compiler_var == "CC":
            updated_var = updated_var.replace(" -std=gnu17", "")
        elif compiler_var == "CXX":
            updated_var = updated_var.replace(" -std=gnu++17", "")

        c.env(compiler_var, updated_var)

    # Set linker type
    c.env("CC_LD", "lld")
    c.env("CXX_LD", "lld")

    if c.platform == "mac" or c.platform == "ios":
        c.env("OBJC_LD", "lld")
        c.env("OBJCXX_LD", "lld")

    c.run(""" {{ meson }} env2mfile --native -o "{{ install }}/meson_native_file.txt" """)
