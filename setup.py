import pathlib
from setuptools import setup, find_packages

setup(
    name='fileconfig',
    version='0.6.2.dev0',
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
    python_requires='>=3.9',
    extras_require={
        'dev': ['tox>=3', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['pytest>=7', 'pytest-cov'],
    },
    long_description=pathlib.Path('README.rst').read_text(encoding='utf-8'),
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
