# bases.py - to be subclassed by client code

import meta

__all__ = ['Config', 'Stacked']


class Config(object):
    """Return section by name from filename as instance."""

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
        """Names, by which the instance can be retrieved."""
        if getattr(self, 'key', None) is None:
            return self.aliases
        return [self.key] + self.aliases


class Stacked(Config):
    """Return section by name from first matching file as instance."""

    __metaclass__ = meta.StackedMeta

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return '<%s.%s[%r] object at %#x>' % (self.__module__,
                self.__class__.__name__, self.__class__.filename, id(self))
        return '%s.%s[%r](%r)' % (self.__module__, self.__class__.__name__,
            self.__class__.filename, self.key)
