import os
import sys
sys.path.insert(0,os.path.abspath('../color'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ColorDetection'
copyright = '2023, ZaheenSystems'
author = 'ZaheenSystems'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

autodoc_mock_imports = ['cv2', 'numpy', 'sklearn', 'pandas', 'webcolors', 'Detections']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
