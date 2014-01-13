# fileconfig - create class instances from config file section

"""Parse config file and return class instances for each section."""

__title__ = 'fileconfig'
__version__ = '0.1'
__author__ = 'Sebastian Bank <sebastian.bank@uni-leipzig.de>'
__license__ = 'MIT,see LICENSE'
__copyright__ = 'Copyright (c) 2014 Sebastian Bank'

import meta

__all__ = ['Config']


class Config(object):

    __metaclass__ = meta.ConfigMeta

    filename = None

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return '<%s.%s object at %#x>' % (self.__module__, self.__class__.__name__, id(self))
        return '%s.%s(%r)' % (self.__module__, self.__class__.__name__, self.key)

    @property
    def names(self):
        return [self.key] + self.aliases
