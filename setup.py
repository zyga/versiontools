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

from setuptools import setup, find_packages


import versiontools


setup(
    name='versiontools',
    version=versiontools.format_version(versiontools.__version__),
    author="Zygmunt Krynicki",
    author_email="zygmunt.krynicki@linaro.org",
    packages=find_packages(),
    test_suite='versiontools.tests',
    description="Smart replacement for plain tuple used in __version__",
    url='https://launchpad.net/versiontools',
    entry_points="""
    [versiontools.vcs_integration]
    bzr=versiontools.bzr_support:BzrIntegration
    git=versiontools.git_support:GitIntegration
    hg=versiontools.hg_support:HgIntegration
    [distutils.setup_keywords]
    version=versiontools:handle_version
    """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General Public"
         " License (LGPL)"),
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development :: Version Control",
    ],
    zip_safe=True)
