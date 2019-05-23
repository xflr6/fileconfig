# test_bases.py

import re


def test_repr_cfg(Cfg):  # noqa: N803
    assert re.match(r'<conftest.Cfg object at 0x\w+>', repr(Cfg.create()))
    assert re.match(r"conftest\.Cfg\('parrot'\)", repr(Cfg('parrot')))


def test_names(Cfg):  # noqa: N803
    assert Cfg.create().names == []
    assert Cfg('parrot').names == ['parrot']
    assert Cfg('slug').names == ['slug', 'snail', 'special_offer']


def test_repr_settings(Settings):  # noqa: N803
    assert re.match(r"<conftest\.Settings\["
                    r"'[^]]+?(\\\\|/)docs(\\\\|/)pet-shop\.ini'"
                    r"\] object at 0x\w+>",
                    repr(Settings.create()))
    assert re.match(r"conftest\.Settings\["
                    r"'[^]]+?(\\\\|/)docs(\\\\|/)lumberjack.ini'"
                    r"\]\('parrot'\)",
                    repr(Settings('parrot')))
