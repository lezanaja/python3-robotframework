#!/usr/bin/env python

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

version_file = join(dirname(__file__), 'src', 'AwareLibrary', 'version.py')
exec(compile(open(version_file).read(), version_file, 'exec'))


setup(name         = 'AwareLibrary',
      version      = VERSION,
      description  = 'Aware Library',
      # long_description = open(join(dirname(__file__), 'README.rst')).read(),
      author       = 'Aware Technology Solution (ATS)',
      author_email = 'info@aware.co.th',
      url          = 'https://www.aware.co.th',
      license      = 'Aware Technology Solution (ATS)',
      keywords     = '',
      platforms    = 'any',
      zip_safe     = False,
      package_dir  = {'' : 'src'},
      packages     = find_packages('src'),
      include_package_data = True,
      install_requires=[
      ]
)
