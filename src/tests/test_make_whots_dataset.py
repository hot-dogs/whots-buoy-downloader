import os
from subprocess import getstatusoutput, getoutput

prg = '../data/make_whots_dataset.py'


def test_exist():
    """exist"""
    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ['-w', '-whots_number']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


def test_input():
    """test for input"""

    option_1 = '-w'
    option_2 = '-s'

    rv, out = getstatusoutput(f"{prg} {option_1} {'17'} {option_2} {'1'}")
    assert out.endswith('WHOTS-XVII_MET_sys1.txt')
