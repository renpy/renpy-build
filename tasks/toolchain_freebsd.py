from renpybuild.context import Context
from renpybuild.task import task, annotator

version = "15.0.7"

@task(platforms="freebsd")
def unpack(c: Context):
    c.clean()

    c.var("version", version)
    c.run("tar xaf $ROOT/tmp/llvmorg-{{version}}.tar.gz")

@task(platforms="freebsd")
def build(c: Context):
    c.var("version", version)
    c.chdir("llvm-project-llvmorg-{{version}}")
    c.run("mkdir -p build")
    c.chdir("build")

    c.env("CC", "clang15")
    c.env("CXX", "clang++15")
    c.run("""
        ../llvm/cmake 
            -DCMAKE_BUILD_TYPE=Release 
            -DLLVM_LIBDIR_SUFFIX=64 
            -DLLVM_ENABLE_PROJECTS="clang;lld;clang-tools-extra;polly;lldb" 
            -DLLVM_CCACHE_BUILD=ON 
            -DLLVM_ENABLE_RUNTIMES=all 
            -DLLVM_TARGETS_TO_BUILD="X86;AArch64;ARM;WebAssebly" 
            -DLLVM_USE_LINKER=gold 
            -DLLVM_DEFAULT_TARGET_TRIPLE={{ host_platform }} 
            -DCMAKE_INSTALL_PREFIX={{ TOOLCHAIN }}
    """)

    c.run("{{ make }}")
    c.run("{{ make_exec }} install")
