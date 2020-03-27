###############################################################################
# NAME:             CMakeLists.txt
#
# AUTHOR:           Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:      Cmake configuration file.
#
# CREATED:          09/13/2019
#
# LAST EDITED:      03/27/2020
###

cmake_minimum_required(VERSION 3.15.1)

project(Cretan DESCRIPTION "User Server")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -Wextra -O3 --std=c++17")

include(./CMakeDefs.txt)

add_executable(Cretan
    "${CRETAN_SOURCES}"
)
target_include_directories(Cretan PRIVATE
    include
)

include(GNUInstallDirs)

install(TARGETS Cretan
        DESTINATION ${CMAKE_INSTALL_BINDIR}
)

###############################################################################
