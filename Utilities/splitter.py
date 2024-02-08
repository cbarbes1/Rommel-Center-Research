from utilities import utilities
import re
import os

"""
This script is used to split the text file containing all metadata for papers associated with salisbury university
over the past 5 years. It splits by entry.
"""

class splitter():
    def __init__(self, file):
        self.file = file
        self.utilities = utilities()
    def split(self):
        """
        Arguments:
            self
        Splits documents up into individual entries, calls make_file from utilities on each entry to make a .txt file for each
        """
