Version Tools Documentation
===========================

.. seealso:: To get started quickly see :ref:`usage`
.. seealso:: See what's new in :ref:`version_1_9_1`

.. note::
    This document may be out of date, the bleeding edge version is always
    available at http://versiontools.rtfd.org/

Installation
============

This package is being actively maintained and published in the `Python Package
Index <http://http://pypi.python.org>`_. You can install it if you have `pip
<http://pip.openplans.org/>`_ tool using just one line::

    $ pip install versiontools

Features
========

* A piece of code that allows you to keep a **single version definition**
  inside your package or module. No more hacks in setup.py, no more
  duplicates in setup.py and somewhere else. Just **one** version per
  package.
* :class:`~versiontools.Version` objects can produce nice version strings for
  released files that are compliant with :pep:`386`. Releases, alphas, betas,
  development snaphots. All of those get good version strings out of the box.
* Version objects understand the :abbr:`VCS (Version Control System)` used by
  your project. Git, Mercurial and Bazaar are supported out of the box.
  Custom systems can be added by 3rd party plugins.
* Version object that compares as a tuple of values and sorts properly.
* Zero-dependency install! If all you care about is handling setup() to get
  nice tarball names then you don't need to depend on versiontools (no
  setup_requires, no install_requires!). You will need to bundle a small
  support module though.

__version__ to string conversion
================================

This is pulled from the documentation of the string method on the
:class:`~versiontools.Version` class. In general you don't need to explicitly
use that class to benefit from this system. To learn more check the
:ref:`usage` section.

.. automethod:: versiontools.Version.__str__
    :noindex:

.. note::
    This logic is implemented in :meth:`versiontools.Version.__str__()`
    and can be overridden by sub-classes. You can use project-specific
    logic if required. To do that replace __version__ with an instance
    of your sub-class.

Indices and tables
==================

.. toctree::
    :maxdepth: 3
    
    usage.rst
    vcs-integration.rst
    reference.rst
    changes.rst

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

