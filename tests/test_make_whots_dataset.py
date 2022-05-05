from subprocess import getstatusoutput, call

# def test_usage():
#     """usage"""
#
#     for flag in ['-w', '-whots_number']:
#         status, output = getstatusoutput(f'{PRG} {flag}')
#         assert status == 0
#         assert output.lower().startswith('usage')
#
#
# def test_input():
#     """test for input"""
#     option_1 = '-w'
#     option_2 = '-s'
#
#     status, output = getstatusoutput(f"{PRG} {option_1} {'17'} {option_2} {'1'}")
#     assert output.endswith('WHOTS-XVII_MET_sys1.txt')
#     call('rm -rf ../../data/raw/WHOTS-XVII_MET_sys1.txt', shell=True)
#
#
# def test_whots_system_number():
#     whots_17_1 = WhotsFileDownloader(17, 1)
#     assert repr(whots_17_1) == "WhotsFileDownloader(17,1)"
#
#
# def test_get_url():
#     whots_16_2 = WhotsFileDownloader(16, 2)
from data.make_whots_dataset import WhotsFileDownloader

WHOTS_17_1 = WhotsFileDownloader(17, 1)


def test_construction():
    """Test the class construction"""
    assert WHOTS_17_1


def test_get_url():
    """Test get_url function"""
    assert WHOTS_17_1.get_url() == 'https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys1.txt'


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
