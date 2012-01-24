===========================
Version Tools Documentation
===========================

.. automodule:: versiontools

.. seealso:: To get started quickly see :ref:`usage`
.. seealso:: See what's new in :ref:`version_1_8_3`

.. note::
    This document may be out of date, the bleeding edge version is always
    available at http://versiontools.rtfd.org/

Features
========

* Keep a *single version definition* inside your package or module
* Get proper versioning of development snapshots coupled with your :abbr:`VCS
  (Version Control System)` (pluggable support for additional systems
  available). Git, Mercurial and Bazaar are supported out of the box.
* Produce nice version strings for released files that are compliant
  with :pep:`386`
* Remain comparable as tuple of integers

How version tuple affects version string
========================================

This is pulled from the documentation of the string method on the
:class:`~versiontools.Version` class. In general you don't need to explicitly
use that class to benefit from this system. To learn more check the
:ref:`usage` section.

.. automethod:: versiontools.Version.__str__
    :noindex:

Indices and tables
==================

.. toctree::
    :maxdepth: 2
    
    installation.rst
    usage.rst
    vcs-integration.rst
    changes.rst
    reference.rst

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

