import os
import warnings
import pickle

class FileHandler:
    def __init__(self, utils):
        self.utils = utils

    def construct_categories(self, directory_path, category_processor):
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            # ensure it's a file
            if self.check_file_status(file_path):
                with open(file_path, "r") as current_file:
                    category_processor.category_finder(current_file, file_path)
            else:
                warnings.warn(
                    f"Warning: Could not verify file at: {file_path} as a file. Continuing to next file."
                )

    def check_file_status(self, file_path) -> bool:
        if os.path.isfile(file_path):
            return True
        return False
    
    def save_cat_dict(self, file_path: str, cat_dict: dict):
        with open(file_path, "wb") as f:
            pickle.dump(cat_dict, f)