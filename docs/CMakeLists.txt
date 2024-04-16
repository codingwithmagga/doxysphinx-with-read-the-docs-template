cmake_minimum_required(VERSION 3.24)

project(documentation VERSION ${PROJECT_VERSION} LANGUAGES CXX)

find_package(Doxygen REQUIRED)
find_package(Doxysphinx REQUIRED)
find_package(Sphinx REQUIRED)

# Find all the public headers
get_target_property(PUBLIC_HEADER_DIRS doctemplate::animals INTERFACE_INCLUDE_DIRECTORIES)

foreach(INCLUDE_DIR ${PUBLIC_HEADER_DIRS})
  file(GLOB_RECURSE INCLUDE_DIR_PUBLIC_HEADERS ${INCLUDE_DIR}/*.h)
  list(APPEND PUBLIC_HEADERS ${INCLUDE_DIR_PUBLIC_HEADERS})
endforeach()

set(DOXYGEN_INPUT_DIR ${CMAKE_SOURCE_DIR})
set(DOXYGEN_OUTPUT_SUBDIR animals)
set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/${DOXYGEN_OUTPUT_SUBDIR})
set(DOXYGEN_INDEX_FILE ${DOXYGEN_OUTPUT_DIR}/html/index.html)
set(DOXYFILE_IN ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in)
set(DOXYFILE_OUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile)
set(DOXYGEN_GENERATE_TAGFILE "${DOXYGEN_OUTPUT_SUBDIR}/html/tagfile.xml")

#Replace variables inside @@ with the current values
configure_file(${DOXYFILE_IN} ${DOXYFILE_OUT} @ONLY)

file(MAKE_DIRECTORY ${DOXYGEN_OUTPUT_DIR}) #Doxygen won't create this for us
add_custom_command(OUTPUT ${DOXYGEN_INDEX_FILE}
                   DEPENDS ${PUBLIC_HEADERS}
                   COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYFILE_OUT}
                   MAIN_DEPENDENCY ${DOXYFILE_OUT} ${DOXYFILE_IN}
                   COMMENT "Generating docs"
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

add_custom_target(doxygen ALL DEPENDS ${DOXYGEN_INDEX_FILE} WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})

set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR}/sphinx)

add_custom_target(Doxysphinx ALL
    COMMAND
        ${DOXYSPHINX_EXECUTABLE} build ${SPHINX_SOURCE} ${SPHINX_BUILD} ${DOXYFILE_OUT}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    DEPENDS doxygen
)

add_custom_target(Sphinx ALL
                  COMMAND
                  ${SPHINX_EXECUTABLE} -b html
                  ${SPHINX_SOURCE} ${SPHINX_BUILD}
                  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                  DEPENDS Doxysphinx
                  COMMENT "Generating documentation with Sphinx")
