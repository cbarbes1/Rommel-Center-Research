import pandas as pd
#import torch
import numpy as np
import json
from striprtf.striprtf import rtf_to_text

class File_Convert():
    # init the process class with a file location
    def __init__(self, path):
        self.path = path
        self.file = None
        self.text = None

    def from_csv(self, output_format):
        self.file = pd.read_csv(self.path)

        if output_format == 'json':
            self.to_json('csv')
    def from_rtf(self, output_format):
        with open(self.path, 'r') as self.file:
            rtf_text = self.file.read()
        
        plain_text = rtf_to_text(rtf_text)
        self.text = plain_text

        if output_format == 'json':
            self.to_json('rtf')
    
    def from_WOS(self):
        with open(self.path, 'r') as file:
          self.file = file.read()
          self.file = self.file.splitlines()
          self.file = [i for i in self.file if 'AB ' in i]
          with open('./abstracts.txt', 'w') as outfile:
            print(self.file, file=outfile)
          
        

    def to_json(self, type):
        if type == 'csv':
            # create dictionary of proposals
            row_dict = {i: self.file.loc[i].to_dict() for i in range(0, self.file.shape[0])}

            output_json = 'Proposals.json'

            # fill the file
            with open(output_json, 'w') as json_file:
                for i in range(0, len(row_dict)):
                    json.dump(row_dict[i], json_file, indent=4)

            print("Row inserted into JSON file successfully")
        elif type == 'rtf':
            txt_list = self.text.splitlines()[6:]
            txt_list = [list(filter(None, item.split('|'))) for item in txt_list]
            title_list = [i[0] for i in txt_list if len(i) == 1] 
            txt_dict = {key[0]: [] for index, key in enumerate(txt_list) if len(key) == 1}

            for i in txt_list:
                if i not in title_list:
                    print(i)
            print(title_list)
            print(txt_dict)
            print(txt_list[0:10])
            
            #print(txt_list)