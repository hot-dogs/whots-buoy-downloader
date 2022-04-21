#!/usr/bin/env python3
import argparse
from abc import ABC
from urllib.request import urlopen


class WhotsFileDownloader:
    """WHOTS File Downloader class.

    WHOTS file downloader are the ones responsible for downloading the WHOTS text files and writing it to disk.
    """

    def __init__(self, whots_number, system_number):
        self.whots_number = whots_number
        self.system_number = system_number
        # self.read_file = None

    def parse_args():
        """
          Parse input arguments
        """
        parser = argparse.ArgumentParser(description=' Download WHOTS files')

        parser.add_argument(
            "-w",
            type=int,
            nargs=1,
            dest="whots_number",
            help="Type the WHOTS buoy number (eg. `17` for WHOTS-17)",
            action="store"
        )

        parser.add_argument(
            "-s",
            type=int,
            nargs=1,
            dest="system_number",
            help="WHOTS system number: ( 1 or 2 )",
            action="store"
        )

        args = parser.parse_args()
        return args

    def get_whots_system(self):
        if self.system_number == 1:
            self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys1.txt"

        elif self.system_number == 2:
            self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-XVII_MET_sys2.txt"

        return self.content

    def read_whots_sys(self):
        with urlopen(self.content) as download:
            self.read_file = download.read().decode()
        return self.read_file

    def save_whots_sys(self):
        with open("sys" + str(self.system_number) + ".txt", 'w') as output:
            output.write(self.read_file)
        return


if __name__ == "__main__":
    args = WhotsFileDownloader.parse_args()
    download = WhotsFileDownloader(args.whots_number[0], args.system_number[0])
    print(download.get_whots_system())
    download.read_whots_sys()
    download.save_whots_sys()