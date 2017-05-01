# test_stack.py

import os


def test_getitem(Settings):
    top = Settings.stack[0]
    assert os.path.basename(top.filename) == 'lumberjack.ini'
    assert Settings.stack[top.filename] is top
