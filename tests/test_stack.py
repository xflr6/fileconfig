# test_stack.py

import os


def test_getitem(Settings):  # noqa: N803
    top = Settings.stack[0]
    assert os.path.basename(top.filename) == 'lumberjack.ini'
    assert Settings.stack[top.filename] is top


def test_repr(Settings):  # noqa: N803
    assert repr(Settings.stack).startswith('<ConfigStack [')
