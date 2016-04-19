import os
import sys

from setuptools import setup, find_packages


version = '0.1.0.dev'

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name='travisci-test',
      version=version,
      description="Travis CI Python Test",
      long_description="""\
""",
      classifiers=[],
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Christopher Selvaraj',
      author_email='christopher.selvaraj@washpost.com',
      url='',
      license='',
      packages=find_packages('src', exclude=['ez_setup', 'examples', 'tests']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      setup_requires=[] + pytest_runner,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      tests_require=['pytest'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
