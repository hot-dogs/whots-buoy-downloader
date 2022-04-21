#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
from urllib.request import urlopen


class WhotsFileDownloader:
    """WHOTS File Downloader class.

    WHOTS file downloader are the ones responsible for downloading the WHOTS text files and writing it to disk.
    """

    def __init__(self, whots_number, system_number):
        self.whots_number, self.system_number, self.content, self.read_file = whots_number, system_number, None, None

    def get_whots_system(self):
        # ----------------------------------------------------------------------------------- #
        # TODO - Transform WHOTS cruise number into greg so we can make the url more generic
        # ----------------------------------------------------------------------------------- #
        if self.system_number == 1:
            self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys1.txt"

        elif self.system_number == 2:
            self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys2.txt"

        return self.content

    def download_whots_sys(self):
        with urlopen(self.content) as download:
            self.read_file = download.read().decode()
        return self.read_file

    def save_whots_sys1(self):
        with open("sys" + str(self.system_number) + ".txt", 'w') as output:
            output.write(self.read_file)
        return


test = WhotsFileDownloader(whots_number=17, system_number=2)
print(test.get_whots_system())
test.download_whots_sys()
test.save_whots_sys1()
