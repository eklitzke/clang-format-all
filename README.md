# Format All The Things!

This is a bash script that will run `clang-format -i` on your code.

Features:

 * finds the right path to `clang-format` on Ubuntu/Debian, which encode the
   LLVM version in the `clang-format` filename
 * finds files recursively
 * detects most extensions commonly used by C/C++ projects

Basic usage:

    clang-format-all src/

Advanced usage:

    clang-format-all project1/ project2/ project3/
