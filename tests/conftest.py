import pytest

from data import DefineWhotsSystem


@pytest.fixture
def w17_1() -> DefineWhotsSystem:
    return DefineWhotsSystem(17, 1)
