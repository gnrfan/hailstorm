#!/usr/bin/env python
#
# Copyright 2013 Bit Zeppelin
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import distutils.core
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

kwargs = {}

version = "1.0.0"

distutils.core.setup(
    name="hailstorm",
    version=version,
    packages = ["hailstorm"],
    package_data = {
        "hailstorm": ["README.md"],
    },
    author="Antonio Ognio",
    author_email="antonio@bitzeppelin.com",
    url="http://github.com/bitzeppelin/hailstorm/",
    download_url="https://github.com/bitzeppelin/hailstorm/zipball/master",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description='A Python templating library in the style of Jinja2 and Django templates '
                'featuring the full power of Python in the expressions that can be embedded '
                'in the template files. Hailstorm was extracted from the templating code '
                'that is part of Tornado Web Server framework published by Facebook.',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    **kwargs
)