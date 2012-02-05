Integration with version control
********************************

versiontools supports a form of version control system integration. This code
is *only* triggered for development versions of your project (indicated by
setting ``releaselevel`` to ``dev"``)

In development mode the generated version string will include the revision
number or the abbreviated hash of the current commit. This makes it nice for
ongoing releases on pypi as after each commit your source tarballs will be
different.

Batteries included
==================

The following version control systems are supported out of the box.  To use
them you need to have the corresponding libraries installed. Check the links
below for details.

.. note:
    Users of your packages will *not* need those libraries. They are most
    useful for the developer during project life-cycle, especially between
    releases, to identify tarballs easily.

Bazaar
++++++

Using bazaar appends the branch revision to the version string. See :ref:`bzr` 

Git
+++

Using git appends the short commit id of the active branch. See :ref:`git` 

Mercurial
+++++++++

Mercurial plug-in appends the branch revision to the development version. See :ref:`hg`

Custom version control systems
==============================

VCS integration is not hard-coded into versiontools. Instead any package that
uses setuptools and provides an entry point ``versiontools.vcs_integration``
can add support for integration with additional version control systems.

To see how to implement this simple API refer to the bundled plug-in for
Bazaar :class:`~versiontools.bzr_support.BzrIntegration`,
Git :class:`~versiontools.git_support.GitIntegration`
or Mercurial :class:`~versiontools.hg_support.HgIntegration`.

To make versiontools aware of additional plug-ins they need to be registered in
the entry points database. To do that make sure your package uses setuptools
and put the following snippet into your ``setup.py``::

    setup(
        name="foo",
        description="The imaginary foo version control system",
        entry_points="""
        [versiontools.vcs_integration]
        foo=foo.versiontools_plugin:FooIntegration
        """
        )

This will make versiontools look for the ``foo`` system by importing
``foo.versiontools_plugin`` and extracting the ``FooIntegration`` class.
Remember that your ``foo`` package needs to be installed for this system to
work.
