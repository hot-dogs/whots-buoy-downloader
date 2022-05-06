import pytest
from data.make_whots_dataset import DefineWhotsSystem


@pytest.fixture
def whots_17_1() -> DefineWhotsSystem:
    return DefineWhotsSystem(17, 1)


@pytest.fixture
def whots_50_1() -> DefineWhotsSystem:
    return DefineWhotsSystem(50, 1)

