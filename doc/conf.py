# -*- coding: utf-8 -*-
#
# graph-tool documentation build configuration file, created by
# sphinx-quickstart on Sun Oct 26 18:29:16 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed
# automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

if sys.version_info < (3,):
    reload(sys)
    sys.setdefaultencoding("Cp1252")

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.intersphinx', 'mathjax', 'sphinx.ext.autosummary',
              'numpydoc',
              'sphinx.ext.extlinks',
              'sphinx.ext.viewcode'
              #'sphinx.ext.linkcode'
              #'matplotlib.sphinxext.plot_directive'
              ]

mathjax_path = "MathJax/MathJax.js?config=default"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'graph-tool'
copyright = u'2016, Tiago de Paula Peixoto <tiago@skewed.de>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from graph_tool import __version__ as gt_version
version = gt_version.split()[0]
# The full version, including alpha/beta/rc tags.
release = gt_version.split()[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['.build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# doctest

doctest_global_setup = open("pyenv.py").read()
doctest_global_setup += "os.chdir('%s')\n" % os.getcwd()

# Options for HTML outputs
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
# html_style = 'default.css'

html_theme = "gt_theme"
html_theme_path = ["."]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "graph-icon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = 'http://graph-tool.skewed.de/doc/'

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'graph-tooldoc'


# Options for LaTeX output
# ------------------------

# Grouping the document tree into LaTeX files. List of tuples (source start
# file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'graph-tool.tex', ur'graph-tool documentation',
   ur'Tiago de Paula Peixoto', 'manual'),
]

latex_preamble = """
\setcounter{tocdepth}{2}
"""

latex_show_pagerefs = True
latex_show_urls = False
latex_paper_size = "a4"

latex_logo = "blockmodel.pdf"

latex_elements = {
    'papersize': "a4paper",
    'fontpkg': r"\usepackage{bookman}"}

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('http://docs.scipy.org/doc/numpy', None),
                       'scipy': ('http://docs.scipy.org/doc/scipy/reference', None),
                       'matplotlib': ('http://matplotlib.org', None),
                       'cairo': ('https://www.cairographics.org/documentation/pycairo/3', None),
                       'ipython': ('http://ipython.org/ipython-doc/stable/', None),
                       'panda': ('http://pandas.pydata.org/pandas-docs/stable/', None)}

extlinks = {'ticket': ('http://graph-tool.skewed.de/tickets/ticket/%s',
                       'ticket '),
            'doi': ('http://dx.doi.org/%s', 'DOI: '),
            'arxiv': ('http://arxiv.org/abs/%s', 'arXiv: ')}


# def process_docstring(app, what, name, obj, options, lines):
#     for i, line in enumerate(lines):
#         if "arg1" in line and "->" in line:
#             lines[i] = ""
#         if "C++ signature :" in line or "graph_tool::Python" in line:
#             lines[i] = ""

# def setup(app):
#     app.connect('autodoc-process-docstring', process_docstring)

# plot directive
import pyenv
plot_rcparams = pyenv.rcParams
#plot_pre_code = open("pyenv.py").read()

autodoc_default_flags = ['members', 'undoc-members']
numpydoc_show_class_members = False
autodoc_docstring_signature = False
autodoc_member_order = 'bysource'
autoclass_content = 'both'
imported_members = True

def linkcode_resolve(domain, info):
    if domain != 'py':
        return None
    if not info['module']:
        return None
    modname = info['module'].replace('.', '/')
    return "https://git.skewed.de/count0/graph-tool/tree/master/src/%s/__init__.py" % modname
