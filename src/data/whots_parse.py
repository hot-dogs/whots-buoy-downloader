#!/usr/bin/env python3
import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""WHOTS FILE DOWNLOADER 
        Example: If you want to download the raw system 1 from WHOTS 17, type:

        python3 make_whots_dataset.py -w 17 -s 1""",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-w",
                        type=int,
                        nargs=1,
                        dest="whots_number",
                        help="Type the WHOTS buoy NUMBER (eg. `17` for WHOTS-17)",
                        action="store")

    parser.add_argument("-s",
                        type=int,
                        nargs=1,
                        dest="system_number",
                        help="WHOTS SYSTEM NUMBER: ( 1 or 2 )",
                        action="store")

    if len(sys.argv) <= 4:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


def main():
    """Start program to get attributes"""
    args = get_args()
    whots_number = args.whots_number
    system_number = args.system_number

    print('whots_number = "{}"'.format(whots_number))
    print('system_number= "{}"'.format(system_number))


if __name__ == "__main__":
    main()
