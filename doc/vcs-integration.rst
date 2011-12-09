Integration with version control systems
****************************************

About
=====

Version tools supports a form of version control system integration. This code
is *only* triggered for development versions of your project (indicated by
setting ``releaselevel`` to something other than ``"final"``)

.. note::
    Currently to use :abbr:`VCS (Version Control System)` integration you
    *must* use the name __version__ in your variable name and you *must* define
    it at module level.  There is some fuzzy logic that walks the traceback
    looking for ``__version__``.


Integration plug-ins
====================

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


Batteries included
==================

Versiontools comes with a few plug-ins for commonly used version control
systems.  To use them you need to have the corresponding libraries installed.
They are documented below. 

.. note:
    Users of your packages will *not* need those libraries. They are most
    useful for the developer during project life-cycle, especially between
    releases, to identify tarballs easily.

Bazaar
++++++

To work with Bazaar repositories you will need bzrlib. You can install it with
pip or from the ubuntu package.

.. note:: 
    On Windows the typical Bazaar installation bundles both the python
    interpreter and a host of libraries and those libraries are not accessible
    by the typically-installed python interpreter. If you wish to use Bazaar on
    windows we would recommend to install Bazaar directly from pypi.

Git
+++

To work with Git repositories you will need `GitPython
<http://pypi.python.org/pypi/GitPython>`_. Version 0.1.6 is sufficient to run
the code. 

Mercurial
+++++++++

To work with Mercurial repositories you will need `Mercurial
<http://mercurial.selenic.com/>`_. You can install it with pip or from the
ubuntu package. 
