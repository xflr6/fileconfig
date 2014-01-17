# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='fileconfig',
    version='0.2',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Config file sections as objects',
    license='MIT',
    keywords='configuration ini file',
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
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
