.. _code_reference:

Code reference
**************

Version class
^^^^^^^^^^^^^

.. autoclass:: versiontools.Version
    :members:


Utility functions
^^^^^^^^^^^^^^^^^

.. :func: versiontools.format_version

Bazaar Integration
^^^^^^^^^^^^^^^^^^

.. autoclass:: versiontools.bzr_support.BzrIntegration
    :members: from_source_tree, revno, branch_nick

Git Integration
^^^^^^^^^^^^^^^

.. autoclass:: versiontools.git_support.GitIntegration
    :members: from_source_tree, revno, branch_nick
