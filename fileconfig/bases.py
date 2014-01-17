# bases.py

import meta

__all__ = ['Config']


class Config(object):

    __metaclass__ = meta.ConfigMeta

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return repr(self.__dict__)

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return '<%s.%s object at %#x>' % (self.__module__,
                self.__class__.__name__, id(self))
        return '%s.%s(%r)' % (self.__module__, self.__class__.__name__, self.key)

    @property
    def names(self):
        if getattr(self, 'key', None) is None:
            return self.aliases
        return [self.key] + self.aliases
