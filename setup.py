#!/usr/bin/env python

# Author: Beta Uliansyah
# email: beta.uliansyah@pknstan.ac.id

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='danarakca',
    description=("Provides instant access to many Indonesian governments financial datasets right from "
                 "Python (in dataframe structure)."),
    author='Beta Uliansyah',
    url='https://github.com/BetaUliansyah/danarakca',
    download_url='https://github.com/BetaUliansyah/danarakca',
    license = 'LGPL',
    author_email='beta.uliansyah@pknstan.ac.id',
    version='0.0.1',
    install_requires=['pandas'],
    packages=['danarakca', 'danarakca.utils'],
    package_data={'danarakca': ['*.gz', 'resources.tar.gz']}
)
