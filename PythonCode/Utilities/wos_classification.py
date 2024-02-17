from utilities import Utilities
import os
import json
import warnings
import time
from json_transformer import JsonTransformer

#random comment so i can re-push

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
        file_content = current_file.read()
        lines = file_content.splitlines()
        for line in lines:
            if line.startswith('WC'):
                #TODO:categories = self.utils.wos_category_splitter(line)
                #print(f'CategoryFinder_1: {categories}')
                #TODO:categories = self.initialize_categories(categories)
                #print(f'CategoryFinder_2: {categories}')
                #TODO:categories = self.update_category_counts_files_set(categories, file_path)
                #print(f'CategoryFinder_3: {categories}')
                #self.update_faculty_count(categories)
                #file_content = current_file.read()
                #print(file_content)
                attributes_to_retrieve = ['author', 'department', 'wc_pattern']
                
                #faculty_member = self.utils.get_attributes(entry_text=file_content, attributes=attributes_to_retrieve)
                attribute_results = self.utils.get_attributes(entry_text=file_content, attributes=attributes_to_retrieve)
                categories = attribute_results['wc_pattern'][1]
                self.initialize_categories(categories=categories)
                self.update_category_counts_files_set(categories=categories, file_name=file_path)
                print(f'ATTRIBUTE RESULTS: {attribute_results}')
                faculty_members = attribute_results['author'][1] if attribute_results['author'][0] else 'Unknown'
                department_members = attribute_results['department'][1] if attribute_results['department'][0] else 'Unknown'
                
                print(f'FACULTY MEMBERS: {faculty_members}')
                print(f'DEPARTMENT MEMBERS: {department_members}')
                #time.sleep(5)
                #print(f'Faculty Member: {faculty_member}')
                #print(f'FACULTY_MEMBER_VALUES: {faculty_member.values()}')
                self.update_faculty_set(categories, faculty_members)
                self.update_faculty_count()
                
                self.update_department_set_2(categories, department_members)
                self.update_department_count()
                
                #time.sleep(5)
                #print(f'Faculty_Member: {faculty_member}')
                #time.sleep(10)
                #categories = self.update_faculty_set(categories, faculty_member)

                # DEPARTMENT FETCHING
                
    def initialize_categories(self, categories):
        print(f'Intialize_Categories: {categories}')
        for i, category in enumerate(categories):
            # if category starts with 'WC ', remove it
            if category.startswith('WC '):
                categories[i] = category[3:]
                category = categories[i]
                
            if category not in self.category_counts:
                self.category_counts[category] = {
                    'faculty_count': 0,
                    'department_count': 0,
                    'article_count': 0,
                    'files': set(),
                    'faculty_set': set(),
                    'department_set': set(),
                    'article_set': set()
                }
            #print(f'Category: {category}')
            #print(f'Category Count: {self.category_counts[category]}')
            #print("\n\n")
            #time.sleep(4)
        #return categories
        
    def update_faculty_count(self):
        for category_values in self.category_counts.values():
            category_values['faculty_count'] = len(category_values['faculty_set'])
    
    def update_department_count(self):
        for category_values in self.category_counts.values():
            category_values['department_count'] = len(category_values['department_set'])
    
    def update_category_counts_files_set(self, categories, file_name):
        print(f'Update_Category_Counts_Files_Set: {categories}')
        for category in categories:
            if category in self.category_counts:
                #print(f'Category: {category}')
                #print(f'File: {file_name}')
                #print("\n\n")
                #time.sleep(4)
                self.category_counts[category]['files'].add(file_name)
            else:
                warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next category.")
                continue
        #return categories
    
    def update_faculty_set(self, categories, faculty_members):
        # Assign the tuple of values from the faculty_member author key
        #is_faculty, authors = faculty_member['author']
        #if is_faculty:
        for category in categories:
            if category in self.category_counts:
                for faculty_member in faculty_members: # iterate over each author in list
                    self.category_counts[category]['faculty_set'].add(faculty_member)
            else:
                warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next category.")
                continue
        #else:
        #    raise ValueError("Failure in update_faculty_set")
    
    #def update_department_set(self, categories, department_members):
        # Assign tuple of values from department_member department key
        #is_department, departments = department_member['department']
        #if is_department:
     #   print(f'DEPARTEMENT MEMBERS: {department_members}')
      #  for category in categories:
       #     if category in self.category_counts:
        #        for department_member in department_members: # iterate over each department in list
         #           print(f'Department Member: {department_member}')
          #          time.sleep(4)
           #         self.category_counts[category]['department_set'].add(department_member)
           # else:
            #    warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next category.")
             #   continue
        #else:
            #raise ValueError("Failure in update_department_set")"""
        
    def update_department_set_2(self, categories, department_info):
        # check if department_info tuple indicates a success
        if department_info[0]:
            department_members = department_info[1] # extract department names
            if isinstance(department_members, list): # if there are multiple department names
                for category in categories:
                    if category in self.category_counts:
                        for department_member in department_members:
                            self.category_counts[category]['department_set'].add(department_member)
                    else:
                        warnings.warn(f'WARNING: Category {category} not found in category_counts. Continuing to next category.')           
            elif isinstance(department_members, str): # if there's only one department name
                for category in categories:
                    if category in self.category_counts:
                        self.category_counts[category]['department_set'].add(department_members)
                    else:
                        warnings.warn(f"WARNING: Category {category} not found in category_counts. Continuing to next category.")
        else:
            # handle case where department_info extraction was unsuccessful
            print("Department info extraction was unsuccessful!")     
        
if __name__ == "__main__":
    split_files_directory_path = "~/Desktop/425testing/ResearchNotes/Rommel-Center-Research/PythonCode/Utilities/split_files"
    #split_files_directory_path = "/Users/spencerpresley/COSC425/Spencer/Rommel-Center-Research/PythonCode/Utilities/split_files"
    split_files_directory_path = os.path.expanduser(split_files_directory_path)
    
    wos = WosClassification()
    wos.construct_categories(directory_path=split_files_directory_path)
    json_maker = JsonTransformer()
    
    categories = wos.get_category_counts()
    """iter_dict = iter(categories.items())
    for i in range(2):
        key, value = next(iter_dict)
        print(f'Key: {key}')
        print(f'Value: {value}')
        print("\n\n")"""
    print("\n\n")
    print(f"\n\nCATEGORIES: {sorted(categories.keys())}\n\n")
    for key, value in categories.items():
        print(f'Key: {key}')
        print(f'Value: {value}')
        print("\n\n")
        #time.sleep(4)"""
    json_maker.make_dict_json(categories)
    
    """paper title as key, number 0 to amount of papers as value. So paper1.txt: 0
    
    make another dict where you have those values 0-amount of papers as keys and then abstracts as values sorted
    
    0: abstractForPaper0
    
    sort that dictionary and pull the abstracts into a list
    so [0abstract, 1abstract,...]
    
    when we get the topics back like
    [0topic, 1topic, 2topic, etc]
    
    go back to the first dictionary and find the paper key associated with the index value and assign it that indices category"""
    

    
    
    
