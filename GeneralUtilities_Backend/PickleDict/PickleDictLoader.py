from PythonCode.Utilities.My_Data_Classes import CategoryInfo
import pickle

class PickleDictLoader:
    def __init__(self, pickle_path: str):
        self.pickle_path: str = pickle_path
        self.loaded_dict: dict = pickle.load(open(self.pickle_path, "rb"))

    def get_loaded_dict(self) -> dict:
        return self.loaded_dict