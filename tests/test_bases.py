# test_bases.py

import re


def test_repr_cfg(Cfg):
    assert re.match(r'<conftest.Cfg object at 0x\w+>', repr(Cfg.create()))
    assert re.match(r"conftest\.Cfg\('parrot'\)", repr(Cfg('parrot')))


def test_names(Cfg):
    assert Cfg.create().names == []
    assert Cfg('parrot').names == ['parrot']
    assert Cfg('slug').names == ['slug', 'snail', 'special_offer']


def test_repr_settings(Settings):
    assert re.match(r"<conftest\.Settings\['[^]]+?(\\\\|/)docs(\\\\|/)pet-shop\.ini'\] object at 0x\w+>",
                    repr(Settings.create()))
    assert re.match(r"conftest\.Settings\['[^]]+?(\\\\|/)docs(\\\\|/)lumberjack.ini'\]\('parrot'\)",
                    repr(Settings('parrot')))
