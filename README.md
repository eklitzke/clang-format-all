# Format All The Things!

This is a bash script that will run `clang-format -i` on your code.

Features:

 * finds the right path to `clang-format` on Ubuntu/Debian, which encode the
   LLVM version in the `clang-format` filename
 * fixes files recursively
 * detects most the file extensions commonly used by C/C++ projects

Basic usage:

    clang-format-all src/

Advanced usage:

    clang-format-all project1/ project2/ project3/

**Note:** While `clang-format` is a powerful tool for enforcing a consistent
coding standard, you should be aware that different versions of `clang-format`
may format the same code differently. As one example that I know of, in C++ long
vector or set literals (say, a dozen elements or more) in `clang-format` 3.7 are
generally formatted with one entry per line, but under `clang-format` 3.5 the
same literals may be formatted with multiple entries per line if the entries are
short enough.
