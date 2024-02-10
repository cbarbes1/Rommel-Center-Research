#from utilities import utilities
import re
import os

"""
This script is used to split the text file containing all metadata for papers associated with salisbury university
over the past 5 years. It splits by entry.
"""

class splitter():
    def __init__(self, path_to_file):
        """
        Initializes the splitter object with the path to the text file, and creates a utilities object needed for certain uses of the class
        
        Arguments:
            path_to_file (str): The path to the file containing WoS metadata for papers
        """
        self.path_to_file = path_to_file
        #self.utilities = utilities()
        self.file = None
    
    def __enter__(self):
        """
        Special method to open the file in read mode as part of the context management protocol. This method is automatically
        called when the splitter object is entered using the 'with' statement.
        
        Returns:
            file: The opened file object, allowing for operations such as reading.
        """
        # open file as read only
        self.file = open(self.path_to_file, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Special method to close the file as part of the context management protocol. This method is automatically called
        when exiting the 'with' block, ensuring that the file is properly closed.
        
        Arguments:
            exc_type: The exception type if an exception was raised within the 'with' block.
            exc_value: The exception value if an exception was raised.
            traceback: The traceback information if an exception was raised.
        """
        if self.file:
            self.file.close()

    def split(self):
        """
        Splits the document into individual entries based on a specified delimiter or pattern, and then calls the
        'make_file' method from the utilities object on each entry to create a separate .txt file for each paper entry.
        """
        with open(self.path_to_file, 'r') as file:
            content = file.read()
        
        #entries = 
        
