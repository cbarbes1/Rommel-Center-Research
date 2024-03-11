from PythonCode.Utilities.My_Data_Classes import CategoryInfo

class ConstructPseudoUniqueFaculty:
    def __init__(self, data_dict: dict[str, CategoryInfo]):
        self.data_dict: dict[str, CategoryInfo] = data_dict
        self.pseudo_unique_faculty_set: set[str] = set()
        self.construct_pseudo_unique_faculty(self.data_dict, self.pseudo_unique_faculty_set)
        
    @staticmethod    
    def construct_pseudo_unique_faculty(data_dict, pseudo_unique_faculty_set: set[str]) -> None:
        for _, category_info in data_dict.items():
            for faculty in category_info.faculty:
                pseudo_unique_faculty_set.add(faculty)
                
    def get_pseudo_unique_faculty_set(self) -> set[str]:
        return self.pseudo_unique_faculty_set
    

