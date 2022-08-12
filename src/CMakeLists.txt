cmake_minimum_required(VERSION 3.22)
project(arrays)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
add_subdirectory(./googletest-release-1.12.1)

set(LIBRARIES gtest pthread)

set(SOURCE_EXE SingleArray/SingleArray.cpp
        VectorArray/VectorArray.cpp FactorArray/FactorArray.cpp PriorityQueue/PriorityQueue.cpp)

add_library(Arrays ${SOURCE_EXE})

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} Arrays)
target_link_libraries(${PROJECT_NAME} ${LIBRARIES})