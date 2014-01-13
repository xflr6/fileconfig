# meta.py - parse config, collect arguments, create instances

import os
import inspect
import ConfigParser

__all__ = ['ConfigMeta']


class ConfigMeta(type):
    """Parse file, create instance for each section, return by section or alias."""

    _parser = ConfigParser.SafeConfigParser

    @staticmethod
    def _split_aliases(aliases):
        return aliases.replace(',', ' ').split()

    def __init__(self, name, bases, dct):
        if self.filename is None:
            return

        if os.path.isabs(self.filename):
            filename = self.filename
        else:
            current_path = os.path.dirname(inspect.getfile(self.__init__))
            filename = os.path.join(current_path, self.filename)

        parser = self._parser()
        parser.read(filename)

        self._keys = []
        self._kwargs = {}
        self._aliases = {}

        for key in parser.sections():
            kwargs = dict(parser.items(key), key=key)

            if 'aliases' in kwargs:
                aliases =  kwargs.pop('aliases')
                if aliases.strip():
                    aliases = self._split_aliases(aliases)
                    self._aliases.update((a, key) for a in aliases)
                    kwargs['aliases'] = aliases

            if 'inherits' in kwargs:
                kwargs = dict(((k, v)
                    for k, v in parser.items(kwargs['inherits'])
                    if k != 'aliases'), **kwargs)

            self._keys.append(key)
            self._kwargs[key] = kwargs

        self._cache = {}

    def __call__(self, key='default'):
        if isinstance(key, self):
            return key

        key = self._aliases.get(key, key)
        if key in self._cache:
            inst = self._cache[key]
        else:
            kwargs = self._kwargs.pop(key)
            inst = self.create(**kwargs)
        return inst

    def create(self, key=None, **kwargs):
        inst = super(ConfigMeta, self).__call__(key=key, **kwargs)

        if key is not None:
            self._cache[key] = inst 
        return inst

    def __iter__(self):
        for key in self._keys:
            yield self(key)

    def pprint_all(self):
        for c in self:
            print '%s\n' % c
