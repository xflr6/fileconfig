# fileconfig - create class instances from config file section

"""Parse config file and return class instances for each section."""

__title__ = 'fileconfig'
__version__ = '0.2'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'MIT, see LICENSE'
__copyright__ = 'Copyright (c) 2014 Sebastian Bank'

from bases import Config
from stack import Stack

__all__ = ['Config', 'Stack']
