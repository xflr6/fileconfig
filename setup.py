# setup.py

import pathlib
from setuptools import setup, find_packages

setup(
    name='fileconfig',
    version='0.6.dev0',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Config file sections as objects',
    keywords='configuration ini file inheritance aliasing',
    license='MIT',
    url='https://github.com/xflr6/fileconfig',
    project_urls={
        'Issue Tracker': 'https://github.com/xflr6/fileconfig/issues',
        'CI': 'https://github.com/xflr6/fileconfig/actions',
        'Coverage': 'https://codecov.io/gh/xflr6/fileconfig',
    },
    packages=find_packages(),
    platforms='any',
    python_requires='>=3.6',
    extras_require={
        'dev': ['tox>3', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['pytest>=4', 'pytest-cov'],
    },
    long_description=pathlib.Path('README.rst').read_text(encoding='utf-8'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
