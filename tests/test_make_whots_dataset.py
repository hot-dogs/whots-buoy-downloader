#!/usr/bin/env python3
import os
from subprocess import getstatusoutput, call
from data.make_whots_dataset import WhotsFileDownloader

PRG = '../data/make_whots_dataset.py'


def test_exist():
    """exist"""
    assert os.path.isfile(PRG)


def test_usage():
    """usage"""

    for flag in ['-w', '-whots_number']:
        status, output = getstatusoutput(f'{PRG} {flag}')
        assert status == 0
        assert output.lower().startswith('usage')


def test_input():
    """test for input"""
    option_1 = '-w'
    option_2 = '-s'

    status, output = getstatusoutput(f"{PRG} {option_1} {'17'} {option_2} {'1'}")
    assert output.endswith('WHOTS-XVII_MET_sys1.txt')
    call('rm -rf ../../data/raw/WHOTS-XVII_MET_sys1.txt', shell=True)


def test_whots_system_number():
    whots_17_1 = WhotsFileDownloader(17, 1)
    assert repr(whots_17_1) == "WhotsFileDownloader(17,1)"


def test_get_url():
    whots_16_2 = WhotsFileDownloader(16, 2)
    assert whots_16_2.get_url() == 'https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVI_MET_sys2.txt'
