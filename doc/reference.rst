.. _code_reference:

Code reference
**************

Version class
^^^^^^^^^^^^^

.. autoclass:: versiontools.Version
    :members:
        __new__, major, minor, micro, releaselevel, serial, from_tuple,
        from_tuple_and_hint, vcs,  __str__


Utility functions
^^^^^^^^^^^^^^^^^

Instead of using :class:`~versiontools.Version` class directly you may want to
use the simplified interface where you simply interpret an arbitrary
five-element version tuple as a version to get the pretty and
:pep:`386`-compliant version string. In that case you may be interested in
this function:

.. autofunction:: versiontools.format_version


Integration with setuptools 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setuptools has a framework where external packages, such as versiontools, can
hook into setup.py metadata and commands. We use this feature to intercept
special values of the `version` keyword argument to `setup()`. This argument
handled by the following method:

.. autofunction:: versiontools.handle_version


Integration with version control systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following version control integration plugins are bundled with
versiontools. Additional plugins may be provided by third party modules but
they are not documented here.


Bazaar
++++++

.. autoclass:: versiontools.bzr_support.BzrIntegration
    :members: from_source_tree, revno, branch_nick


Git
+++

.. autoclass:: versiontools.git_support.GitIntegration
    :members: from_source_tree, revno, branch_nick


Hg (Mercurial)
++++++++++++++

.. autoclass:: versiontools.hg_support.HgIntegration
    :members: from_source_tree, revno, branch_nick

