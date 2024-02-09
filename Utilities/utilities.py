import re
import os
import warnings
from Utilities.DEPRECATED_splitter import split

#TODO: Update comments and make documentation on the class and it's methods

"""
This script contains a class that has various utility methods that will be used for many purposes throughout the project
"""

class utilities():
    def __init__(self):
        self.author_regex = r'AF\s(.+?)(?=\nTI)'
        self.title_regex = r'TI\s(.+?)(?=\nSO)'
        self.abstract_regex = r'AB\s(.+?)(?=\nC1)'
        self.end_record_regex = r'DA \d{4}-\d{2}-\d{2}\nER\n?'
        
    # TODO: look at functionality here as it may not be working as intended 
    def get_attributes(self, entry, attribute):
        """
        Extracts specified attributes from the article entry, returns them in a dictionary,
        and warns about missing or invalid attributes.
        
        Arguments:
            entry (str): The text of the article entry.
            attributes (list): A list of strings representing the attributes to extract, e.g., ["title", "author"].
        
        Returns:
            dict: A dictionary with extracted attributes.
        
        Raises:
            ValueError: If an unknown attribute is requested.
        """
        
        attribute_patterns = {
            'author': (self.author_regex, re.DOTALL),
            'title': (self.title_regex, re.DOTALL),
            'abstract': (self.abstract_regex, re.DOTALL),
            'end_record': (self.end_record_regex, re.DOTALL),
        }
        
        attribute_results = {}
        for attribute in attribute_patterns:
            if attribute in attribute_patterns:
                pattern, flags = attribute_patterns[attribute]
                match = re.search(pattern, entry, flags)
                if match:
                    attribute_results[attribute] = (True, match.group(1).strip())
                else:
                    attribute_results[attribute] = (False, None)
                    warnings.warn(f"Attribute: '{attribute}' was not found in the entry", RuntimeWarning)
            else:
                raise ValueError(f"Unknwon attribute: '{attribute}' requested.")
        return attribute_results
      
    def get_file_name(self, author, title):
        """
        Arguments:
            Author: authors name for entry
            Title: title for the entry
            
        Author and title can be obtained by calling the get_attribute() function and passing in author and title as the attribute
        Returns:
            What to name file
        """
        return f"Author:{author}_Title:{title}.txt"
    
    def get_output_dir(self, path=None):
        # if no path is provided path is made to be the current directory
        if path == "None":
            # return current working directory
            return os.getcwd()
        
        # check if provided path exists
        if not os.path.exists(path):
            # if it doesn't exist, create the directory and any intermediate directories
            os.makedirs(path, exist_ok=True)
        return path
    
    def __enter__(self, mode='r'):
        """
        Special method to open the file in read mode as part of the context management protocol. This method is automatically
        called when the splitter object is entered using the 'with' statement.
        
        Arguments:
            mode (str): The mode in which to open the file. Defaults to 'r' for read mode.
        
        Returns:
            file: The opened file object, allowing for operations such as reading.
        """
        # open file as read only
        self.file = open(self.path_to_file, mode)
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

    
    def splitter(self, path_to_file):
        """
        Splits the document into individual entries based on a specified delimiter or pattern, and then calls the
        'make_file' method from the utilities object on each entry to create a separate .txt file for each paper entry.
        """
        with open(path_to_file, 'r', encoding='utf-8') as file:
            file_content = file.read()
        splits = re.split(self.end_record_regex, file_content)
        # filter out empty entries
        splits = [split + 'DA 2024-02-08\nER' for split in splits if split.strip()] # re-add delimiter for completeness if needed 
        return splits
      
    def make_files(self, path_to_file, output_dir):
        """
        Arguments:
            file: full text file with all metadata for all entries
            output_dir: path to directory for which file should be saved in
        Returns:
            A dictionary who's key is the number of the entry (1-654), value is the path to that file
        Calls split to split the file up into chunks and makes each chunk it's own file and puts them into a dictionary as an entry
        """
        splits = self.splitter(path_to_file)
        file_paths = {} # to keep track of created files and their paths
        
        for index, split in enumerate(splits, start=1):
            # Get attributes to form filename
            attributes = self.get_attributes(split, ['author', 'title'])
            author = attributes['author'][1] if attributes['author'][0] else 'Unknown'
            title = attributes['title'][1] if attributes['title'][0] else 'Unkown'
            
            # construct file name
            file_name = self.get_file_name(author, title)
            
            # Ensure output directory exists
            save_in_dir = self.get_output_dir(output_dir)
            
            # Construct full path for new file
            path = os.path.join(save_in_dir, file_name)
            
            # Write entry contents to new file
            with open(path, 'w') as new_file:
                new_file.write(split)
                
            file_paths[index] = path # track created file
            
        return file_paths
            
            
            
    