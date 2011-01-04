.. _usage:

Usage
*****

Adding support for your project
===============================

Put this in your package ``__init__.py``::

    __version__ = "1.2.3" # replace with your project version
    try:
        import versiontools
        __version__ = versiontools.Version(*__version__.split("."))
    except ImportError:
        pass


Add this somewhere inside your ``setup.py`` ``setup()`` call::

    setup(
        install_requires = [
            'versiontools >= 1.0.2',
        ],
        setup_requires = [
            'versiontools >= 1.0.2',
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

