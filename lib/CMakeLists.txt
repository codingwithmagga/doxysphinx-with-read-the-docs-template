cmake_minimum_required(VERSION 3.24)

project(animals VERSION ${PROJECT_VERSION} LANGUAGES CXX C)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS TRUE)

add_library(animals SHARED 
        src/cat.cpp
        src/dog.cpp
    )

target_include_directories(animals
    PUBLIC
        include
)

add_library(doctemplate::animals ALIAS animals)
