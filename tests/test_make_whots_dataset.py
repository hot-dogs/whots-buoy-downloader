from subprocess import getstatusoutput, call
import pytest
from data import DefineWhotsSystem


def test_construction_17(w17_1):
    """Test the class construction"""
    assert w17_1.whots_number == 17
    assert w17_1.system_number == 1


def test_bad_constructor():
    with pytest.raises(ValueError):
        DefineWhotsSystem(16, 4)


def test_construction_50():
    w50_1 = DefineWhotsSystem(50, 1)
    assert w50_1.whots_number == 50
    assert w50_1.system_number == 1


def test_whots_number():
    w = DefineWhotsSystem
    w.whots_number = 16
    assert w.whots_number == 16


def test_system_number():
    w = DefineWhotsSystem
    w.system_number = 1
    assert w.system_number == 1


def test_get_url(w17_1):
    """Test get_url function"""
    assert w17_1.url() == 'https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys1.txt'

# def test_test_url():
#     assert WHOTS_17_1.test_url() ==
#
#
# def test_read_raw_file():
#     assert False
#
#
# def test_save_raw_data():
#     assert False
#
#
# def test_display_system_file():
#     assert False

# @pytest.mark.skip(reason='Need to fix/implement the bash usage')
# def test_usage():
#     """usage"""
#
#     for flag in ['-w', '-whots_number']:
#         status, output = getstatusoutput(f'{PRG} {flag}')
#         assert status == 0
#         assert output.lower().startswith('usage')
#
#
# @pytest.mark.skip(reason='Need to fix/implement bash input')
# def test_input():
#     """test for input"""
#     option_1 = '-w'
#     option_2 = '-s'
#
#     status, output = getstatusoutput(f"{PRG} {option_1} {'17'} {option_2} {'1'}")
#     assert output.endswith('WHOTS-XVII_MET_sys1.txt')
#     call('rm -rf ../../data/raw/WHOTS-XVII_MET_sys1.txt', shell=True)
