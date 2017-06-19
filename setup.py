import os
import re

from setuptools import setup, find_packages

v = open(os.path.join(os.path.dirname(__file__), 'edwin_core', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='edwin_core',
      version=VERSION,
      description="Data Science Helper for Jupyter Notebooks",
      long_description=open(readme).read(),
      classifiers=[
      'Development Status :: 1 - Alpha',
      'Environment :: IPython Shell, IPython Notebooks',
      'Intended Audience :: Data Scientists, Data Architects',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      ],
      install_requires=[
        "requests",
        "numpy",
        "pandas",
        "IPython",
        "mpld3",
        "matplotlib"
      ],
      keywords='Jupyter Notebooks Jupyterhub',
      author='John Omernik',
      author_email='john@omernik.com',
      license='Apache',
      packages=find_packages(),
      include_package_data=True,
      tests_require=[],
      test_suite="",
      zip_safe=False
)
