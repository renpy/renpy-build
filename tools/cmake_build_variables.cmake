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

set_env_without_ccache(CC)
set_env_without_ccache(CXX)
set_env_without_ccache(CPP)
set_variable_without_ccache(CMAKE_AR AR)
set_variable_without_ccache(CMAKE_RANLIB RANLIB)
set_variable_without_ccache(CMAKE_STRIP STRIP)

if(DEFINED ENV{RC})
    set_variable_without_ccache(CMAKE_RC_COMPILER RC)
endif()

if(DEFINED ENV{LD})
    set_env_without_ccache(LD)
endif()

if(DEFINED ENV{LDSHARED})
    set_env_without_ccache(LDSHARED)
endif()

# Set "CMAKE_<LANG>_COMPILER_LAUNCHER" to tell cmake to use ccache
set(CMAKE_C_COMPILER_LAUNCHER "ccache")
set(CMAKE_CXX_COMPILER_LAUNCHER "ccache")
