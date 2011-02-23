#!/usr/bin/env python
#
# Copyright (C) 2010 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of versiontools.
#
# versiontools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# versiontools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with versiontools.  If not, see <http://www.gnu.org/licenses/>.

"""
About
=====

Define *single* and *useful* ``__version__`` of a projects.

.. Note: Since version 1.1 we should conform to PEP 386

"""

import os
import operator


class Version(tuple):
    """
    Version class suitable to be used in module's __version__

    Version class is a tuple and has the same logical components as
    :data:`sys.version_info`.

    There is some extra logic when initializing tuple elements. All
    variables except for releaselevel are silently converted to integers
    That is::

        >>> Version("1.2.3.dev".split("."))
        (1, 2, 3, "dev", 0)

    Also the following default values are used:

        :micro: defaults to zero
        :releaselevel: defaults to "final"
        :serial: 0

    There is a constraint on allowed values of releaselevel. Only the
    following values are permitted:

    * 'dev' (default unless specified differently)
    * 'alpha'
    * 'beta'
    * 'candidate'
    * 'final'
    """

    _RELEASELEVEL_TO_TOKEN = {
        "alpha": "a",
        "beta": "b",
        "candidate": "c",
    }

    @classmethod
    def from_tuple(cls, version_tuple):
        """
        Create version from 5-element tuple

        Note: this is identical to the constructor, just spelled in a
        way that is more obvious to use.

        .. versionadded:: 1.1
        """
        return cls(*version_tuple)

    def __new__(cls, major, minor, micro=0, releaselevel="final", serial=0):
        if releaselevel not in ('dev', 'alpha', 'beta', 'candidate', 'final'):
            raise ValueError(
                "releaselevel %r is not permitted" % (releaselevel,))
        def to_int(v):
            v = int(v)
            if v < 0:
                raise ValueError("Version components cannot be negative")
            return v
        major = to_int(major)
        minor = to_int(minor)
        micro = to_int(micro)
        serial = to_int(serial)
        obj = tuple.__new__(cls, (major, minor, micro, releaselevel, serial))
        obj.__dict__ = {'_vcs': cls._query_vcs()}
        return obj

    major = property(operator.itemgetter(0))
    minor = property(operator.itemgetter(1))
    micro = property(operator.itemgetter(2))
    releaselevel = property(operator.itemgetter(3))
    serial = property(operator.itemgetter(4))

    @property
    def vcs(self):
        """
        Return VCS integration object, if any

        .. note::
            This attribute is **not** an element of the version tuple
            and thus does not break sorting.

        .. versionadded:: 1.0.4
        """
        return self._vcs

    @classmethod
    def _find_source_tree(cls):
        """
        Find the absolute pathname of the tree that contained the file
        that called our __init__()
        """
        import inspect
        frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)
        for index0, record in enumerate(outer_frames):
            frame, filename, lineno, func_name, context, context_index = record
            if func_name == "<module>" and "__version__" in context[context_index]:
                caller = frame
                break
        else:
            caller = None
        if caller:
            return os.path.dirname(os.path.abspath((inspect.getsourcefile(caller))))

    @classmethod
    def _query_vcs(cls):
        """
        Query version control system for the value of serial number.
        The actual version control integration is pluggable, anything
        that provides an entrypoint for ``versintools.vcs_integration``
        is considered. The first version control system that finds the
        revision number wins.
        """
        import pkg_resources
        source_tree = cls._find_source_tree()
        if source_tree is None:
            return
        for entrypoint in pkg_resources.iter_entry_points("versiontools.vcs_integration"):
            try:
                integration_cls = entrypoint.load()
                integration = integration_cls.from_source_tree(source_tree)
                if integration:
                    return integration
            except ImportError:
                pass

    def __str__(self):
        """
        Return a string representing the version of this package

        The string is not a direct concatenation of all version
        components. Instead it's a more natural 'human friendly'
        version where components with certain values are left out.
        """
        version = "%s.%s" % (self.major, self.minor)
        if self.micro != 0:
            version += ".%s" % self.micro
        token = self._RELEASELEVEL_TO_TOKEN.get(self.releaselevel)
        if token:
            version += "%s%d" % (token, self.serial)
        if self.releaselevel != "final" and self.vcs is not None:
            version += ".dev%s" % self.vcs.revno
        return version


def format_version(version):
    """
    Pretty formatting for 5-element version tuple.

    .. versionadded:: 1.1
    """
    if isinstance(version, Version):
        return str(version)
    elif isinstance(version, tuple) and len(version) == 5:
        return str(Version.from_tuple(version))
    else:
        raise ValueError("version must be a tuple of five items")


__version__ = Version(1, 1, 0, "final", 0)
