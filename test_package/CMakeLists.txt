cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

add_compile_options(
  "$<$<COMPILE_LANGUAGE:CXX>:-std=c++17>"
)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

enable_testing()
add_test(NAME example
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND example)
