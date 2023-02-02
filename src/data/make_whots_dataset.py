import os
import roman
import sys
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from whots_parse import get_args


class DefineWhotsSystem:
    """WHOTS File Downloader class.
    
    WHOTS file downloader is  responsible for downloading the WHOTS text files
    and writing it to disk.

    Parameters
    ----------

    Returns
    -------

    """

    def __init__(self, whots_number, system_number):
        if system_number > 3:
            raise ValueError("System Number can't be greater than 3")

        self.whots_number = whots_number
        self.system_number = system_number
        self.content = None

    def __str__(self):
        self_str = (
            f'  WHOTS NUMBER :  {self.whots_number}'
            f'\nSYSTEM NUMBER:  {self.system_number}'
        )
        return self_str

    def __repr__(self):
        return f"{self.__class__.__name__}({self.whots_number},{self.system_number})"

    @property
    def whots_number(self):
        """ """
        return self._whots_number

    @whots_number.setter
    def whots_number(self, value):
        """

        Parameters
        ----------
        value :
            

        Returns
        -------

        
        """
        self._whots_number = value

    @property
    def system_number(self):
        """ """
        return self._system_number

    @system_number.setter
    def system_number(self, value):
        """

        Parameters
        ----------
        value :
            

        Returns
        -------

        
        """
        if value > 3:
            raise ValueError("System Number can't be greater than 3")
        self._system_number = value

    def url(self):
        """.url is a property that formats and returns the correct
        WHOTS file.

        Parameters
        ----------

        Returns
        -------

        
        """
        self.content = "https://uop.whoi.edu/currentprojects/WHOTS/data/WHOTS-" + \
                       str(roman.toRoman(self.whots_number)) + \
                       "_MET_sys" + str(self.system_number) + ".txt"

        return self.content

    def test_url(self):
        """ """
        print('-' * 70 + '\n Checking ... ' + self.content)
        try:
            urlopen(self.content)
        except HTTPError as e:
            sys.exit(f'WHOTS-{self.whots_number} SYSTEM-{self.system_number} is not available.\n'
                     f"{'-' * 70}\n"
                     f"The Error code was: {e.code}\n"
                     f"{'-' * 70}\n")

        except URLError as e:
            sys.exit(f'WHOTS-{self.whots_number} SYSTEM-{self.system_number} is not available.\n'
                     f"{'-' * 70}\n"
                     f"Failed to reach the serve:"
                     f"Reason: {e.reason}"
                     f"{'-' * 70}\n")

    def read_raw_file(self):
        """ """
        with urlopen(self.content) as download:
            return download.read().decode()

    def save_raw_data(self):
        """ """
        with open(os.path.join('../../data/raw', "WHOTS-" +
                                                 str(roman.toRoman(self.whots_number)) +
                                                 "_MET_sys" + str(self.system_number) +
                                                 ".txt"), 'w') as output:
            return output.write(self.read_raw_file())

    def display_system_file(self):
        """ """
        return print("-" * 70 + "\nSaving ... " + "WHOTS-" +
                     str(roman.toRoman(self.whots_number)) +
                     "_MET_sys" + str(self.system_number) + ".txt")


def main():
    """ """
    args = get_args()
    whots = DefineWhotsSystem(args.whots_number[0], args.system_number[0])
    whots.url()
    whots.test_url()
    whots.read_raw_file()
    whots.save_raw_data()
    whots.display_system_file()


if __name__ == "__main__":
    main()
