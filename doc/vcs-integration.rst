VCS Integration
***************

About
=====

Version tools supports a form of version control system integration.
This code is *only* triggered for development versions of your project
(indicated by setting ``releaselevel`` to something other than ``"final"``)

.. note::
    Currently to use :abbr:`VCS (Version Control System)` integration you
    *must* use the name __version__ in your variable name and you *must* define
    it at module level.  There is some fuzzy logic that walks the traceback
    looking for ``__version__``.


VCS Integration Plugins
=======================

VCS integration is not hard-coded into versiontools. Instead any package that
uses setuptools and provides an entry point ``versiontools.vcs_integration``
can add support for integration with additional version control systems.

To see how to implement this API refer to the bundled plug-in for bzr
:class:`versiontools.bzr_support.BzrIntegration`.


Supported VCSes
***************

Bazaar
======

Version tools comes bundles with support for bazaar via the
:class:`~versiontools.bzr_support.BzrIntegration` class.

