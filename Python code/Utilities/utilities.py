import re
import os
import warnings

#TODO: make documentation on the class and it's methods

"""
This script contains a class that has various utility methods that will be used for many purposes throughout the project
"""

class Utilities():
    MAX_FILENAME_LENGTH = 255
    def __init__(self):
        # regular expressions used to extracting the corresponding features from a document
        self.author_pattern = re.compile(r'AF\s(.+?)(?=\nTI)', re.DOTALL)
        self.title_pattern = re.compile(r'TI\s(.+?)(?=\nSO)', re.DOTALL)
        self.abstract_pattern = re.compile(r'AB\s(.+?)(?=\nC1)', re.DOTALL)
        self.end_record_pattern = re.compile(r'DA \d{4}-\d{2}-\d{2}\nER\n?', re.DOTALL)
         
    def get_attributes(self, entry_text, attributes):
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
            'author': self.author_pattern,
            'title': self.title_pattern,
            'abstract': self.abstract_pattern,
            'end_record': self.end_record_pattern,
        }
        
        attribute_results = {}
        for attribute in attributes:
            if attribute in attribute_patterns:
                pattern = attribute_patterns[attribute]
                match = re.search(pattern, entry_text)
                if match:
                    attribute_results[attribute] = (True, match.group(1).strip())
                else:
                    attribute_results[attribute] = (False, None)
                    warnings.warn(f"Attribute: '{attribute}' was not found in the entry", RuntimeWarning)
            else:
                raise ValueError(f"Unknown attribute: '{attribute}' requested.")
        return attribute_results
    
    def sanitize_filename(self, text, max_length=MAX_FILENAME_LENGTH):
        """
        Sanitizes a string for use as part of a file name.
        
        Args:
            text (str): The text to sanitize.
            max_length (int): The maximum allowed length of the sanitized string. If nothing is provided defaults to MAX_FILENAME_LENGTH
        
        Returns:
            str: A sanitized string safe for use in a file name.
        """
        
        # Remove any potential HTML tags
        text = re.sub('<[^>]+>', '', text)
        
        # Replace invalid filename characters with underscores
        invalid_chars = r'[<>:"/\\|?*\n]+'
        sanitized = re.compile(invalid_chars).sub('_', text)
        
        # Truncate to avoid excessively long file names
        return sanitized[:max_length]
    
    def get_file_name(self, author, title):
        """
        Constructs a filename using the first author's name and the title of an entry.
            
        Parameters:
            author (str): The author(s) of the entry.
            title (str): The title of the entry.
            
        Returns:
            str: A sanitized and formatted filename.
        """
        
        # split author string on newline and take the first author only
        first_author = author.split('\n')[0].strip()
        
        # sanitize and truncate the first authors name and title
        sanitized_author = self.sanitize_filename(first_author)
        sanitized_title = self.sanitize_filename(title)

        # construct file name
        file_name = f"Author:{sanitized_author}_Title:{sanitized_title}.txt"
        # return formatted file name
        return file_name[:255]
    
    def get_output_dir(self, path=None):
        """
        Ensures the output directory exists, creating it if necessary.
        
        Parameters:
            path (str, optional): The path to the output directory. Defaults to the current working directory if None.
        
        Returns:
            str: The path to the output directory.
        """
        # Use current working directory if no path is provided
        if path is None:
            # return current working directory
            return os.getcwd()
        
        # Create the directory if it doesn't exist
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        return path
    
    def splitter(self, path_to_file):
        """
        Splits a document into individual entries based on a specified delimiter.
        
        Parameters:
            path_to_file (str): The path to the the document to be split
        
        Returns:
            list: A list of strings, each representing an individual entry from the document.
        """
        # Read entire document into memory
        with open(path_to_file, 'r', encoding='utf-8') as file:
            file_content = file.read()
            
        # Split the document into entries based on the end record delimiter
        #splits = re.split(self.end_record_pattern, file_content)
        splits = self.end_record_pattern.split(file_content)
        
        # filter out any empty strings that may result from splitting
        splits = [split + 'DA 2024-02-08\nER' for split in splits if split.strip()] # re-add delimiter for completeness if needed 
        return splits
      
    def make_files(self, path_to_file, output_dir):
        """
        Splits a document into individual entries and creates a separate file for each entry in the specified output directory.
        
        Parameters:
            path_to_file (str): The path to the full text file containing all metadata for the entries.
            output_dir (str): The path to the directory where the individual entry files should be saved.
        
        Returns:
            file_paths: A dictionary where each key is the number of the entry (starting from 1) and each value is the path to the corresponding file.
        
        This method first splits the document into individual entries using the `splitter` method. 
        It then iterates over each entry, extracts the necessary attributes to form a filename, 
        ensures the output directory exists, and writes each entry's content to a new file in the output directory.
        Then returns the file_paths dictionary to make referencing any specific document later easier
        """
        splits = self.splitter(path_to_file)
        
        # dictionary to keep track of created files and their paths
        file_paths = {}
        
        for index, split in enumerate(splits, start=1):
            # Extract attributes to form filename
            attributes = self.get_attributes(split, ['author', 'title'])
            author = attributes['author'][1] if attributes['author'][0] else 'Unknown'
            title = attributes['title'][1] if attributes['title'][0] else 'Unkown'
            
            # Construct file name
            file_name = self.get_file_name(author, title)
            
            # Ensure output directory exists
            save_in_dir = self.get_output_dir(output_dir)
            
            # Construct full path for new file
            path = os.path.join(save_in_dir, file_name)

            # Check if file already exists to avoid duplicates/overwriting
            if not os.path.exists(path):
            # Write the entry's contents to the new file
                with open(path, 'w') as new_file:
                    new_file.write(split)
            
                # Track the created file
                file_paths[index] = path
            else:
                print(f"File {path} already exists. Skipping.")
            
        return file_paths
