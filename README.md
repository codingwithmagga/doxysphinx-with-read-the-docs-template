# Documentation Template

Template project to use [doxygen](https://www.doxygen.nl/), [doxysphinx](https://github.com/boschglobal/doxysphinx), [doxylink](https://github.com/sphinx-contrib/doxylink), [Sphinx](https://www.sphinx-doc.org/en/master/) and [Read the Docs](https://about.readthedocs.com/) for project documentation. As an example, a C++ library is added to this project (see `libs` folder) using CMake. The documentation can either be automatically build using CMake targets or locally using the terminal.

Take a look at the Read the Docs documentation [here](https://doxysphinx-with-read-the-docs-template.readthedocs.io/en/latest/). You can also find additional information about the build process there.

## Key features

* Combine [doxygen](https://www.doxygen.nl/), [doxysphinx](https://github.com/boschglobal/doxysphinx), [doxylink](https://github.com/sphinx-contrib/doxylink), [Sphinx](https://www.sphinx-doc.org/en/master/) and [Read the Docs](https://about.readthedocs.com/) for online documentation
* Automated Online Documentation Build Process on Read the Docs server
* Automated Offline Documentation Build Process using CMake

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

## Additional References

[Microsoft devblog](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/) - Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake

