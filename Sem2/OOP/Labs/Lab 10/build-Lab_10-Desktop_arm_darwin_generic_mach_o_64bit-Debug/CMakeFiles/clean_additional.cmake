# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/Lab_10_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/Lab_10_autogen.dir/ParseCache.txt"
  "Lab_10_autogen"
  )
endif()
