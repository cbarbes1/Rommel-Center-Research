from utilities import Utilities
import warnings
from My_Data_Classes import CategoryInfo

class CategoryProcessor:
    def __init__(self, utils, faculty_department_manager):
        self.utils = utils
        self.faculty_department_manager = faculty_department_manager
        self.category_counts = {}
        
    def category_finder(self, current_file, file_path):
        file_content = current_file.read()
        lines = file_content.splitlines()
        for line in lines:
            if line.startswith('WC'):
                attributes_to_retrieve = ['author', 'department', 'wc_pattern']
                attribute_results = self.utils.get_attributes(entry_text=file_content, attributes=attributes_to_retrieve)
                categories = attribute_results['wc_pattern'][1]
                self.initialize_categories(categories=categories)
                self.update_category_counts_files_set(categories=categories, file_name=file_path)
                faculty_members = attribute_results['author'][1] if attribute_results['author'][0] else 'Unknown'
                department_members = attribute_results['department'][1] if attribute_results['department'][0] else 'Unknown'
                self.faculty_department_manager.update_faculty_set(categories, faculty_members)
                self.faculty_department_manager.update_department_set_2(categories, department_members)
    
    def initialize_categories(self, categories):
        for i, category in enumerate(categories):
            # if category starts with 'WC ', remove it
            if category.startswith('WC '):
                categories[i] = category[3:]
                category = categories[i]
                
            if category not in self.category_counts:
                # Intialize a new CategoryInfo dataclass instance for the given category
                self.category_counts[category] = CategoryInfo()
                
    def update_category_counts_files_set(self, categories, file_name):                      
        for category in categories:
            if category in self.category_counts:
                self.category_counts[category].files.add(file_name)
            else:
                warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next category.")