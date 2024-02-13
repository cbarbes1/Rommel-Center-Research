from utilities import Utilities
import os
import json
import warnings

#random comment so i can repush

class WosClassification():
    # Goes through all split_files finds their web of science categories
    # Adds categories to a category dictionary, key: category value: various counts (faculty, articles, department, etc)
    # updates faculty count, dept count, and article count each time it sees a new faculty, article, or dept for that category
    
    def __init__(self):
        self.utils = Utilities()
        self.category_counts = {}
    
    def get_category_counts(self):
        return self.category_counts
    
    def construct_categories(self, directory_path):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            # ensure it's a file
            if self.check_file_status(file_path):
                with open(file_path, 'r') as current_file:
                    self.category_finder(current_file, file_path)
            else:
                warnings.warn(f"Warning: Could not verify file at: {file_path} as a file. Continuing to next file.")
                continue
            
    def check_file_status(self, file_path)->bool:
        if os.path.isfile(file_path):
            return True
        return False

    def category_finder(self, current_file, file_path):
        for line in current_file:
            if line.startswith('WC'):
                categories = self.utils.wos_category_splitter(line)
                self.initialize_categories(categories)
                self.update_category_counts_files_set(categories, file_path)
        
    def initialize_categories(self, categories):
        for category in categories:
            if category not in self.category_counts:
                self.category_counts[category] = {
                    'faculty_count': 0,
                    'department_count': 0,
                    'article_count': 0,
                    'files': set(),
                }
    
    def update_category_counts_files_set(self, categories, file_name):
        for category in categories:
            if category in self.category_counts:
                self.category_counts[category]['files'].add(file_name)
            else:
                warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next category.")
                continue
            
if __name__ == "__main__":
    split_files_directory_path = "~/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities/split_files"
    split_files_directory_path = os.path.expanduser(split_files_directory_path)
    
    wos = WosClassification()
    wos.construct_categories(directory_path=split_files_directory_path)
    
    categories = wos.get_category_counts()
    print(categories)

    
