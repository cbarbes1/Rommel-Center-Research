import pandas as pd
import torch
import numpy as np
import json

class File_Convert():
    # init the process class with a file location
    def __init__(self, path):
        self.path = path
        self.file = None

    def from_csv(self, output_format):
        self.file = pd.read_csv(self.path)

        if output_format == 'json':
            self.to_json()

    def to_json(self):
        # create dictionary of proposals
        row_dict = {i: self.file.loc[i].to_dict() for i in range(0, self.file.shape[0])}

        output_json = 'Proposals.json'

        # fill the file
        with open(output_json, 'w') as json_file:
            for i in range(0, len(row_dict)):
                json.dump(row_dict[i], json_file, indent=4)

        print("Row inserted into JSON file successfully")
