import pandas as pd
#import torch
import numpy as np
import json
from striprtf.striprtf import rtf_to_text
import csv
import requests
import xml.etree.ElementTree as ET
from data_class import CitationData, TopicData 

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

            result = {}
            current_section = None
            current_titles = []

            for item in txt_list:
                if len(item) == 1:  # Section name
                    if current_section is not None:
                        result[current_section] = current_titles
                        current_titles = []
                    current_section = item[0]
                else:  # Title
                    current_titles.append(item)
            print(txt_list)

            final = {key: {} for key in title_list}

            #print(result)
            
            for key, value in result.items():
                for index, i in enumerate(value):
                        if len(i) == 3:
                            final[key][i[0]] = {'Number of Publications':i[1], 'Journal Ranking':i[2], 'Citation List':value[index+1:index+1+int(i[1])]}

            
            with open('output.json', 'w') as file:
                json.dump(final, file, indent=4)


def loadRSS():

    url = 'https://www.salisbury.edu/sitemap.xml'

    resp = requests.get(url)

    with open('feed.xml', 'wb') as f:
        f.write(resp.content)



if __name__ == "__main__":

    loadRSS()