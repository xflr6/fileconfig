"""Bases to be subclassed by client code."""

from . import meta

__all__ = ['Config', 'Stacked']


class Config(metaclass=meta.ConfigMeta):
    """Return section by name from filename as instance."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        items = sorted(self.__dict__.items())
        items = ',\n'.join(f'  {k!r}: {v!r}' for k, v in items)
        return '{\n%s\n}' % items

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return (f'<{self.__module__}.{self.__class__.__name__} object'
                    f' at {id(self):#x}>')
        return f'{self.__module__}.{self.__class__.__name__}({self.key!r})'

    @property
    def names(self):
        """Names, by which the instance can be retrieved."""
        if getattr(self, 'key', None) is None:
            result = []
        else:
            result = [self.key]
        if hasattr(self, 'aliases'):
            result.extend(self.aliases)
        return result


class Stacked(Config, metaclass=meta.StackedMeta):
    """Return section by name from first matching file as instance."""

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return (f'<{self.__module__}.{self.__class__.__name__}'
                    f'[{self.__class__.filename!r}] object at {id(self):#x}>')
        return (f'{self.__module__}.{self.__class__.__name__}'
                f'[{self.__class__.filename!r}]({self.key!r})')
