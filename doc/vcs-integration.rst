VCS Integration
***************

About
=====

Version tools supports a form of version control system integration.
This code is *only* triggered for development versions of your project
(indicated by setting ``releaselevel`` to ``"dev"``) that have a default
value (``None``) for ``serial`` (last component of the version tuple).

When both conditions are true :abbr:`VCS (Version Control System)` integration
plug-in attempts to obtain the revision number of the source tree and use it
instead of the serial number. This way the tree revision is incremented on
every commit. This is useful for embedding the true version inside generated
content such as release tarballs or documentation.

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

