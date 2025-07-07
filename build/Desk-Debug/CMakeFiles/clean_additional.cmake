# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/Optimiser_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/Optimiser_autogen.dir/ParseCache.txt"
  "Optimiser_autogen"
  )
endif()
