# test_bases.py

import unittest

from fileconfig.bases import Config, Stacked


class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class Cfg(Config):
            filename = '../docs/pet-shop.ini'
        cls.Cfg = Cfg

    @classmethod
    def tearDownClass(cls):
        del cls.Cfg

    def test_repr(self):
        self.assertRegexpMatches(repr(self.Cfg.create()),
            "<test_bases.Cfg object at 0x\w+>")
        self.assertEqual(repr(self.Cfg('parrot')),
            "test_bases.Cfg('parrot')")

    def test_names(self):
        self.assertEqual(self.Cfg.create().names, [])
        self.assertEqual(self.Cfg('parrot').names, ['parrot'])
        self.assertEqual(self.Cfg('slug').names,
            ['slug', 'snail', 'special_offer'])


class TestStacked(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class Settings(Stacked):
            filename = '../docs/pet-shop.ini'
        Settings.add('../docs/lumberjack.ini')
        cls.Settings = Settings

    @classmethod
    def tearDownClass(cls):
        del cls.Settings

    def test_repr(self):
        self.assertRegexpMatches(repr(self.Settings.create()),
            r"<test_bases\.Settings\['[^]]+?\\\\docs\\\\pet-shop\.ini'\] object at 0x\w+>")
        self.assertRegexpMatches(repr(self.Settings('parrot')),
            r"test_bases\.Settings\['[^]]+?\\\\docs\\\\lumberjack.ini'\]\('parrot'\)")
