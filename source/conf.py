# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SDP User Guide'
copyright = '2022-2024, Xiang Liu(刘祥)@ASIPP'
author = 'Xiang Liu'
release = '0.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sphinx_rtd_theme
 
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel']

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

rst_epilog = """
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# by ChatGPT 3.5, used to copy unreferenced image into _images folder under build/html 

import os
import shutil

# Configure a pre-build function to copy unused images
def copy_unused_images(app, exception):
    source_image_dir = os.path.join(app.builder.srcdir, 'pic')
    build_image_dir = os.path.join(app.builder.outdir, '_images')

    # Create the destination directory (if it doesn't exist)
    os.makedirs(build_image_dir, exist_ok=True)

    # Get all the referenced image files
    referenced_images = set()
    for docname in app.env.found_docs:
        doctree = app.env.get_doctree(docname)
        for image_node in doctree.traverse(condition=lambda node: node.tagname == 'image'):
            if 'uri' in image_node.attributes:
                referenced_images.add(image_node.attributes['uri'])

    # Traverse the source image directory and copy unreferenced images to the build directory
    for filename in os.listdir(source_image_dir):
        source_image_path = os.path.join(source_image_dir, filename)
        build_image_path = os.path.join(build_image_dir, filename)

        if filename not in referenced_images:
            shutil.copyfile(source_image_path, build_image_path)

# Associate the pre-build function with the Sphinx build process
def setup(app):
    app.connect('build-finished', copy_unused_images)
