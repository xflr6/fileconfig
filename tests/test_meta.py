# test_bases.py

import unittest

import os

from fileconfig.bases import Config, Stacked


class TestConfigMeta(unittest.TestCase):

    def test_init_uf8(self):
        class M00se(Config):
            filename = '../docs/holy-grail.ini'
            _encoding = 'utf-8-sig'
        self.assertEqual(M00se(u'M\xf8\xf8se').key, u'M\xf8\xf8se')


class TestStackedMeta(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class Settings(Stacked):
            filename = '../docs/pet-shop.ini'
        Settings.add('../docs/lumberjack.ini')
        cls.Settings = Settings

    @classmethod
    def tearDownClass(cls):
        del cls.Settings

    def test_iter(self):
        self.assertEqual([(os.path.basename(s.filename), s.key) for s in self.Settings],
             [('lumberjack.ini', 'Bevis'), ('lumberjack.ini', 'parrot'),
              ('pet-shop.ini', 'slug'), ('pet-shop.ini', 'Polly')])

    def test_repr(self):
        self.assertEqual(repr(self.Settings.__base__),
            "<class 'fileconfig.bases.Stacked'>")
        self.assertRegexpMatches(repr(self.Settings),
            r"<class test_meta\.Settings\['[^]]+?\\\\docs\\\\pet-shop\.ini'\]>")
