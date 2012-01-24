Version History
***************

.. _version_1_8_3:

Version 1.8.3
=============

* Fix incorrectly specified line in git support. Previosuly a KeyError
  may bleed to the outside calling code, depending on python version. 

* Fix incorrectly specified line in bzr support. Previously a non-bzr
  directory could be associated as a malformed bzr branch.

.. _version_1_8_2:

Version 1.8.2
=============

 * Improve git support by adding code paths compatible with python-git 0.1.6 (which
   is easier to get on Debian)
 * Change git support to default to short commit id. If you want to access the
   long commit id you need to access it directly as GitIntegration.commit_id

.. _version_1_8_1:

Version 1.8.1
=============

 * Improve performance when working with checkouts. The use of branch.nick has
   been replaced with branch._get_nick(local=True). This avoids network
   operations and is much more responsive.

.. _version_1_8:

Version 1.8
===========

 * Fixed all pep8 issues (prettier syntax)

 * Fixed an issue with using __import__ on Python 2.4.

 * Fixed an issue with using :versiontools:path.to.symbol with nested modules

 * Fixed an issue with using exceptions on Python 3.x

 * Added test that demostrated that exception handling works on all Python versions.

 * Unified error handling across version control plugins.

 * General documentation improvements, installation, usage, code refrerence,
   and writing additional plug-ins.

 * Added a *backwards incompatible* constraint on serial to be greater than
   zero on alpha, beta and release candidates as required by :pep:`386`.

.. _version_1_7:

Version 1.7
===========

* Add support for Mercurial repositories

* Fix a bug in exception handling that affected 1.6

.. _version_1_6:

Version 1.6
===========

* Add support for python2.4 and python2.5 thanks to Jannis Leidel (thanks!).

* Add tox (http://codespeak.net/~hpk/tox/) configuration file for easier
  testing.

.. _version_1_5:

Version 1.5
===========

* Added Git support, contributed by Jannis Leidel (thanks!). To use it you need
  GitPython >= 0.3.2.RC1. It does not currently work on GitPython packaged in
  Ubuntu Natty (0.1.6). 

.. _version_1_4:

Version 1.4
===========

* Work harder to figure out the source tree a __version__ object comes from.
  This is possible with a new function
  :meth:`versiontools.Version.from_tuple_and_hint`.

* Allow people to omit the version identifier in setup.py (defaulting to
  ``__version__``) 

.. _version_1_3_2:

Version 1.3.2
=============

* Change version string produced by :meth:`versiontools.Version.__str__` and
  `versiontools.format_version` to be more useful when vcs integration is not
  available and the release is not final. Consult the table below for details.

  +----------------------+----------------------+--------------------------------+
  | Prior to 1.3.2       | 1.3.2                | Comment                        |
  +======================+======================+================================+
  | ``1.2.3``            | ``1.2.3.dev``        | When releaselevel==dev but     |
  |                      |                      | VCS integration is not         |
  | When VCS integration |                      | available we now add a .dev    |
  | is not available     |                      | suffix to differentiate from   |
  |                      |                      | released versions              |
  +----------------------+----------------------+--------------------------------+
  | ``1.2.3a5`` or       | ``1.2.3a5``          | ``.devREVNO`` is only added    |
  | ``1.2.3a5.devREVNO`` | `                    | when releaselevel==dev.        |
  +----------------------+----------------------+                                |
  | ``1.2.3b5`` or       | ``1.2.3b5``          | It will never appear on alphas |
  | ``1.2.3b5.devREVNO`` |                      | , betas or release candidates. |
  +----------------------+----------------------+                                |
  | ``1.2.3c5`` or       | ``1.2.3c5``          |                                |
  | ``1.2.3c5.devREVNO`` |                      |                                |
  +----------------------+----------------------+--------------------------------+

.. _version_1_3_1:

Version 1.3.1
=============

* To make `setup.py test` work in third party components we cannot use
  versiontools in our own setup.

.. _version_1_3:

Version 1.3
===========

* Add integration with setuptools (or more accurately, distribute) so that you
  no longer have to try-import versiontools. This means that you may finally
  install your packages with pip and everything will work correctly.

* Prevent an unexplained crash when following the backtrace in
  ``Version._find_source_tree()``.

.. seealso:: To get started quickly see :ref:`using_versiontools`

.. _version_1_2:

Version 1.2
===========

* Change how vcs objects are constructed. With this change they are only
  constructed lazily when needed.  This speeds up common operations, delays the
  time any additional modules are imported (if any) and retains backwards comp
  ability.

* Updated documentation on installation instructions to point to the new PPA

* Updated recommended usage guide so that installed programs do not depend on
  versiontools. This allows you to use versiontools in setup.py and still
  benefit from the smart version formatting and keep your deployment
  lightweight.

* Added basic unit tests

* Fixed most PEP8 issues

.. _version_1_1:

Version 1.1
===========

* Change version string produced by
  :meth:`versiontools.Version.__str__` to be compatible with :pep:`386`
  The following table shows how old versions map to new versions:

  +-----------------------+----------------------+--------------------------------+
  | Old Version           | New Version          | Comment                        |
  +=======================+======================+================================+
  | ``1.2``               | ``1.2``              |                                |
  +-----------------------+----------------------+--------------------------------+
  | ``1.2.3``             | ``1.2.3``            |                                |
  +-----------------------+----------------------+--------------------------------+
  | ``1.2.3.dev.5``       | ``1.2.3.devREVNO``   | VCS revision and serial are    |
  |                       |                      | two distinct fields. Serial    |
  |                       |                      | is no longer displayed for     |
  |                       |                      | development releases.          |
  +-----------------------+----------------------+--------------------------------+
  | ``1.2.3.alpha.5``     | ``1.2.3a5`` or       | ``.devREVNO`` is only added    |
  |                       | ``1.2.3a5.devREVNO`` | when VCS integration is        |
  +-----------------------+----------------------+ available.                     |
  | ``1.2.3.beta.5``      | ``1.2.3b5`` or       |                                |
  |                       | ``1.2.3b5.devREVNO`` |                                |
  +-----------------------+----------------------+                                |
  | ``1.2.3.candidate.5`` | ``1.2.3c5`` or       |                                |
  |                       | ``1.2.3c5.devREVNO`` |                                |
  +-----------------------+----------------------+--------------------------------+

* Add :func:`versiontools.format_version` that converts a 5-element
  tuple to a proper version string and is more obvious in intent. 
* Change default of Version releaselevel to "final"
* Change default of Version serial to 0
* Serial field is no longer initialized with revision number from vcs,
  instead it is used to count alphas, betas and release candidates.
* All version components except for releaselevel must be non-negative
  integers or strings that can be converted to such integers
* Do not warn about "directory foo is not a bzr branch". This message
  was changed to debug as it is now legitimate for released code not to
  have bzr version control files.

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
