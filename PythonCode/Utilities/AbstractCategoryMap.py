import os
from GeneralUtilities_Backend.file_ops.file_ops import FileOps

class AbstractCategoryMap:
    def __init__(self, Utilities):
        self.utilities = Utilities
        self.file_ops = FileOps(output_dir="/mnt/c/Users/Theki/Desktop/425/Rommel-Center-Research/PythonCode/Utilities/")
        self.results = self.map_abstract_categories()
        self.file_ops.write_json("abstracts_to_categories.json", self.results)

    def map_abstract_categories(self):
        dir_path = "./split_files"
        results = {}
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r") as file:
                    file_content = file.read()
                attributes = self.utilities.get_attributes(
                    file_content, ["abstract", "wc_pattern"]
                )

                abstract = attributes["abstract"][1] if ["abstract"][0] else None
                categories = attributes["wc_pattern"][1] if ["wc_pattern"] else []

                if abstract:
                    results[abstract] = categories
        return results