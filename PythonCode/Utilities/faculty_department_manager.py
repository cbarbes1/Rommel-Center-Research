import warnings

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
        if department_info[0]:
            department_members = department_info[1]
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