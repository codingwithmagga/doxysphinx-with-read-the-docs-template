# doxysphinx-with-read-the-docs-template

Template project to use doxygen, doxysphinx, doxylink and read the docs for project documentation. As an example a C++ library is added to this project (see `libs` folder) using CMake. The whole documentation process is also added using CMake targets to generate the documentation locally. In the documentation it is also shown how to create a local documentation without using CMake at all.

## Prerequisites for this project

### Documentation without CMake

* **doxygen** - found at [https://www.doxygen.nl/](https://www.doxygen.nl/)

* **doxysphinx** - found at [https://github.com/boschglobal/doxysphinx](https://github.com/boschglobal/doxysphinx)

* **doxylink** - found at [https://github.com/sphinx-contrib/doxylink](https://github.com/sphinx-contrib/doxylink)

* **sphinx** - found at [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)

### Local CMake documentation

If you want to create the local documentation using CMake also the following requirements are necessary:

* **CMake v3.24+** - found at [https://cmake.org/](https://cmake.org/)

* **C++ Compiler** - i.e. *MSVC*, *GCC*, *Clang*

> ***Note:*** *You also need to be able to provide a ***CMake*** supported
[generator](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html).*

## References

[Microsoft devblog](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/) - Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake

