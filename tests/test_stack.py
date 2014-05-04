# test_stack.py

import unittest

import os

from fileconfig.bases import Stacked


class TestStack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        class Settings(Stacked):
            filename = '../docs/pet-shop.ini'
        Settings.add('../docs/lumberjack.ini')
        cls.Settings = Settings

    @classmethod
    def tearDownClass(cls):
        del cls.Settings

    def test_getitem(self):
        top = self.Settings.stack[0]
        self.assertEqual(os.path.basename(top.filename), 'lumberjack.ini')
        self.assertIs(self.Settings.stack[top.filename], top)
