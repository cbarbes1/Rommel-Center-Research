from utilities import Utilities
import os
import json
import warnings
import time
from json_transformer import JsonTransformer
from faculty_set_postprocessor import FacultyPostprocessor
from My_Data_Classes import CategoryInfo

# random comment so i can re-push


class WosClassification:
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
                with open(file_path, "r") as current_file:
                    self.category_finder(current_file, file_path)
            else:
                warnings.warn(
                    f"Warning: Could not verify file at: {file_path} as a file. Continuing to next file."
                )
                continue

    def check_file_status(self, file_path) -> bool:
        if os.path.isfile(file_path):
            return True
        return False

    def category_finder(self, current_file, file_path):
        file_content = current_file.read()
        lines = file_content.splitlines()
        for line in lines:
            if line.startswith("WC"):
                attributes_to_retrieve = ["author", "department", "wc_pattern"]

                attribute_results = self.utils.get_attributes(
                    entry_text=file_content, attributes=attributes_to_retrieve
                )
                categories = attribute_results["wc_pattern"][1]
                self.initialize_categories(categories=categories)
                self.update_category_counts_files_set(
                    categories=categories, file_name=file_path
                )

                faculty_members = (
                    attribute_results["author"][1]
                    if attribute_results["author"][0]
                    else "Unknown"
                )
                department_members = (
                    attribute_results["department"][1]
                    if attribute_results["department"][0]
                    else "Unknown"
                )

                self.update_faculty_set(categories, faculty_members)
                self.update_faculty_count()

                self.update_department_set_2(categories, department_members)
                self.update_department_count()

    def initialize_categories(self, categories):
        for i, category in enumerate(categories):
            # if category starts with 'WC ', remove it
            if category.startswith("WC "):
                categories[i] = category[3:]
                category = categories[i]

            if category not in self.category_counts:
                # Intialize a new CategoryInfo dataclass instance for the given category
                self.category_counts[category] = CategoryInfo()

    def update_faculty_count(self):
        for category, category_info in self.category_counts.items():
            category_info.faculty_count = len(category_info.faculty)

    def update_department_count(self):
        for category, category_info in self.category_counts.items():
            category_info.department_count = len(category_info.departments)

    def update_category_counts_files_set(self, categories, file_name):
        for category in categories:
            if category in self.category_counts:
                self.category_counts[category].files.add(file_name)
            else:
                warnings.warn(
                    f"Warning: Category {category} not found in category_counts. Continuing to next category."
                )

    def update_faculty_set(self, categories, faculty_members):
        # Assign the tuple of values from the faculty_member author key
        # is_faculty, authors = faculty_member['author']
        # if is_faculty:
        for category in categories:
            if category in self.category_counts:
                category_info = self.category_counts[category]
                for faculty_member in faculty_members:
                    category_info.faculty.add(faculty_member)
            else:
                warnings.warn(
                    f"Warning: Category {category} not found in category_counts. Continuing to next."
                )

    def update_department_set_2(self, categories, department_info):
        # Check if department_info tuple indicates a success
        if department_info[0]:
            department_members = department_info[1]  # Extract department names
            for category in categories:
                if category in self.category_counts:
                    category_info = self.category_counts[category]
                    # Check if there are multiple department names or a single one
                    if isinstance(
                        department_members, list
                    ):  # If there are multiple department names
                        for department_member in department_members:
                            category_info.departments.add(department_member)
                    elif isinstance(
                        department_members, str
                    ):  # If there's only one department name
                        category_info.departments.add(department_members)
                    else:
                        warnings.warn(
                            f"Unexpected department_members type: {type(department_members)}"
                        )
                else:
                    warnings.warn(
                        f"WARNING: Category {category} not found in category_counts. Continuing to next category."
                    )
        else:
            # Handle case where department_info extraction was unsuccessful
            print("Department info extraction was unsuccessful!")


if __name__ == "__main__":
    split_files_directory_path = "~/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities/split_files"
    split_files_directory_path = os.path.expanduser(split_files_directory_path)

    wos = WosClassification()
    processor = FacultyPostprocessor()
    json_maker = JsonTransformer()

    # Construct categories by processing files in the directory
    wos.construct_categories(directory_path=split_files_directory_path)

    # Get category counts, now from CategoryInfo instances
    categories = wos.get_category_counts()
    print(f"Cats: {categories}")

    processor.remove_near_duplicates(category_dict=categories)

    wos.update_faculty_count()
    wos.update_department_count()

    categories_serializable = {
        category: category_info.to_dict()
        for category, category_info in categories.items()
    }
    json_maker.make_dict_json(categories_serializable)
    print(f"Processed Categories: {categories_serializable}")

    """paper title as key, number 0 to amount of papers as value. So paper1.txt: 0
    
    make another dict where you have those values 0-amount of papers as keys and then abstracts as values sorted
    
    0: abstractForPaper0
    
    sort that dictionary and pull the abstracts into a list
    so [0abstract, 1abstract,...]
    
    when we get the topics back like
    [0topic, 1topic, 2topic, etc]
    
    go back to the first dictionary and find the paper key associated with the index value and assign it that indices category"""
