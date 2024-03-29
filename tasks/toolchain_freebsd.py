from renpybuild.context import Context
from renpybuild.task import task, annotator

# for quickly exiting during testing
import sys

# Used this for the basis for building this cross-compiler chain
# https://preshing.com/20141119/how-to-build-a-gcc-cross-compiler/
# also took heavy inspiration from Linux From Scratch
# https://linuxfromscratch.org/lfs/downloads/9.1-systemd-rc1/LFS-BOOK-9.1-rc1-NOCHUNKS.html#ch-tools-generalinstructions
#binutils = "2.40"
#gcc = "13.2.0"
llvm = "18.1.2"

@task(kind="toolchain", platforms="freebsd")
def unpack_toolchain(c: Context):
    c.clean()
#
#    c.var("binutils", binutils)
#    c.run("tar xJf {{ tmp }}/tars/binutils-{{binutils}}.tar.xz")
#
#    c.var("gcc", gcc)
#    c.run("tar xzf {{ tmp }}/tars/gcc-{{gcc}}.tar.gz")
#
    c.var("llvm", llvm)
    c.run("tar xzf {{ tmp }}/tars/llvmorg-{{llvm}}.tar.gz")

#@task(kind="cross", platforms="freebsd")
#def unpack_cross(c: Context):
#    c.clean()
#
#    c.var("binutils", binutils)
#    c.run("tar xJf {{ tmp }}/tars/binutils-{{binutils}}.tar.xz")
#
#    c.var("gcc", gcc)
#    c.run("tar xzf {{ tmp }}/tars/gcc-{{gcc}}.tar.gz")
#
#    c.var("llvm", llvm)
#    c.run("tar xzf {{ tmp }}/tars/llvmorg-{{llvm}}.tar.gz")
#
## build this first to link against
#@task(kind="toolchain", platforms="freebsd")
#def build_binutils_stage1(c: Context):
#    c.var("binutils", binutils)
#    c.chdir("binutils-{{binutils}}")
#
#    c.env("CC", "ccache clang15")
#    c.env("CXX", "ccache clang++15")
#    c.env("CPP", "ccache clang15 -E")
#    
#    # LFS tip for binutils cross-compilation
#    if c.arch == "x86_64":
#        c.run("mkdir -p {{ TOOLCHAIN }}/lib")
#        c.run("ln -sf {{ TOOLCHAIN }}/lib64")
#
#    c.run("""
#        ./configure --prefix={{ TOOLCHAIN }}
#            --target={{ target_platform }}
#            --disable-nls
#            --enable-gprofng=no
#            --disable-werror
#            --with-sysroot={{ install }}
#    """)
#
#    # binutils doesn't like being built with anything but gmake by itself
#    c.run("{{ make_exec }}")
#    c.run("{{ make_exec }} install")
#
## build what's needed to generate required libgcc libraries for llvm and future gcc build
#@task(kind="toolchain", platforms="freebsd")
#def configure_gcc_stage1(c: Context):
#    c.var("gcc", gcc)
#    c.chdir("gcc-{{gcc}}")
#
#    # download extra libs per here: https://gcc.gnu.org/wiki/FAQ#configure
#    c.run("touch contrib/download_prerequisites")
#    c.run("sh contrib/download_prerequisites")
#
#    # this patch removes a Linux only macro that causes the build to fail
#    #c.patch("gcc-tree-header-fix-freebsd.diff", p=0)
#
#    # Force GCC to not use any system headers or libraries at all
#    bsd_header = str(c.path("gcc/config/netbsd.h"))
#    c.var("bsd_header", bsd_header)
#    # append this to end of bsd_header; %replace% will be replaced with sed in next step
#    with open(bsd_header, mode='a') as f:
#        print('''
##undef STANDARD_STARTFILE_PREFIX_1
##undef STANDARD_STARTFILE_PREFIX_2
##define STANDARD_STARTFILE_PREFIX_1 "%replace%/lib"
##define STANDARD_STARTFILE_PREFIX_2 ""
#        ''', file=f)
#
#    c.run("""
#        sed -e 's@/lib\(exec\)@{{ TOOLCHAIN }}&@g'
#            -e 's@%replace%@{{ TOOLCHAIN }}@g'
#            -e 's@/usr@{{ TOOLCHAIN }}@g' 
#            -i.orig {{ bsd_header }}
#    """)
#
#    # build in external build directory
#    c.run("mkdir -p ../gcc-build")
#    c.chdir("../gcc-build")
#
#    # fix sanity check error
#    c.env("CC", "ccache gcc-13")
#    c.env("CXX", "ccache g++-13")
#    c.env("CPP", "ccache cpp")
#    c.env("CFLAGS", "-Wall -isystem {{ TOOLCHAIN }}/include")
#    c.env("CXXFLAGS", "{{ CFLAGS }}")
#
#    c.run("""
#        ../gcc-{{gcc}}/configure --prefix={{ TOOLCHAIN }}
#            --target={{ target_platform }}
#            --with-sysroot={{ install }}
#            --with-newlib
#            --without-headers
#            --with-native-system-header-dir={{ TOOLCHAIN }}/include
#            --disable-nls
#            --disable-shared
#            --disable-multilib
#            --disable-threads
#            --disable-libatomic
#            --disable-libgomp
#            --disable-libquadmath
#            --disable-libssp
#            --disable-libvtv
#            --disable-zlib
#            --disable-libstdcxx
#            --enable-languages=c,c++
#    """)
#    
## created this to prevent errors caused from configuring gcc multiple times in a row
#@task(kind="toolchain", platforms="freebsd")
#def build_gcc_stage1(c: Context):
#    c.var("gcc", gcc)
#    c.chdir("gcc-build")
#
#    # fix sanity check error
#    c.env("CC", "ccache clang15")
#    c.env("CXX", "ccache clang++15")
#    c.env("CPP", "ccache clang15 -E")
#    c.env("CFLAGS", "-Wall -isystem {{ TOOLCHAIN }}/include")
#    c.env("CXXFLAGS", "{{ CFLAGS }}")
#
#    c.run("{{ make }}")
#    c.run("{{ make_exec }} install")
#
#    sys.exit()
#
## build clang/llvm against cross-compiled gcc from previous step
## this will be the main compiler but requires gcc to work properly
#@task(kind="toolchain", platforms="freebsd")
#def build_llvm_stage64(c: Context):
#    c.var("llvm", llvm)
#    c.chdir("llvm-project-llvmorg-{{llvm}}")
#    c.run("mkdir -p build")
#    c.chdir("build")
#
#    # to solve rebuild issues
#    c.run("touch CMakeCache.txt")
#    c.run("mv CMakeCache.txt reset")
#
#    #c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
#    c.env("CC", "clang15")
#    c.env("CXX", "clang++15")
#    c.env("CPP", "clang15 -E")
#    c.env("CFLAGS", "-I/usr/include")
#    c.env("CXXFLAGS", "-I/usr/include")
#    c.env("LDFLAGS", "-L/usr/lib -L/usr/local/lib")
#    c.run("""
#        cmake 
#            -DCMAKE_BUILD_TYPE=Release 
#            -DLLVM_LIBDIR_SUFFIX=64 
#            -DLLVM_ENABLE_PROJECTS="clang;lld" 
#            -DLLVM_CCACHE_BUILD=ON 
#            -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"
#            -DLLVM_TARGETS_TO_BUILD="X86"
#            -DLLVM_USE_LINKER=lld
#            -DLLVM_DEFAULT_TARGET_TRIPLE={{ host_platform }} 
#            -DCMAKE_INSTALL_PREFIX={{ TOOLCHAIN }}
#            ../llvm/
#    """)
#
#    c.run("{{ make }}")
#    c.run("{{ make_exec }} install")
#
#    # Symlink to correct a bug with building cross-tools
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-ar {{ TOOLCHAIN }}/bin/llvm-ar-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-ranlib {{ TOOLCHAIN }}/bin/llvm-ranlib-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-windres {{ TOOLCHAIN }}/bin/llvm-windres-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-strip {{ TOOLCHAIN }}/bin/llvm-strip-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-lipo {{ TOOLCHAIN }}/bin/llvm-lipo-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-nm {{ TOOLCHAIN }}/bin/llvm-nm-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/llvm-readelf {{ TOOLCHAIN }}/bin/llvm-readelf-15")
#    c.run("ln -sf {{ TOOLCHAIN }}/bin/clang++ {{ TOOLCHAIN }}/bin/clang++-15")

# rebuild binutils with cross llvm/clang
#@task(kind="cross", platforms="freebsd")
#def build_binutils_stage2(c: Context):
#    c.var("binutils", binutils)
#    c.chdir("binutils-{{binutils}}")
#
#    # use these to fix some build issues
##    c.env("PATH", "{{ PATH }}:{{ TOOLCHAIN }}/bin")
##    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
##    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
##    c.env("LDFLAGS", "-L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
#    c.run("""
#        ./configure --prefix={{ cross }}/{{ host_platform }}
#            --build={{ build_platform }}
#            --target={{ target_platform }}
#            --host={{ host_platform }}
#            --disable-multilib
#    """)
#
#    # binutils doesn't like being built with anything but gmake by itself
#    c.run("{{ make_exec }}")
#    c.run("{{ make_exec }} install")
#
## rebuild all of gcc with new libraries and tools
#@task(kind="cross", platforms="freebsd")
#def build_gcc_stage4(c: Context):
#    c.var("gcc", gcc)
#    c.chdir("gcc-{{gcc}}")
#
#    # download extra libs per here: https://gcc.gnu.org/wiki/FAQ#configure
#    c.run("touch contrib/download_prerequisites")
#    c.run("sh contrib/download_prerequisites")
#    c.patch("gcc-tree-header-fix-freebsd.diff", p=0)
#
#    # build in external build directory
#    c.run("mkdir -p ../gcc-build")
#    c.chdir("../gcc-build")
#
#    # use these to fix some build issues
##    c.env("PATH", "{{ TOOLCHAIN }}/bin:{{ PATH }}")
##    c.env("CFLAGS", "{{ CFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
##    c.env("CXXFLAGS", "{{ CXXFLAGS }} -I{{ TOOLCHAIN }}/include -I/usr/include -I/usr/local/include")
##    c.env("LDFLAGS", "{{ LDFLAGS }} -L{{ TOOLCHAIN }}/lib64 -L/usr/lib -L/usr/local/lib")
#    c.run("""
#        ../gcc-{{gcc}}/configure --prefix={{ cross }}/{{ host_platform }}
#            --build={{ build_platform }}
#            --target={{ target_platform }}
#            --host={{ host_platform }}
#            --enable-languages=c,c++
#            --disable-multilib
#    """)
#
#    c.run("{{ make }}")
#    c.run("{{ make_exec }} install")
#
# build 64-bit FreeBSD cross-compiler
@task(kind="toolchain", platforms="freebsd")
def build_llvm_freebsd64(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    # use these to fix some build issues
    c.run("touch CMakeCache.txt")
    c.run("mv CMakeCache.txt reset")
    c.env("CC", "clang15")
    c.env("CXX", "clang++15")
    c.env("CPP", "clang15 -E")
    c.env("LLVM_DIR", "../llvm")
    c.env("Clang_DIR", "../clang")
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
            -DCMAKE_INSTALL_PREFIX={{ cross }}/{{ target_platform }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

    # Symlink to correct a bug with building cross-tools
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ar 
          {{ cross }}/{{ host_platform }}/bin/llvm-ar-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ranlib 
          {{ cross }}/{{ host_platform }}/bin/llvm-ranlib-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-windres 
          {{ cross }}/{{ host_platform }}/bin/llvm-windres-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-strip 
          {{ cross }}/{{ host_platform }}/bin/llvm-strip-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-lipo 
          {{ cross }}/{{ host_platform }}/bin/llvm-lipo-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-nm 
          {{ cross }}/{{ host_platform }}/bin/llvm-nm-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-readelf 
          {{ cross }}/{{ host_platform }}/bin/llvm-readelf-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/clang++ 
          {{ cross }}/{{ host_platform }}/bin/clang++-15""")

## build 32-bit FreeBSD cross-compiler
@task(kind="toolchain", platforms="freebsd")
def build_llvm_freebsd64(c: Context):
    c.var("llvm", llvm)
    c.chdir("llvm-project-llvmorg-{{llvm}}")
    c.run("mkdir -p build")
    c.chdir("build")

    # use these to fix some build issues
    c.run("touch CMakeCache.txt")
    c.run("mv CMakeCache.txt reset")
    c.env("CC", "clang15")
    c.env("CXX", "clang++15")
    c.env("CPP", "clang15 -E")
    c.run("""
        cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=32
            -DLLVM_ENABLE_PROJECTS="clang;lld" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi"
            -DLLVM_TARGETS_TO_BUILD="X86"
            -DLLVM_USE_LINKER=lld
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ target_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ cross }}/{{ target_platform }}
            ../llvm/
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")

    # Symlink to correct a bug with building cross-tools
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ar 
          {{ cross }}/{{ host_platform }}/bin/llvm-ar-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-ranlib 
          {{ cross }}/{{ host_platform }}/bin/llvm-ranlib-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-windres 
          {{ cross }}/{{ host_platform }}/bin/llvm-windres-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-strip 
          {{ cross }}/{{ host_platform }}/bin/llvm-strip-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-lipo 
          {{ cross }}/{{ host_platform }}/bin/llvm-lipo-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-nm 
          {{ cross }}/{{ host_platform }}/bin/llvm-nm-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/llvm-readelf 
          {{ cross }}/{{ host_platform }}/bin/llvm-readelf-15""")
    c.run("""ln -sf {{ cross }}/{{ host_platform }}/bin/clang++ 
          {{ cross }}/{{ host_platform }}/bin/clang++-15""")

