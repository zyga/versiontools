.. _usage:

Usage
*****

Adding support for your project
===============================

Put this in your package ``__init__.py``::

    __version__ = (1, 2, 3, 'final', 0)" # replace with your project version
    try:
        import versiontools
        __version__ = versiontools.Version.from_tuple(__version__)
    except ImportError:
        pass


Edit your ``setup.py`` to have code that looks like this::

    import your_package
    import versiontools

    setup(
        version = versiontools.format_version(your_package.__version__),
        install_requires = [
            'versiontools >= 1.1',
        ],
        setup_requires = [
            'versiontools >= 1.1',
        ],
    )


This code will ensure that:

1. Your package will use version tools
2. Your package will correctly install (via pip)


Developing with versiontools
============================

While you are working on the next version of your project you should
make sure that ``releaselevel`` is set to ``"dev"``. This will (if you
have proper vcs integration in place) allow you to get the most benefit.


Releases
========

Each time you make a release (with setup.py sdist or any bdist commands) make
sure to change the ``releaselevel`` to something other than ``"dev"``. You can
use the following strings:

* ``"alpha"``
* ``"beta"``
* ``"candidate"``
* ``"final"``

