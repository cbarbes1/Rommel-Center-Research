from GeneralUtilities.PickleDict.PickleDictLoader import PickleDictLoader
from Utilities.My_Data_Classes import CategoryInfo
from FuzzyMatcher import FuzzyMatcher
from PseudoUniqueFaculty import ConstructPseudoUniqueFaculty
import re

class FacultyNameFormatter:
    def __init__(self):
        self.category_dict: dict[str, CategoryInfo] = PickleDictLoader.load_pickle_dict()
        self.format_pattern = re.compile(r'^[A-Za-z]+,\s[A-Za-z]+\s[A-Z]\.$')
        self.pseudo_unique_fac_set = ConstructPseudoUniqueFaculty(self.category_dict).get_pseudo_unique_faculty_set()
        self.refined_and_unique_fac_set = self.construct_formatted_faculty_name_set(self.pseudo_unique_fac_set)
        
        
    def format_faculty_name(self, faculty_name: str) -> str:
        pass

    @staticmethod
    def construct_formatted_faculty_name_set(pseudo_unique_faculty_set: set[str]) -> set[str]:
        for name in pseudo_unique_faculty_set:
            group_key = FuzzyMatcher.is_name_in_group(name)

