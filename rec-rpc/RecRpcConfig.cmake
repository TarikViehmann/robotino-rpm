if(NOT REC_RPC_DIR)
    set( REC_RPC_DIR "/usr" )
  endif()
# Define package variables
set(REC_RPC_INCLUDE_DIRS "${CMAKE_INSTALL_PREFIX}/include")
set(REC_RPC_LIBRARY_DIRS "${CMAKE_INSTALL_PREFIX}/lib64")
set(REC_RPC_BIN_DIRS "${CMAKE_INSTALL_PREFIX}/bin")

# Set the found flag
find_path(
	REC_RPC_INCLUDES
	rec/rpc/Client.h
    ${REC_RPC_INCLUDE_DIRS}
)

find_library(
	REC_RPC_RELEASE_LIBRARY
	NAMES
	rec_rpc
	PATHS
    ${REC_RPC_LIBRARY_DIRS}
)

if(REC_RPC_INCLUDES AND REC_RPC_RELEASE_LIBRARY)
    set(REC_RPC_LIBRARY ${REC_RPC_RELEASE_LIBRARY})
    set(REC_RPC_FOUND TRUE)
endif()
# Export targets
add_library(rec_rpc INTERFACE)
target_include_directories(rec_rpc INTERFACE "${REC_RPC_INCLUDE_DIRS}")
target_link_directories(rec_rpc INTERFACE "${REC_RPC_LIBRARY_DIRS}")

