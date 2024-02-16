import re
import Levenshtein

class DuplicateNameHandler:
    def __init__(self):
        # Initialize the original author name as an empty string
        self.original_author_name = ""
        
        # Compiled regex patterns to save on computation time
        # Pattern to remove middle initial from author name
        self.middle_initial_pattern = re.compile(r'\s+[A-Z]\.\s*')
        # Pattern to remove whitespace from author name
        self.name_compressor_pattern = re.compile(r'\s+')
        
        # Dictionary to hold compressed names and original names
        # Key: compressed name (str), Value: original name (str)
        self.author_names_dict = {}
    
    def get_original_name(self, compressed_name):
        """
        Retrieves the original name for a given compressed name.
        
        Args:
            compressed_name (str): The compressed name to look up.
        
        Returns:
            tuple: (bool, str) A tuple where the first element is True if the original name was found,
                   and False otherwise. The second element is the original name or an error message.
        """
        try:
            return True, self.author_names_dict[compressed_name]
        except KeyError:
            return False, f"Original name for {compressed_name} not found. KeyError"
    
    def save_original_author_name(self, original_author_name):
        """
        Saves the provided author name as the current original author name.
        
        Args:
            original_author_name (str): The full name of the author.
        """
        self.original_author_name = original_author_name

    def remove_middle_intial(self, author_name):
        """
        Removes the middle initial from the authors name if present
        
        Args:
            author_name (str): Full name of author
        
        Returns:
            (str): The author's name with the middle initial removed
        """
        # Use MI Pattern to remove middle intial from any names that have them
        return self.middle_initial_pattern.sub('', author_name)
    
    def name_compressor(self, author_name):
        """
        Compresses the author's name by removing whitespace and converting the name to lowercase
        
        Args:
            author_name (str): The name of the author to be compressed
        Returns:
            str: The compressed author name
        """
        return self.name_compressor_pattern.sub('', author_name).lower()
    
    def name_smusher(self, author_name):
        """
        Processes the author's name by removing the middle initial and compressing the name
        Updates the author names dictionary with the transformed name as the key and original name as the value
        
        Args:
            author_name (str): The name of the author to be processed
        
        Returns:
            str: 
        """
        self.save_original_author_name(author_name)
        compressed_name = self.remove_middle_intial(author_name)
        compressed_name = self.name_compressor(compressed_name)
        
        # Add/ Update dictionary: author_names_dict with compressed name as key and original name as value
        self.author_names_dict[compressed_name] = self.original_author_name
        return compressed_name
    
class DuplicateNameHandlerEdgeCases(DuplicateNameHandler):
    def __init__(self):
        # Initialize base class
        super().__init__()
    
    def extract_faculty_sets(self, category_dict):
        #TODO: Implement
        """
        Extracts the faculty_set value from each key in category_dict and stores those lists in a set
        
        Args:
            category_dict (dictionary): A dictionary where the keys are the category names and the values contain a faculty_set. 
        Returns:
            list_of_faculty_sets (list): A list containing each set from all the keys in category_dict
        """
        list_of_faculty_sets = []
        
        for key in category_dict:
            try:
                list_of_faculty_sets.append(category_dict[key]['faculty_set'])
            except:
                print(f"Error extracting faculty sets from {key}, continuing to next")
        return list_of_faculty_sets
        
        
    
    def filter_names_by_initials(self, author_set):
        """
        Filters each set of faculty names, keeping only those where the first letter of both the first and last name
        match the first letter of the original author name.
        
        Args:
            author_sets (dict): A list of sets of author names.
        
        Returns:
            
        """
        # TODO: implement
        filtered_set = {name for name in author_set if len(name.split()) >= 2 and name.split()[0][0].lower() == name.split()[-1][0].lower()}
        return filtered_set
    
    def remove_near_duplicates(self, category_dict):
        #TODO: Implement
        """
        Controls the flow of the class calling neccesary function to handle the edge case of near duplicates slipping through
        preprocessing.
        """
        # list
        faculty_sets = self.extract_faculty_sets(category_dict)
        
        
    """
    POSSIBLE IMPLEMENTATION
    TODO: CHECK THE LOGIC
    
        def remove_near_duplicates(self, category_dict):
        
        Controls the flow of the class, calling necessary functions to handle the edge case of near duplicates slipping through
        preprocessing.
        
        Args:
            category_dict (dict): A dictionary where the keys are category names and the values are sets of faculty names.
        
        faculty_sets = self.get_sets_from_dict(category_dict)
        for category, author_set in category_dict.items():
            filtered_set = self.filter_names_by_initials(author_set)
            final_set = self.process_for_duplicates(filtered_set, faculty_sets)
            # Update the original category_dict with the processed set
            category_dict[category] = final_set

    def process_for_duplicates(self, author_set, faculty_sets):
        
        Processes a set of author names to remove near duplicates, keeping the most frequently occurring name across all sets.
        
        Args:
            author_set (set): A set of author names to process.
            faculty_sets (list): A list of all sets of author names.
        
        Returns:
            set: A set of author names after removing near duplicates.
        
        all_names = set().union(*faculty_sets)  # Combine all names from all sets
        final_set = set()
        for name in author_set:
            similar_names = {other_name for other_name in all_names if Levenshtein.distance(name, other_name) <= 2}
            most_frequent_name = max(similar_names, key=lambda x: sum(x in s for s in faculty_sets))
            final_set.add(most_frequent_name)
        return final_set
    """