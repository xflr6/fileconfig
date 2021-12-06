import pathlib


def test_getitem(Settings):  # noqa: N803
    top = Settings.stack[0]
    assert pathlib.Path(top.filename).name == 'lumberjack.ini'
    assert Settings.stack[top.filename] is top


def test_repr(Settings):  # noqa: N803
    assert repr(Settings.stack).startswith('<ConfigStack [')
