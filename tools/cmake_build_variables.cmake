macro(set_variable_without_ccache VAR ENV_ARG)
    # Remove "ccache" in environment variables and set
    # the related cmake variable to it
    string(REGEX REPLACE "^ccache " "" NO_CCACHE $ENV{${ENV_ARG}})
    set(${VAR} ${NO_CCACHE})
endmacro()

macro(set_env_without_ccache VAR)
    # Remove "ccache" in environment variables, but instead
    # of setting the cmake variable, let cmake itself set it by
    # environment variable to ensure that the parameters are
    # passed correctly
    string(REGEX REPLACE "^ccache " "" NO_CCACHE $ENV{${VAR}})
    set(ENV{${VAR}} ${NO_CCACHE})
endmacro()

macro(set_env_without_string VAR REPLACE_STRING)
    # Remove "REPLACE_STRING" for environment "VAR" and set
    # the "REPLACED" variable to environment
    string(REPLACE ${REPLACE_STRING} "" REPLACED $ENV{${VAR}})
    set(ENV{${VAR}} ${REPLACED})
endmacro()

set_env_without_ccache(CC)
set_env_without_ccache(CXX)
set_env_without_ccache(CPP)
set_variable_without_ccache(CMAKE_AR AR)
set_variable_without_ccache(CMAKE_RANLIB RANLIB)
set_variable_without_ccache(CMAKE_STRIP STRIP)

# Set "CMAKE_<LANG>_COMPILER_LAUNCHER" to tell cmake to use ccache
set(CMAKE_C_COMPILER_LAUNCHER "ccache")
set(CMAKE_CXX_COMPILER_LAUNCHER "ccache")
set(CMAKE_OBJC_COMPILER_LAUNCHER "ccache")
set(CMAKE_OBJCXX_COMPILER_LAUNCHER "ccache")

# Remove "-std=*" from environment
set_env_without_string(CC " -std=gnu17")
set_env_without_string(CXX " -std=gnu++17")

# Set "CMAKE_<LANG>_STANDARD" to add flag -std=* for compiler
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_STANDARD 17)
set(CMAKE_OBJC_STANDARD 17)
set(CMAKE_OBJCXX_STANDARD 17)

# Set "CMAKE_<LANG>_EXTENSIONS" to use std flag such as -std=gnu17 instead of -std=c17
set(CMAKE_C_EXTENSIONS ON)
set(CMAKE_CXX_EXTENSIONS ON)
set(CMAKE_OBJC_EXTENSIONS ON)
set(CMAKE_OBJCXX_EXTENSIONS ON)

# Cmake has it own way to set linker since version 3.29, but currently Ubuntu's camke is outdated
if(CMAKE_VERSION VERSION_GREATER "3.29")
    set_env_without_string(CC "-fuse-ld=lld -Wno-unused-command-line-argument ")
    set_env_without_string(CXX "-fuse-ld=lld -Wno-unused-command-line-argument ")
    set_env_without_string(CPP "-fuse-ld=lld -Wno-unused-command-line-argument ")

    set(CMAKE_LINKER_TYPE LLD)
    set(CMAKE_C_USING_LINKER_LLD "-fuse-ld=lld")
    set(CMAKE_CXX_USING_LINKER_LLD "-fuse-ld=lld")
    set(CMAKE_OBJC_USING_LINKER_LLD "-fuse-ld=lld")
    set(CMAKE_OBJCXX_USING_LINKER_LLD "-fuse-ld=lld")
endif()
