import os
from GeneralUtilities_Backend.file_ops.file_ops import FileOps
from typing import Tuple

class AbstractCategoryMap:
    def __init__(self, Utilities_obj: object, *, dir_path: str):
        self.utilities = Utilities_obj
        self.dir_path = dir_path
        self.file_ops = FileOps(output_dir="/mnt/c/Users/Theki/Desktop/425/Rommel-Center-Research/PythonCode/Utilities/")
        self.results = self.map_abstract_categories(dir_path=self.dir_path)
        self.file_ops.write_json("abstracts_to_categories.json", self.results)

    def map_abstract_categories(self, *, dir_path: str):
        results = {}
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if not os.path.isfile(file_path):
                continue
            
            file_content = self.file_ops.read_file(file_path)
                
            attributes = self.utilities.get_attributes(
                file_content, ["abstract", "wc_pattern"]
            )

            abstract, categories = self.extract_abstract_and_categories(attributes=attributes)
            if abstract:
                results[abstract] = categories
                
        return results
    
    @staticmethod
    def extract_abstract_and_categories(*, attributes: Tuple[bool, str]):
        abstract = attributes["abstract"][1] if ["abstract"][0] else None
        categories = attributes["wc_pattern"][1] if ["wc_pattern"] else []
        return abstract, categories

