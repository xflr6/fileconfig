# stacks.py

import os

import meta
import bases

import tools

class StackMeta(meta.ConfigMeta):

    def __init__(self, name, bases, dct):
        if hasattr(self, '_stack'):
            super(StackMeta, self).__init__(name, bases, dct)
        else:
            self._map = {}
            self._configs = []
            filename = dct.pop('filename', None)
            if filename is not None:
                if not os.path.isabs(filename):
                    filename = os.path.join(tools.caller_path(), filename)
                self.add(filename)

    def add(self, filename, position=0):
        if not os.path.isabs(filename):
            filename = os.path.join(tools.caller_path(), filename)

        cls = type(self.__name__, (self,),
            {'_stack': self, '__module__': self.__module__, 'filename': filename})
        self._map[filename] = cls
        self._configs.insert(position, cls)

    def __call__(self, key=meta.SECTION):
        if hasattr(self, '_stack'):
            return super(StackMeta, self).__call__(key)

        for c in self._configs:
            try:
                return c(key)
            except KeyError:
                pass
        else:
            raise KeyError(key)

    def __iter__(self):
        if hasattr(self, '_stack'):
            return super(StackMeta, self).__iter__()
        seen = set()
        return (s for c in self._configs for s in c
            if s.key not in seen and not seen.add(s.key))

    def __getitem__(self, filename):
        if hasattr(self, '_stack'):
            raise RuntimeError()
        return self._map[filename]

    def __repr__(self):
        if hasattr(self, '_stack'):
            return '<class %s.%s[%r]>' % (self.__module__, self.__name__, self.filename)
        return super(StackMeta, self).__repr__()


class Stack(bases.Config):

    __metaclass__ = StackMeta

    def __repr__(self):
        if getattr(self, 'key', None) is None:
            return '<%s.%s[%r] object at %#x>' % (self.__module__,
                self.__class__.__name__, self.__class__.filename, id(self))
        return '%s.%s[%r](%r)' % (self.__module__, self.__class__.__name__,
            self.__class__.filename, self.key)
