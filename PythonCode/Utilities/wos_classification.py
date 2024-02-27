from utilities import Utilities
from My_Data_Classes import CategoryInfo
from file_handler import FileHandler
from category_processor import CategoryProcessor
from faculty_department_manager import FacultyDepartmentManager
from faculty_set_postprocessor import FacultyPostprocessor
import os
import json

class WosClassification():
    def __init__(self):
        self.utils = Utilities()
        self.faculty_postprocessor = FacultyPostprocessor()
        # Initialize the CategoryProcessor and FacultyDepartmentManager with dependencies
        self.category_processor = CategoryProcessor(self.utils, None)
        
        # Intialize FacultyDepartmentManager
        self.faculty_department_manager = FacultyDepartmentManager(self.category_processor)
        
        # Link CategoryProcessor and FacultyDepartmentManager
        self.category_processor.faculty_department_manager = self.faculty_department_manager
        self.file_handler = FileHandler(self.utils)
    
    def process_directory(self, directory_path):
        """
        Orchestrates the process of reading files from a directory,
        extracting categories, and updating faculty and department data.
        """
        # Use FileHandler to traverse the directory and process each file
        self.file_handler.construct_categories(directory_path, self.category_processor)
    
    def get_category_counts(self):
        """
        Returns the current state of category counts dict
        """
        return self.category_processor.category_counts
    
    def refine_faculty_sets(self):
        self.faculty_postprocessor.remove_near_duplicates(self.get_category_counts())
        self.faculty_department_manager.update_faculty_count()
        self.faculty_department_manager.update_department_count()
    
    def serialize_and_save_data(self, output_path="category_data.json"):
        """
        Serializes category data to JSON and saves it to a file.
        """
        # Prepare category data for serialization using to_dict method from CategoryInfo class from My_Data_Classes.py
        categories_serializable = {category: category_info.to_dict() for category, category_info in self.get_category_counts().items()}
        
        # Serialize to JSON and save to a file
        with open(output_path, 'w') as json_file:
            json.dump(categories_serializable, json_file, indent=4)
            
        print(f"Data serialized and saved to {output_path}")

    
    
if __name__ == "__main__":
    # Define path to the directory containing the WoS txt files you want to process
    directory_path = "~/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities/split_files"
    directory_path = os.path.expanduser(directory_path)
    
    # Instantiate the orchestrator class
    wos_classifiction = WosClassification()
    
    # Process the directory
    wos_classifiction.process_directory(directory_path)
    
    # Refine faculty sets to remove near duplicates and update counts
    wos_classifiction.refine_faculty_sets()
    
    # Serialize the processed data and save it
    wos_classifiction.serialize_and_save_data("processed_category_data.json")
    
    print("Processing complete.")
    