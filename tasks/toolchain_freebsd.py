from renpybuild.context import Context
from renpybuild.task import task, annotator

# Used this for the basis for building this cross-compiler chain
# https://preshing.com/20141119/how-to-build-a-gcc-cross-compiler/
binutils = "2.40"
gcc = "13.2.0"
llvm = "15.0.7"

@task(kind="toolchain", platforms="freebsd")
def unpack_toolchain(c: Context):
    c.clean()

    c.var("binutils", binutils)
    c.run("tar xJf {{ tmp }}/tars/binutils-{{binutils}}.tar.xz")

    c.var("gcc", gcc)
    c.run("tar xzf {{ tmp }}/tars/gcc-{{gcc}}.tar.gz")

@task(kind="cross", platforms="freebsd")
def unpack_cross(c: Context):
    c.clean()

    c.var("binutils", binutils)
    c.run("tar xJf {{ tmp }}/tars/binutils-{{binutils}}.tar.xz")

    c.var("llvm", llvm)
    c.run("tar xzf {{ tmp }}/tars/llvmorg-{{llvm}}.tar.gz")

@task(kind="toolchain", platforms="freebsd")
def build_binutils(c: Context):
    c.var("binutils", binutils)
    c.chdir("binutils-{{binutils}}")

    c.env("CC", "ccache clang15")
    c.env("CXX", "ccache clang++15")
    c.env("CPP", "ccache clang15 -E")
    c.run("""
        ./configure --prefix={{ TOOLCHAIN }}
            --target={{ host_platform }}
            --disable-multilib
    """)

    # binutils doesn't like being built with anything but gmake by itself
    c.run("{{ make_exec }}")
    c.run("{{ make_exec }} install")

@task(kind="toolchain", platforms="freebsd")
def build_gcc(c: Context):
    c.var("gcc", gcc)
    c.chdir("gcc-{{gcc}}")

    c.env("CC", "ccache clang15")
    c.env("CXX", "ccache clang++15")
    c.env("CPP", "ccache clang15 -E")
    c.env("CFLAGS", "-I/usr/include -I/usr/local/include -Wno-unused-result")
    c.env("CXXFLAGS", "-I/usr/include -I/usr/local/include -Wno-unused-result")
    c.run("""
        ./configure --prefix={{ TOOLCHAIN }}
            --target={{ host_platform }}
            --enable-languages=c,c++
            --disable-multilib
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }}")

@task(kind="cross", platforms="freebsd")
def build_llvm(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    c.env("CC", "ccache gcc-13")
    c.env("CXX", "ccache gcc++-13")
    c.env("CPP", "ccache cpp-13")
    c.run("""
        cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=64 
            -DLLVM_ENABLE_PROJECTS="clang;clang-extra-tools;lld;lldb" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES="all"
            -DLLVM_TARGETS_TO_BUILD="X86"
            -DLLVM_USE_LINKER=lld
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ host_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ TOOLCHAIN }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

@task(kind="cross", platforms="freebsd")
def build_binutils(c: Context):
    c.var("binutils", binutils)
    c.chdir("binutils-{{binutils}}")

    c.run("""
        ./configure --prefix={{ TOOLCHAIN }}
            --build={{ build_platform }}
            --target={{ target_platform }}
            --host={{ host_platform }}
            --disable-multilib
    """)

    # binutils doesn't like being built with anything but gmake by itself
    c.run("{{ make_exec }}")
    c.run("{{ make_exec }} install")
