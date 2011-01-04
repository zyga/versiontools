Version History
***************

.. _version_1_0_4:

Version 1.0.4
=============

* Add support to obtain VCS integration object via
  :data:`~versiontools.Version.vcs` attribute
* Add support to obtain branch nickname from :class:`~versiontools.bzr_support.BzrIntegration` (via
  :data:`~versiontools.bzr_support.BzrIntegration.branch_nick` property)
* Add :ref:`code_reference`.


Version 1.0.3
=============

* Don't crash when :class:`ImportError` occurs during VCS integration
  initialization

Version 1.0.2
=============

* Add documentation
* Fix chicken-and-egg problem so that packages can now depend on
  versiontools and still be installed correctly with pip


Version 1.0.1
=============

* Make VCS integration more robust in the way it locates source tree


Version 1.0
===========

* Initial release
