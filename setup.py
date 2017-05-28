# setup.py

from setuptools import setup, find_packages

setup(
    name='fileconfig',
    version='0.5.6.dev0',
    author='Sebastian Bank',
    author_email='sebastian.bank@uni-leipzig.de',
    description='Config file sections as objects',
    keywords='configuration ini file inheritance aliasing',
    license='MIT',
    url='https://github.com/xflr6/fileconfig',
    packages=find_packages(),
    platforms='any',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
