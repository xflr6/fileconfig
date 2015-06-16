# setup.py

from setuptools import setup, find_packages

setup(
    name='fileconfig',
    version='0.5.3.dev0',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Config file sections as objects',
    keywords='configuration ini file inheritance aliasing',
    license='MIT',
    url='http://github.com/xflr6/fileconfig',
    packages=find_packages(),
    extras_require={
        'test': ['nose', 'coverage', 'flake8', 'pep8-naming'],
        'dev': ['wheel'],
    },
    platforms='any',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
