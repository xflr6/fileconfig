# tools.py - runtime path inspection

import os
import inspect

__all__ = ['class_path', 'caller_path']


def class_path(cls):
    """Return the path to the source file of the given class."""
    if cls.__module__ == '__main__':
        return os.getcwd()

    filename = inspect.getfile(cls)

    path = os.path.dirname(filename)
    if not path:
        return os.getcwd()
    return path


def caller_path(steps=1):
    """Return the path to the source file of the current frames' caller."""
    caller = inspect.getouterframes(inspect.currentframe())[steps + 1]
    frame, filename, line_number, function_name,lines, index = caller

    path = os.path.dirname(filename)
    if not path:
        return os.getcwd()
    return path
