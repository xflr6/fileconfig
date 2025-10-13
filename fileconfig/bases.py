"""Bases to be subclassed by client code."""

from . import meta

__all__ = ['Config', 'Stacked']


class Config(metaclass=meta.ConfigMeta):
    """Return section by name from filename as instance."""

    key: str

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __str__(self) -> str:
        items = sorted(self.__dict__.items())
        items_repr = ',\n'.join(f'  {k!r}: {v!r}' for k, v in items)
        return '{\n%s\n}' % items_repr

    def __repr__(self) -> str:
        if getattr(self, 'key', None) is None:
            return (f'<{self.__module__}.{self.__class__.__name__} object'
                    f' at {id(self):#x}>')
        return f'{self.__module__}.{self.__class__.__name__}({self.key!r})'

    @property
    def names(self) -> list[str]:
        """Names, by which the instance can be retrieved."""
        result = [self.key] if getattr(self, 'key', None) is not None else []
        if hasattr(self, 'aliases'):
            result.extend(self.aliases)
        return result


class Stacked(Config, metaclass=meta.StackedMeta):
    """Return section by name from first matching file as instance."""

    def __repr__(self) -> str:
        if getattr(self, 'key', None) is None:
            return (f'<{self.__module__}.{self.__class__.__name__}'
                    f'[{self.__class__.filename!r}] object at {id(self):#x}>')
        return (f'{self.__module__}.{self.__class__.__name__}'
                f'[{self.__class__.filename!r}]({self.key!r})')
