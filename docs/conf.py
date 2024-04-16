# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import subprocess
import os
from pathlib import Path

lib_name = "animals"


def get_output_dir():
    read_the_docs_build_folder = Path(os.environ.get("READTHEDOCS_OUTPUT", None))
    main_folder = read_the_docs_build_folder.parent.absolute()
    output_dir = main_folder / "docs" / lib_name

    return output_dir


def configureDoxyfile(input_dir, output_dir):
    with open("Doxyfile.in", "r") as file:
        filedata = file.read()

    filedata = filedata.replace("@DOXYGEN_INPUT_DIR@", input_dir)
    filedata = filedata.replace("@DOXYGEN_OUTPUT_DIR@", output_dir)
    filedata = filedata.replace(
        "@DOXYGEN_GENERATE_TAGFILE@", lib_name + "/html/tagfile.xml"
    )

    with open("Doxyfile", "w") as file:
        file.write(filedata)


# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get("READTHEDOCS", None) == "True"

if read_the_docs_build:
    read_the_docs_build_folder = Path(os.environ.get("READTHEDOCS_OUTPUT", None))
    input_dir = ".."
    output_dir = get_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    configureDoxyfile(input_dir, output_dir.absolute().as_posix())
    cwd = os.path.dirname(os.path.realpath(__file__))
    subprocess.call(["doxygen", "Doxyfile"], shell=False, cwd=cwd)
    subprocess.call(
        ["doxysphinx", "build", ".", read_the_docs_build_folder / "html", "Doxyfile"],
        shell=False,
        cwd=cwd,
    )


# -- Project information -----------------------------------------------------

project = "Documentation Template"
copyright = "2024, CodingWithMagga"
author = "CodingWithMagga"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# ...

extensions = [
    "sphinx.ext.graphviz",
    "sphinxcontrib.doxylink",
]

doxylink = {lib_name: (lib_name + "/html/tagfile.xml", lib_name + "/html")}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# For code highlighting
pygments_style = "sphinx"
