import pytest

from fileconfig import bases


@pytest.fixture(scope='session')
def Cfg():  # noqa: N802
    class Cfg(bases.Config):
        filename = '../docs/pet-shop.ini'
    return Cfg


@pytest.fixture(scope='session')
def Settings():  # noqa: N802
    class Settings(bases.Stacked):
        filename = '../docs/pet-shop.ini'
    Settings.add('../docs/lumberjack.ini')
    return Settings


@pytest.fixture(scope='session')
def M00se():  # noqa: N802
    class M00se(bases.Config):
        filename = '../docs/holy-grail.ini'
        _encoding = 'utf-8-sig'
    return M00se
