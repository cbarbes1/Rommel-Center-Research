from fuzzywuzzy import fuzz, process
import collections
from typing import Tuple
from DeducedData.PseudoUniqueFaculty import PseudoUniqueFaculty

class FuzzyMatcher:
    def __init__(self):
        # Lastname, F. is key, list of names that belong to that key
        self.faculty_name_groups: dict[str, list[str]] = collections.defaultdict(list)
        self.pseudo_unique_faculty_set: set[str] = PseudoUniqueFaculty.get_pseudo_unique_faculty_set()
        self._create_groups(self.faculty_name_groups, self.pseudo_unique_faculty_set)
    
    @staticmethod
    def _create_groups(faculty_name_groups: dict[str, list[str]], pseudo_unique_set: set[str]) -> None:
        for faculty_name in pseudo_unique_set:
            if faculty_name == "":
                continue
            if ", " in faculty_name:
                last_name, remainder = FuzzyMatcher._get_last_name_and_remainder(faculty_name)
                first_initial = FuzzyMatcher._get_frist_initial(remainder) if remainder else ''
            else:
                # If there's no comma, split by the first space.
                last_name, first_initial = FuzzyMatcher._extract_last_name_and_initial(faculty_name)
            group_key = (last_name, first_initial)
            faculty_name_groups[group_key].append(faculty_name)
    
    @staticmethod
    def is_name_in_group(name: str, name_groups: dict[str, list[str]]) -> Tuple[bool, list[str]]:
        if ", " in name:
            last_name, remainder = FuzzyMatcher._get_last_name_and_remainder(name)
            first_initial = FuzzyMatcher._get_frist_initial(remainder) if remainder else ''
        else:
            last_name, first_initial = FuzzyMatcher._extract_last_name_and_initial(name)
        group_key = (last_name, first_initial)
        
        if group_key in name_groups:
            return True, name_groups[group_key]
        return False, []
        
    @staticmethod
    def _get_last_name_and_remainder(name:str ) -> Tuple[str, str]:
        last_name, remainder = name.split(", ", 1)
        return last_name, remainder

    @staticmethod
    def _get_frist_initial(remainder: str) -> str:
        return remainder[0]

    @staticmethod
    def _extract_last_name_and_initial(faculty_name: str) -> tuple:
        parts = faculty_name.split(" ", 1)
        if len(parts) == 2:
            last_name, remainder = parts
            first_initial = remainder[0] if remainder else ''
        else:
            # Case for when name is just one string, assumes string is the last name
            last_name = faculty_name
            first_initial = ''
        return last_name, first_initial

