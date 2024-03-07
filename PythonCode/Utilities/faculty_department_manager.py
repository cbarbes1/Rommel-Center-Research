import warnings
import time
class FacultyDepartmentManager:
    def __init__(self, category_processor):
        self.category_processor = category_processor
    
    def update_faculty_set(self, categories, faculty_members):
        for category in categories:
            if category in self.category_processor.category_counts:
                category_info = self.category_processor.category_counts[category]
                for faculty_member in faculty_members:
                    category_info.faculty.add(faculty_member)
            else:
                warnings.warn(f"Warning: Category {category} not found in category_counts. Continuing to next.")
                
    def update_department_set_2(self, categories, department_info):
        if department_info == "Unknown":
            return
        
        
        else:
            department_members = department_info
            for category in categories:
                if category in self.category_processor.category_counts:
                    category_info = self.category_processor.category_counts[category]
                    if isinstance(department_members, list):
                        for department_member in department_members:
                            category_info.departments.add(department_member)
                    elif isinstance(department_members, str):
                        category_info.departments.add(department_members)
                    else:
                        warnings.warn(f"Unexpected department_members type: {type(department_members)}")
                else:
                    warnings.warn(f"WARNING: Category {category} not found in category_counts. Continuing to next category.")
    def update_faculty_count(self):
        for category, category_info in self.category_processor.category_counts.items():
            category_info.faculty_count = len(category_info.faculty)
    
    def update_department_count(self):
        for category, category_info in self.category_processor.category_counts.items():
            category_info.department_count = len(category_info.departments)
            
    def update_article_counts(self, categories_dict):
        """Returns total article count which is = to length of the files set"""
        for _, info in categories_dict.items():
            info.article_count = len(info.files)
        return categories_dict 