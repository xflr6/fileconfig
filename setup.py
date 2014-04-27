# setup.py

from setuptools import setup

setup(
    name='fileconfig',
    version='0.4.1',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Config file sections as objects',
    keywords='configuration ini file inheritance aliasing',
    license='MIT',
    url='http://github.com/xflr6/fileconfig',
    packages=['fileconfig'],
    platforms='any',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
