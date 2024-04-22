cmake_minimum_required(VERSION 3.24)

project(documentation VERSION ${PROJECT_VERSION} LANGUAGES CXX)

# Find necessary packages
find_package(Doxygen REQUIRED)
find_package(Doxysphinx REQUIRED)
find_package(Sphinx REQUIRED)

# Find all the public headers from the animals library and store it in PUBLIC_HEADERS
get_target_property(PUBLIC_HEADER_DIRS doctemplate::animals INTERFACE_INCLUDE_DIRECTORIES)
foreach(INCLUDE_DIR ${PUBLIC_HEADER_DIRS})
  file(GLOB_RECURSE INCLUDE_DIR_PUBLIC_HEADERS ${INCLUDE_DIR}/*.h)
  list(APPEND PUBLIC_HEADERS ${INCLUDE_DIR_PUBLIC_HEADERS})
endforeach()

# Create some necessary variables
# Doxygen Input/Output dir and tag file
set(DOXYGEN_INPUT_DIR ${CMAKE_SOURCE_DIR})
set(DOXYGEN_OUTPUT_SUBDIR animals)
set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${DOXYGEN_OUTPUT_SUBDIR})
set(DOXYGEN_GENERATE_TAGFILE "${DOXYGEN_OUTPUT_SUBDIR}/html/tagfile.xml")

# Homepage file from doxygen
set(DOXYGEN_INDEX_FILE ${DOXYGEN_OUTPUT_DIR}/html/index.html)

# Generic doxygen configuration file and configured file
set(DOXYFILE_IN ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in)
set(DOXYFILE_OUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)

# Replace variables inside @@ with the current values
configure_file(${DOXYFILE_IN} ${DOXYFILE_OUT} @ONLY)

# Create doxygen output dir since doxygen won't do it
file(MAKE_DIRECTORY ${DOXYGEN_OUTPUT_DIR})

# Create a custom command for the doxygen creation process
# Note that it depends ${PUBLIC_HEADERS}, s.t. it will only be executed when a public header file has changed
add_custom_command(OUTPUT ${DOXYGEN_INDEX_FILE}
                   DEPENDS ${PUBLIC_HEADERS}
                   COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYFILE_OUT}
                   MAIN_DEPENDENCY ${DOXYFILE_IN}
                   COMMENT "Running doxygen"
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Adding a custom doxygen target
# Using the output of the above custom command ensures that this is only build when necessary (which means when
# a public header file has changed)
# Using a custom target directly without the add_custom_command(...) chain cause a doxygen rebuilt in every build run.
add_custom_target(doxygen ALL
    DEPENDS ${DOXYGEN_INDEX_FILE}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Specifing sphinx source and build folder
set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR}/sphinx)

# Search for all *.rst files in lib docs folder
file(GLOB_RECURSE DOXYSPHINX_RST_FILES ${DOXYGEN_OUTPUT_DIR}/*.rst)

# Create a custom command for the doxysphinx creation process
# Note that it also depends on ${PUBLIC_HEADERS} and doxygen, s.t. it will everytime be executed after doxygen was run
add_custom_command(OUTPUT ${DOXYSPHINX_RST_FILES}
    DEPENDS ${PUBLIC_HEADERS} doxygen
    COMMAND ${DOXYSPHINX_EXECUTABLE} build ${SPHINX_SOURCE} ${SPHINX_BUILD} ${DOXYFILE_OUT}
    COMMENT "Running doxysphinx"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Creating a custom target for doxysphinx
add_custom_target(doxysphinx ALL
    DEPENDS ${DOXYSPHINX_RST_FILES}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

# Search for all *.rst files in docs folder
file(GLOB_RECURSE RST_FILES *.rst)

set(SPHINX_INDEX_FILE ${SPHINX_BUILD}/index.html)

# Create a custom command for the sphinx process
add_custom_command(OUTPUT ${SPHINX_INDEX_FILE}
    DEPENDS ${RST_FILES} doxysphinx
    COMMAND ${SPHINX_EXECUTABLE} -b html ${SPHINX_SOURCE} ${SPHINX_BUILD}
    COMMENT "Running sphinx-build"
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_target(sphinx ALL
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS ${SPHINX_INDEX_FILE}
)
