import re
import os

"""
This script contains a class that has various utility methods that will be used for many purposes throughout the project
"""

class utilities():
    def __init__(self):
        pass
    def get_author(self, file):
        """
        Arguments:
            Article entry
        Returns:
            Author of the article
        """
    def get_title(self, file):
        """
        Arguments:
            Article entry
        Returns:
            Title of the article
        """
    def get_abstract(self, file):
        """
        Arguments:
            Article entry
        Returns:
            Abstract of the article
        """
    def get_file_name(self, entry):
        """
        Arguments:
            Article entry
        Returns:
            What to name file
        """
        title = self.get_title(entry)
        author = self.get_author(entry)
        return f"Author:{author}_Title:{title}.txt"
    def get_output_dir(self, type=None):
        if type == "None":
            # return current working directory
            return os.getcwd()
    def make_file(self, file, output_dir):
        """
        Arguments:
            file: full text file with all metadata for all entries
            output_dir: path to directory for which file should be saved in
        Returns:
            A dictionary who's key is the number of the entry (1-654), value is the path to that file
        Calls split to split the file up into chunks and makes each chunk it's own file and puts them into a dictionary as an entry
        """
        splitter = splitter(file)
    