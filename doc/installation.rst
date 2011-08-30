Installation
============

Prerequisites
^^^^^^^^^^^^^

There are no requirements to use core features.

Plugins have addtional dependencies but typically require the appropriate
python library to work. Check your plugin documentation for details.

To build the documentation from source you will need sphinx.

Installation Options
^^^^^^^^^^^^^^^^^^^^

There are several installation options available:


Using Python Package Index
--------------------------

This package is being actively maintained and published in the `Python Package
Index <http://http://pypi.python.org>`_. You can install it if you have `pip
<http://pip.openplans.org/>`_ tool using just one line::

    pip install versiontools


Using source tarball
--------------------

To install from source you must first obtain a source tarball from
`versiontools pypi page <http://pypi.python.org/pypi/versiontools>`_. Unpack
the tarball and run::

    python setup.py install

You can pass ``--user`` if you prefer to do a local (non system-wide)
installation.

..  note:: 

    To install from source you will need setuptools or distribute. They are
    typically installed on any Linux system with python but on Windows you may
    need to install that separately.


Using Ubuntu PPAs
-----------------

For Ubuntu 10.04 onward there is a stable PPA (personal package archive):

* ppa:linaro-validation/ppa

To add a ppa to an Ubuntu system use the add-apt-repository command::

    sudo add-apt-repository ppa:linaro-validation/ppa

After you add the PPA you need to update your package cache::

    sudo apt-get update

Finally you can install the package, it is called `python-versiontools`::

    sudo apt-get install python-versiontools
