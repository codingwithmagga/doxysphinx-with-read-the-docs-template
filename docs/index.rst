.. _Home:

Welcome to this template documentation!
=======================================

.. toctree::
    :maxdepth: 2
    :titlesonly:
    
    Home <self>
    build_process
    Doxygen Main <animals/html/index>

This repository shows how to use a combination of `doxygen <https://www.doxygen.nl/>`_, `doxysphinx <https://github.com/boschglobal/doxysphinx>`__, `doxylink <https://github.com/sphinx-contrib/doxylink>`_, `Sphinx <https://www.sphinx-doc.org/en/master/>`_, and `Read the Docs <https://about.readthedocs.com/>`_ to create online documentation. :ref:`Build Process` shows additional information about the documentation build process online and offline, either with or without using CMake. The created doxygen online documentation can be accessed by following this :doc:`/animals/html/index` link or the "Doxygen Main" link on the left side or above this text. In the following, you will find some short information about the mentioned tools and the configuration used.

Doxygen
+++++++
Doxygen is a powerful tool for automatically generating documentation from annotated source code in various programming languages, including C++, C, Java, Python, and more. It parses source code files and extracts documentation comments marked with special tags, typically in a format like Javadoc or Qt-style comments.

In this template project a small C++ library is documented using doxygen. Take a look at the header files in the `lib/include` folder to see them live. Using all these tools, the created doxygen documentation will be integrated into Sphinx-Read-the-Docs online documentation. To achieve this, some configurations have to be changed from the default doxygen configuration file. In this project the recommendations from `doxysphinx <https://github.com/boschglobal/doxysphinx/blob/main/docs/getting_started.md#mandatory-settings>`__ are used.  You can take a look at the used doxygen configuration file in `docs/Doxyfile.in`. 

Doxysphinx
++++++++++

Doxysphinx is a Doxygen and Sphinx integration tool. It is an easy-to-use CLI tool that usually runs immediately after Doxygen generation. It reuses the Doxygen-generated HTML output and incorporates it into Sphinx document generation. Doxysphinx supports all known Doxygen features and integrates well with the Sphinx output (for example, themes, search, etc.). Doxysphinx also supports restructured text annotations (RST) within C++ files.

As stated above, the recommended doxygen settings from `doxysphinx <https://github.com/boschglobal/doxysphinx/blob/main/docs/getting_started.md#mandatory-settings>`__ are used in this project. Other than that, no special configuration is used for Doxysphinx.

Doxylink
++++++++

Doxylink serves as a Sphinx extension designed to facilitate linking to external Doxygen API documentation. This feature enables users to specify C++ symbols, which are then automatically transformed into hyperlinks directing to their corresponding HTML pages within the Doxygen documentation.

In this project it is used to create links between the Sphinx-generated online documentation based on restructured text (RST) files and the doxygen documentation. Using doxylink you can, for example, create links like this:

* classes: :animals:`Cat`
* methods: :animals:`Dog::eat`

Sphinx
++++++

Sphinx is a versatile documentation generation tool primarily used for Python projects but applicable to various programming languages. It converts source files written in formats like reStructuredText or Markdown into different output formats, such as HTML or PDF. Sphinx automates the process of creating documentation, including API references, cross-referencing between different sections, and customization of appearance. It streamlines the documentation workflow, ensuring projects are well-documented and accessible to users. 

Sphinx is used in this project to create nicely structured and organized HTML-based documentation. Take a look at the ``docs/*.rst`` files to get an insight into the input files used by Sphinx. The configuration of Sphinx is stored in ``docs/conf.py``. In this file are additional comments for clarification, and also the most important parts are described under :ref:`Build Process`. 

Read the Docs
+++++++++++++

Read the Docs can be used to build, host, and share documentation. It can be used for free for open source and community projects, but there are also premium membership options as well as business packages. 

The online Read the Docs build process is configured in the file ``.readthedocs.yaml``. In this project the build process using Sphinx and all the other tools is automated on the platform and will be published automatically.
