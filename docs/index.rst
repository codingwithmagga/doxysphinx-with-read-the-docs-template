Welcome to this template documentation!
=======================================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    
    Home <self>
    local_doc
    Doxygen Main <animals/html/index>

This repository shows how to use a combination of `doxygen <https://www.doxygen.nl/>`_, `doxysphinx <https://github.com/boschglobal/doxysphinx>`__, `doxylink <https://github.com/sphinx-contrib/doxylink>`_, `Sphinx <https://www.sphinx-doc.org/en/master/>_` and `Read the Docs <https://about.readthedocs.com/>`_ to create an online documentation. In the following you find some short information about the mentioned tools and the used configuration.

Doxygen
+++++++
Doxygen is a powerful tool for automatically generating documentation from annotated source code in various programming languages, including C++, C, Java, Python, and more. It parses source code files and extracts documentation comments marked with special tags, typically in a format like Javadoc or Qt-style comments.

In this template project a small C++ library is documented using doxygen. Have a look into the header files in the `lib/include` folder to see it live. Using all these tools the created doxygen documentation will be integrated into Sphinx-Read-the-Docs online documentation. To achieve this, some configurations have to be changed from the default Doxyfile. In this project I follow the recommendations from `doxysphinx <https://github.com/boschglobal/doxysphinx/blob/main/docs/getting_started.md#mandatory-settings>`__.  You can have a look at the used doxygen configuration file in `docs/Doxyfile.in`. 

Doxysphinx
++++++++++

From the Doxysphinx repository: Doxysphinx is a Doxygen and Sphinx integration tool. It is an easy-to-use cli tool and typically runs right after Doxygen generation. It reuses the Doxygen generated HTML output and integrates it into Sphinx document generation. With this, Doxysphinx supports all known Doxygen features and at the same time integrates well with the Sphinx output (for example, Sphinx-Themes, search etc.). Doxysphinx, also supports restructured text (rST) annotations within C++ files.

As stated above the recommended doxygen settings from `doxysphinx <https://github.com/boschglobal/doxysphinx/blob/main/docs/getting_started.md#mandatory-settings>`__ are used in this project. Other than that no special configuration is used.

Doxylink
++++++++

Sphinx
++++++

Read the Docs
+++++++++++++

Online documentation
++++++++++++++++++++

The created doxygen online documentation can be accessed by following this :doc:`/animals/html/index` link or the "Doxygen Main" link on the left side. Using doxylink you can also directly link to 

* classes: :animals:`Cat`
* methods: :animals:`Dog::eat`
