#!/usr/bin/env python3
import argparse
import roman
import sys
from urllib.request import urlopen


def parse_args():
    """
      Parse input arguments
    """
    parser = argparse.ArgumentParser(
        description="""WHOTS FILE DOWNLOADER 
        Example: If you want to download the raw system 1 from WHOTS 17, type:
        
        python3 whots_download_parser.py -w 17 -s 1""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "-w",
        type=int,
        nargs=1,
        dest="whots_number",
        help="Type the WHOTS buoy NUMBER (eg. `17` for WHOTS-17)",
        action="store"
    )

    parser.add_argument(
        "-s",
        type=int,
        nargs=1,
        dest="system_number",
        help="WHOTS SYSTEM NUMBER: ( 1 or 2 )",
        action="store"
    )

    if len(sys.argv) <= 4:
        parser.print_help()
        sys.exit()
    else:
        args = parser.parse_args()

    return args


class WhotsFileDownloader:
    """WHOTS File Downloader class.

    WHOTS file downloader is  responsible for downloading the WHOTS text files
    and writing it to disk.
    """

    def __init__(self, whots_number, system_number):
        self.whots_number = whots_number
        self.system_number = system_number
        self.content = None

    def __str__(self):
        self_str = (
            f' WHOTS NUMBER :  {self.whots_number}\n'
            f' SYSTEM NUMBER:  {self.system_number}'
        )
        return self_str

    def __repr__(self):
        return f"{self.__class__.__name__}({self.whots_number},{self.system_number})"

    def get_url(self):
        self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-" + \
                       str(roman.toRoman(self.whots_number)) + \
                       "_MET_sys" + str(self.system_number) + ".txt "

        return self.content

    def display_url(self):
        print(self.content)

    def read_system_file(self):
        with urlopen(self.content) as download:
            return download.read().decode()

    def save_system_file(self):
        with open("WHOTS-" +
                  str(roman.toRoman(self.whots_number)) +
                  "_MET_sys" + str(self.system_number) +
                  ".txt", 'w') as output:

            return output.write(self.read_system_file())

    def display_system_file(self):
        print("Saving ... " + "WHOTS-" +
              str(roman.toRoman(self.whots_number)) +
              "_MET_sys" + str(self.system_number) + ".txt")


def main():
    args = parse_args()
    whots = WhotsFileDownloader(args.whots_number[0], args.system_number[0])
    whots.get_url()
    whots.display_url()
    whots.read_system_file()
    whots.save_system_file()
    whots.display_system_file()


if __name__ == "__main__":
    main()
