# test_bases.py

import re

import os


def test_init_uf8(M00se):
    assert M00se(u'M\xf8\xf8se').key == u'M\xf8\xf8se'


def test_iter(Settings):
    assert [(os.path.basename(s.filename), s.key) for s in Settings] == \
         [('lumberjack.ini', 'Bevis'), ('lumberjack.ini', 'parrot'),
          ('pet-shop.ini', 'slug'), ('pet-shop.ini', 'Polly')]


def test_repr(Settings):
    assert repr(Settings.__base__) == "<class 'fileconfig.bases.Stacked'>"
    assert re.match(r"<class conftest\.Settings\['[^]]+?(\\\\|/)docs(\\\\|/)pet-shop\.ini'\]>",
                    repr(Settings))
