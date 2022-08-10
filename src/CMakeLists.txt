cmake_minimum_required(VERSION 3.22)
project(arrays)

set(CMAKE_CXX_STANDARD 23)
add_subdirectory(./googletest-release-1.12.1)

set(LIBRARIES gtest pthread)

set(SOURCE_EXE main.cpp SingleArray/SingleArray.cpp SingleArray/SingleArray.hpp)

add_library(SingleArray SingleArray/SingleArray.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_EXE})

target_link_libraries(${PROJECT_NAME} SingleArray)
target_link_libraries(${PROJECT_NAME} ${LIBRARIES})