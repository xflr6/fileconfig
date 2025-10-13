import pathlib
import re

import pytest

from fileconfig import bases


def test_init_uf8(M00se):  # noqa: N803
    assert M00se('M\xf8\xf8se').key == 'M\xf8\xf8se'


def test_notfound():
    with pytest.raises(IOError):
        class NoCfg(bases.Config):
            filename = 'nonfilename'


def test_iter(Settings):  # noqa: N803
    assert [(pathlib.Path(s.filename).name, s.key) for s in Settings] == \
           [('lumberjack.ini', 'Bevis'), ('lumberjack.ini', 'parrot'),
            ('pet-shop.ini', 'slug'), ('pet-shop.ini', 'Polly')]


def test_getitem(Settings):  # noqa: N803
    assert Settings[Settings.filename] is Settings


def test_call(Settings):  # noqa: N803
    assert Settings(Settings('Bevis')) is Settings('Bevis')
    with pytest.raises(KeyError):
        Settings('nonkey')


def test_repr(Settings):  # noqa: N803
    assert repr(Settings.__base__) == "<class 'fileconfig.bases.Stacked'>"
    assert re.match(r"<class conftest\.Settings\["
                    r"'[^]]+?(\\\\|/)docs(\\\\|/)pet-shop\.ini'\]>",
                    repr(Settings))
