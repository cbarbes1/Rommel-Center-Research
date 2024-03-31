import re
import os
import warnings
import time
import json
from AttributeExtractionStrategies import AuthorExtractionStrategy, DefaultExtractionStrategy, WosCategoryExtractionStrategy, DepartmentExtractionStrategy

# TODO: make documentation on the class and it's methods

"""
This script contains a class that has various utility methods that will be used for many purposes throughout the project
"""

class Utilities:
    MAX_FILENAME_LENGTH = 255

    def __init__(self):

        # for WoS categories
        self.wc_pattern = re.compile(r"WC\s+(.+?)(?=\nWE)", re.DOTALL)

        # attribute patterns
        self.attribute_patterns = {
            "author": AuthorExtractionStrategy(),
            "title": DefaultExtractionStrategy(),
            "abstract": DefaultExtractionStrategy(),
            "end_record": DefaultExtractionStrategy(),
            "wc_pattern": WosCategoryExtractionStrategy(),
            "department": DepartmentExtractionStrategy(),
        }

    def get_attributes(self, entry_text, attributes):
        """
        Extracts specified attributes from the article entry and returns them in a dictionary.
        It also warns about missing or invalid attributes.

        Parameters:
            entry_text (str): The text of the article entry.
            attributes (list of str): A list of attribute names to extract from the entry, e.g., ["title", "author"].

        Returns:
            dict: A dictionary where keys are attribute names and values are tuples.
                  Each tuple contains a boolean indicating success or failure of extraction,
                  and the extracted attribute value or None.

        Raises:
            ValueError: If an attribute not defined in `self.attribute_patterns` is requested.
        """
        attribute_results = {}
        for attribute in attributes:
            # Check if the requested attribute is defined in the attribute patterns dictionary
            if attribute in self.attribute_patterns:
                if attribute == "author":
                    attribute_results[attribute] = self.attribute_patterns[attribute].extract_attribute(entry_text)
                
                elif attribute == "department":
                    attribute_results[attribute] = self.attribute_patterns[attribute].extract_attribute(entry_text)

                elif attribute == "wc_pattern":
                    attribute_results[attribute] = self.attribute_patterns[attribute].extract_attribute(entry_text)
                    
                else:
                    # Extract the attribute and add it to results dictionary
                    attribute_results[attribute] = self.attribute_patterns[attribute].extract_attribute(
                        attribute, entry_text
                    )
            else:
                # Raise an error if an unknown attribute is requested
                raise ValueError(f"Unknown attribute: '{attribute}' requested.")
        return attribute_results
    
    def extract_abstract_and_categories_from_file(self):
        dir_path = "./split_files"
        results = {}
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    file_content = file.read()
                attributes = self.get_attributes(
                    file_content, ["abstract", "wc_pattern"]
                )

                abstract = attributes["abstract"][1] if ["abstract"][0] else None
                categories = attributes["wc_pattern"][1] if ["wc_pattern"] else []

                if abstract:
                    results[abstract] = categories
        return results

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
        text = re.sub("<[^>]+>", "", text)

        # Replace invalid filename characters with underscores
        invalid_chars = r'[<>:"/\\|?*\n]+'
        sanitized = re.compile(invalid_chars).sub("_", text)

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
        first_author = author[0].strip()

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
            return os.getcwd()

        # Create the directory if it doesn't exist
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        return path

    def abstract_to_categories_mapping(self, entry_text):
        """
        Extracts the abstract and categories from the entry text and returns a dictionary
        with the abstract as the key and categories as the value.

        Parameters:
            entry_text (str): The text of the article entry.

        Returns:
            dict: A dictionary with the abstract as the key and a list of categories as the value.
        """
        # Extract attributes
        attributes = self.get_attributes(entry_text, ["abstract", "wc_pattern"])

        # Initializes the result dictionary
        result = {}

        # Extract the abstract and categories from the attributes dictionary
        abstract = attributes["abstract"][1] if attributes["abstract"][0] else None
        categories = attributes["wc_pattern"][1] if attributes["wc_pattern"][0] else []

        # Check if abstract and categories were successfully extracted
        if abstract and categories:
            # map the abstract to the categories in the result dictionary
            result[abstract] = categories

        return result

    def splitter(self, path_to_file):
        """
        Splits a document into individual entries based on a specified delimiter.

        Parameters:
            path_to_file (str): The path to the the document to be split

        Returns:
            list: A list of strings, each representing an individual entry from the document.
        """
        # Read entire document into memory
        with open(path_to_file, "r", encoding="utf-8") as file:
            file_content = file.read()

        # Split the document into entries based on the end record delimiter
        splits = self.end_record_pattern.split(file_content)

        # filter out any empty strings that may result from splitting
        # re-add delimiter for completeness if needed
        splits = [split + "DA 2024-02-08\nER" for split in splits if split.strip()]
        return splits

    def get_wos_categories(self, path_to_entry):
        """
        Parameters:
            path_to_entry (str): The path to a file
        returns:
            list of the categories.
            list is constructed so that from left to right is most inclusive to least inclusive
            this means index 0 is the root category, index 1 first level subcategory, and so on

        Function looks through a file to find the web of science categories, storing them in
        the categories list. Format of storing is left->right most inclusive->least inclusive
        """
        categories = []
        full_path = "/mnt/linuxlab/home/spresley1/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities/split_files/Author:Osman, Suzanne L._Title:Sexual victimization experience, acknowledgment labeling and rape_   empathy among college men and w.txt"
        with open(full_path, "r") as file:
            file_content = file.read()
        wc_match = re.search(self.wc_pattern, file_content)
        if wc_match:
            # split matched string by ';' and strip whitespace from each category
            categories = [category.strip() for category in wc_match.group(1).split(";")]
        return categories

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
            attributes = self.get_attributes(split, ["author", "title"])
            author = attributes["author"][1] if attributes["author"][0] else "Unknown"
            title = attributes["title"][1] if attributes["title"][0] else "Unkown"

            # Construct file name
            file_name = self.get_file_name(author, title)

            # Ensure output directory exists
            save_in_dir = self.get_output_dir(output_dir)

            # Construct full path for new file
            path = os.path.join(save_in_dir, file_name)

            # Check if file already exists to avoid duplicates/overwriting
            if not os.path.exists(path):
                # Write the entry's contents to the new file
                with open(path, "w") as new_file:
                    new_file.write(split)

                # Track the created file
                file_paths[index] = path
            else:
                print(f"File {path} already exists. Skipping.")

        return file_paths


if __name__ == "__main__":
    utils = Utilities()
    results = utils.extract_abstract_and_categories_from_file()
    with open("abstracts_to_categories.json", "w") as json_file:
        json.dump(results, json_file, indent=4)
