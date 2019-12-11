:mod:`editpyxl` - A Python library to edit Excel 2007 xlsx/xlsm files
===========================================================================

.. module:: editpyxl
.. moduleauthor:: Adam Morris

:Author: Adam Morris
:Source code: http://bitbucket.org/amorris/editpyxl/src
:Issues: http://bitbucket.org/amorris/editpyxl/issues
:Generated: |today|
:License: MIT/Expat
:Version: |release|

Introduction
------------

Editpyxl is a Python library to non-destructively edit Excel 2010 xlsx/xlsm files.

The purpose is to edit excel files without otherwise modifying the excel document, to allow for efficient and quick
edits of an excel file.

Many thanks to openpyxl for their hard work in developing a tool to read and writing excel files.
https://bitbucket.org/ericgazoni/openpyxl


A Note on Limitations
---------------------

Excel 2007+ is an XML format.  This library loads the necessary XML documents, edits them, and saves them back
to disk.

Currently, it is only possible to edit cells which exist.  Editpyxl does not add or delete cells.

Further, string editing is limited!  Excel stores all cell strings in a shared table, so if you edit a piece of text
 which is the same in multiple cells, changing one cell will change all the cells with the shared text.



How to Contribute Code
----------------------

Any help will be greatly appreciated, just follow those steps:

    1. Please start a new fork
    (https://bitbucket.org/amorris/editpyxl/fork) for each independent
    feature, don't try to fix all problems at the same time, it's easier for
    those who will review and merge your changes ;-)

    2.
    Hack hack hack

    3. Don't forget to add unit tests for your changes ! (YES, even if it's a
    one-liner, or there is a high probability your work will not be taken
    into consideration). There are plenty of examples in the /test directory
    if you lack know-how or inspiration.

    4. If you added a whole new feature, or just improved something, you can
    be proud of it, so add yourself to the AUTHORS file :-)

    5.
    Let people know about the shiny thing you just implemented, update the docs !

    6. When it's done, just issue a pull request (click on the large "pull
    request" button on *your* repository) and wait for your code to be
    reviewed, and, if you followed all theses steps, merged into the main
    repository.


This is an open-source project, maintained by volunteers on their spare time,
so while we try to work on this project as often as possible, sometimes life
gets in the way. Please be patient.

Other ways to help
------------------

There are several ways to contribute, even if you can't code (or can't code well):

    - adding bugs on the bug tracker: closing bugs that have already been
      closed, are not relevant, cannot be reproduced, ...

    - updating documentation in virtually every area: many large features have
      been added (mainly about charts and images at the moment) but without any
      documentation, it's pretty hard to do anything with it

    - proposing compatibility fixes for different versions of Python: we support
      2.6 to 3.3, so if it does not work on your environment, let us know :-)


Installation
------------

The best method to install editpyxl is using a PyPi client such as
easy_install (setuptools) or pip. It is advisable to do this in a Python
virtualenv without system packages::

    $ pip install editpyxl

or ::

    $ easy_install editpyxl

.. note::

    To install from sources (there is nothing to build, editpyxl is 100% pure
    Python), you can download an archive from `bitbucket`_ (look in the
    "tags" tab).

    There is support for the popular `lxml`_ library which will be used if it is installed.

    After extracting the archive, you can do::

    $ python setup.py install

.. _bitbucket: https://bitbucket.org/amorris/editpyxl/downloads
.. _lxml: http://lxml.de


Getting the source
------------------

Source code is hosted on bitbucket.org. You can get it using a Mercurial client and the following URLs:

    * $ hg clone \https://bitbucket.org/amorris/editpyxl -r |release|

or to get the latest development version:

    * $ hg clone \https://bitbucket.org/amorris/editpyxl


Usage examples
--------------

Cookbook
++++++++

.. toctree::

    usage


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
