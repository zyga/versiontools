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
Versiontools help build useful __version__ objects for your projects
"""

import os


class Version(object):
    """
    Version object suitable to be placed in module's __version__

    Behaves like python's sys.version_info.

    Has some extra abilities when used for development (when
    releaselevel is "dev"). It can then integrate with bzrlib and other
    version control systems to get the revision the branch that contains
    the file that used each Version() object.
    """

    def __init__(self, major, minor, micro=0, releaselevel="dev", serial=0):
        assert releaselevel in ('dev', 'alpha', 'beta', 'candidate', 'final')
        self.major = major
        self.minor = minor
        self.micro = micro
        self.releaselevel = releaselevel
        self.serial = serial
        if self.releaselevel == "dev":
            self.serial = self._query_vcs()

    @property
    def as_tuple(self):
        return (self.major, self.minor, self.micro, self.releaselevel, self.serial)

    def _find_source_tree(self):
        """
        Find the absolute pathname of the tree that contained the file
        that called our __init__()
        """
        import inspect
        frame = inspect.currentframe()
        outer_frames = inspect.getouterframes(frame)
        # Go three frames up:
        #   * one for this function
        #   * another for _query_vcs()
        #   * last one for  __init__
        caller = outer_frames[2][0]
        return os.path.dirname(os.path.abspath((inspect.getsourcefile(caller))))

    def _query_vcs(self):
        """
        Query version control system for the value of serial number.
        The actual version control integration is pluggable, anything
        that provides an entrypoint for versintools.vcs_integration" is
        considered. The first version control system that finds the
        revision number wins.
        """
        import pkg_resources
        source_tree = self._find_source_tree()
        for entrypoint in pkg_resources.iter_entry_points("versiontools.vcs_integration"):
            integration_cls = entrypoint.load()
            integration = integration_cls.from_source_tree(source_tree)
            if integration:
                return integration.revno

    def __repr__(self):
        return 'Version(%r, %r, %r, %r, %r)' % (
            self.major, self.minor, self.micro, self.releaselevel,
            self.serial)

    def __str__(self):
        """
        Return a string representing the version of this package
        """
        version = "%s.%s" % (self.major, self.minor)
        if self.micro != 0:
            version += ".%s" % self.micro
        if self.releaselevel != 'final':
            version += ".%s" % self.releaselevel
        if self.releaselevel == 'dev' and self.serial:
            version += '.%s' % self.serial
        return version


__version__ = Version(1, 0, 0, "dev")
