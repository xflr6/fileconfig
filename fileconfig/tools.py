# tools.py

import os
import inspect

__all__ = ['class_path', 'caller_path']


def class_path(cls):
    if cls.__module__ == '__main__':
        return os.getcwd()

    filename = inspect.getfile(cls)

    path = os.path.dirname(filename)
    if not path:
        return os.getcwd()
    return path


def caller_path(steps=2):
    caller = inspect.getouterframes(inspect.currentframe())[steps]
    frame, filename, line_number, function_name,lines, index = caller

    path = os.path.dirname(filename)
    if not path:
        return os.getcwd()
    return path
