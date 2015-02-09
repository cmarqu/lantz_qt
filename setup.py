#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    print('Please install or upgrade setuptools or pip to continue')
    sys.exit(1)


import os
import sys
import codecs


def read(filename):
    return codecs.open(filename, encoding='utf-8').read()


long_description = '\n\n'.join([read('README'),
                                read('AUTHORS'),
                                read('CHANGES')])

__doc__ = long_description

requirements = []

if sys.version_info < (3, 4):
    requirements.append('enum34')

root_folder = os.path.dirname(os.path.abspath(__file__))

setup(name='Lantz-qt',
      version='0.4.dev0',
      license='BSD',
      description='Instrumentation framework',
      long_description=long_description,
      keywords='measurement control instrumentation science',
      author='Hernan E. Grecco',
      author_email='hernan.grecco@gmail.com',
      url='http://lantz.glugcen.dc.uba.ar/',
      packages=['lantz_qt',
                'lantz_qt.ui',
                'lantz_qt.ui.blocks',
                'lantz_qt.utils'],
      install_requires=['lantz_core>=0.4'],
      zip_safe=False,
      platforms='any',
      entry_points={
           'zest.releaser.releaser.after_checkout': [
              'pyroma = lantz:run_pyroma',
           ],
        },
      classifiers=[
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'Intended Audience :: Science/Research',
           'License :: OSI Approved :: BSD License',
           'Operating System :: MacOS :: MacOS X',
           'Operating System :: Microsoft :: Windows',
           'Operating System :: POSIX',
           'Programming Language :: Python',
           'Programming Language :: Python :: 3.2',
           'Programming Language :: Python :: 3.3',
           'Programming Language :: Python :: 3.4',
           'Topic :: Scientific/Engineering',
           'Topic :: Software Development :: Libraries'
      ],
      scripts=['scripts/lantz-monitor',
               ],
)
