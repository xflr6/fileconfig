# conftest.py

import pytest

from fileconfig.bases import Config, Stacked


@pytest.fixture(scope='session')
def Cfg():
    class Cfg(Config):
        filename = '../docs/pet-shop.ini'
    return Cfg


@pytest.fixture(scope='session')
def Settings():
    class Settings(Stacked):
        filename = '../docs/pet-shop.ini'
    Settings.add('../docs/lumberjack.ini')
    return Settings


@pytest.fixture(scope='session')
def M00se():
    class M00se(Config):
        filename = '../docs/holy-grail.ini'
        _encoding = 'utf-8-sig'
    return M00se
