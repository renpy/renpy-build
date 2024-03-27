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

    c.var("llvm", llvm)
    c.run("tar xzf {{ tmp }}/tars/llvmorg-{{llvm}}.tar.gz")

@task(kind="cross", platforms="freebsd")
def unpack_cross(c: Context):
    c.clean()

    c.var("binutils", binutils)
    c.run("tar xJf {{ tmp }}/tars/binutils-{{binutils}}.tar.xz")

    c.var("gcc", gcc)
    c.run("tar xzf {{ tmp }}/tars/gcc-{{gcc}}.tar.gz")

    c.var("llvm", llvm)
    c.run("tar xzf {{ tmp }}/tars/llvmorg-{{llvm}}.tar.gz")

# build this first to link against
@task(kind="toolchain", platforms="freebsd")
def build_binutils_stage1(c: Context):
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

# Build just the standard libraries
@task(kind="toolchain", platforms="freebsd")
def build_llvm_stage1(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    # to solve rebuild issues
    c.run("touch CMakeCache.txt")
    c.run("mv CMakeCache.txt reset")

    #c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
    c.env("CC", "clang15")
    c.env("CXX", "clang++15")
    c.env("CPP", "clang15 -E")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=64 
            -DLLVM_ENABLE_PROJECTS="" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"
            -DLLVM_TARGETS_TO_BUILD="X86"
            -DLLVM_USE_LINKER=lld
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ host_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ TOOLCHAIN }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

# build what's needed to generate required libgcc libraries for llvm and future gcc build
@task(kind="toolchain", platforms="freebsd")
def build_gcc_stage1(c: Context):
    c.var("gcc", gcc)
    c.chdir("gcc-{{gcc}}")

    # download extra libs per here: https://gcc.gnu.org/wiki/FAQ#configure
    c.run("touch contrib/download_prerequisites")
    c.run("sh contrib/download_prerequisites")
    c.patch("gcc-tree-header-fix-freebsd.diff", p=0)

    # build in external build directory
    c.run("mkdir -p ../gcc-build")
    c.chdir("../gcc-build")

    # use these to fix some build issues
    c.env("CC", "ccache clang15")
    c.env("CXX", "ccache clang++15")
    c.env("CPP", "ccache clang15 -E")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        ../gcc-{{gcc}}/configure --prefix={{ TOOLCHAIN }}
            --target={{ host_platform }}
            --enable-languages=c
            --disable-docs
            --disable-multilib
    """)

    c.run("{{ make }} all-gcc")
    c.run("{{ make_exec }} install-gcc")

# build a more complete version of clang/llvm
@task(kind="toolchain", platforms="freebsd")
def build_llvm_stage2(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    # to solve rebuild issues
    c.run("touch CMakeCache.txt")
    c.run("mv CMakeCache.txt reset")

    #c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
    c.env("CC", "clang15")
    c.env("CXX", "clang++15")
    c.env("CPP", "clang15 -E")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=64 
            -DLLVM_ENABLE_PROJECTS="clang;lld" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"
            -DLLVM_TARGETS_TO_BUILD="X86"
            -DLLVM_USE_LINKER=lld
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ host_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ TOOLCHAIN }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

    # Symlink to correct a bug with building cross-tools
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-ar {{ TOOLCHAIN }}/bin/llvm-ar-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-ranlib {{ TOOLCHAIN }}/bin/llvm-ranlib-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-windres {{ TOOLCHAIN }}/bin/llvm-windres-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-strip {{ TOOLCHAIN }}/bin/llvm-strip-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-lipo {{ TOOLCHAIN }}/bin/llvm-lipo-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-nm {{ TOOLCHAIN }}/bin/llvm-nm-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-readelf {{ TOOLCHAIN }}/bin/llvm-readelf-15")
    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-clang++ {{ TOOLCHAIN }}/bin/llvm-clang++-15")

# build libgcc support library
@task(kind="toolchain", platforms="freebsd")
def build_gcc_stage2(c: Context):
    c.var("gcc", gcc)
    c.chdir("gcc-{{gcc}}")

    # build in external build directory
    c.run("mkdir -p ../gcc-build")
    c.chdir("../gcc-build")

    c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
    c.env("CC", "ccache clang15")
    c.env("CXX", "ccache clang++15")
    c.env("CPP", "ccache clang15 -E")

    c.env("CFLAGS", "-I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include -isystem /usr/include -Wall")
    c.env("CXXFLAGS", "-I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include -isystem /usr/include -Wall -std=c++11 -stdlib=libc++")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib -L/usr/local/lib/gcc13")
    c.run("""
        ../gcc-{{gcc}}/configure --prefix={{ TOOLCHAIN }}
            --target={{ host_platform }}
            --enable-languages=c
            --disable-multilib
    """)

    c.run("{{ make }} all-target-libgcc")
    c.run("{{ make_exec }} install-target-libgcc")

@task(kind="toolchain", platforms="freebsd")
def build_gcc_stage3(c: Context):
    c.var("gcc", gcc)
    c.chdir("gcc-{{gcc}}")

    # build in external build directory
    c.run("mkdir -p ../gcc-build")
    c.chdir("../gcc-build")

    # use these to fix some build issues
    c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
    c.env("CC", "ccache clang15")
    c.env("CXX", "ccache clang++15")
    c.env("CPP", "ccache clang15 -E")

    c.env("CFLAGS", "-I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include -isystem /usr/include -Wall")
    c.env("CXXFLAGS", "-I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include -isystem /usr/include -Wall -std=c++11 -stdlib=libc++")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib -L/usr/local/lib/gcc13")
    c.run("""
        ../gcc-{{gcc}}/configure --prefix={{ TOOLCHAIN }}
            --target={{ host_platform }}
            --enable-languages=c++
            --disable-docs
            --disable-multilib
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")


# rebuild binutils with cross llvm/clang
@task(kind="cross", platforms="freebsd")
def build_binutils_stage2(c: Context):
    c.var("binutils", binutils)
    c.chdir("binutils-{{binutils}}")

    # use these to fix some build issues
    c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        ./configure --prefix={{ cross }}/{{ host_platform }}
            --build={{ build_platform }}
            --target={{ target_platform }}
            --host={{ host_platform }}
            --disable-multilib
    """)

    # binutils doesn't like being built with anything but gmake by itself
    c.run("{{ make_exec }}")
    c.run("{{ make_exec }} install")

# rebuild all of gcc with new libraries and tools
@task(kind="cross", platforms="freebsd")
def build_gcc_stage4(c: Context):
    c.var("gcc", gcc)
    c.chdir("gcc-{{gcc}}")

    # download extra libs per here: https://gcc.gnu.org/wiki/FAQ#configure
    c.run("touch contrib/download_prerequisites")
    c.run("sh contrib/download_prerequisites")
    #c.patch("gcc-tree-header-fix-freebsd.diff", p=0)

    # build in external build directory
    c.run("mkdir -p ../gcc-build")
    c.chdir("../gcc-build")

    # use these to fix some build issues
    c.env("PATH", "{{ TOOLCHAIN }}/bin:{{ PATH }}")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "{{ LDFLAGS }} -L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        ../gcc-{{gcc}}/configure --prefix={{ cross }}/{{ host_platform }}
            --build={{ build_platform }}
            --target={{ target_platform }}
            --host={{ host_platform }}
            --enable-languages=c,c++
            --disable-multilib
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

# build proper final llvm/clang that rest of libraries will build against
@task(kind="cross", platforms="freebsd")
def build_llvm_stage2(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    # use these to fix some build issues
    c.env("PATH", "{{ TOOLCHAIN }}/bin:{{ PATH }}")
    c.run("touch CMakeCache.txt")
    c.run("mv CMakeCache.txt reset")
    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
    c.env("LDFLAGS", "{{ LDFLAGS }} -L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
    c.run("""
        cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=64 
            -DLLVM_ENABLE_PROJECTS="clang;lld" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"
            -DLLVM_TARGETS_TO_BUILD="X86"
            -DLLVM_USE_LINKER=lld
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ target_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ cross }}/{{ host_platform }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

    # Symlink to correct a bug with building cross-tools
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ar {{ cross }}/{{ host_platform }}/bin/llvm-ar-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ranlib {{ cross }}/{{ host_platform }}/bin/llvm-ranlib-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-windres {{ cross }}/{{ host_platform }}/bin/llvm-windres-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-strip {{ cross }}/{{ host_platform }}/bin/llvm-strip-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-lipo {{ cross }}/{{ host_platform }}/bin/llvm-lipo-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-nm {{ cross }}/{{ host_platform }}/bin/llvm-nm-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-readelf {{ cross }}/{{ host_platform }}/bin/llvm-readelf-15")
    c.run("ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-clang++ {{ cross }}/{{ host_platform }}/bin/llvm-clang++-15")

