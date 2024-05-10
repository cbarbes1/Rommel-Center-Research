'''
Author: Cole Barbes
Last Updated: 03/27/2024
File Converter class structure to manage all needed file conversions
'''
import pandas as pd

# import torch
import numpy as np
import json
from striprtf.striprtf import rtf_to_text
import csv
import requests
import xml.etree.ElementTree as ET
from .data_class import CitationData, TopicData


class File_Convert:
    # init the process class with a file location
    def __init__(self, path):
        self.path = path
        self.file = None
        self.text = None

    def from_csv(self, output_format):
        '''
        convert the csv file to a pandas data frame
        '''
        self.file = pd.read_csv(self.path)

        if output_format == "json":
            self.to_json("csv")

    def from_rtf(self, output_format):
        '''
        convert the rtf using the library an send the text output to a given type
        '''
        with open(self.path, "r") as self.file:
            rtf_text = self.file.read()

        plain_text = rtf_to_text(rtf_text)
        self.text = plain_text

        if output_format == "json":
            self.to_json("rtf")

    def to_json(self, type):
        if type == "csv":
            # create dictionary of proposals
            row_dict = {
                i: self.file.loc[i].to_dict() for i in range(0, self.file.shape[0])
            }

            output_json = "Proposals.json"

            # fill the file
            with open(output_json, "w") as json_file:
                for i in range(0, len(row_dict)):
                    json.dump(row_dict[i], json_file, indent=4)

            print("Row inserted into JSON file successfully")
        elif type == "rtf":
            txt_list = self.text.splitlines()[6:]

            txt_list = [list(filter(None, item.split("|"))) for item in txt_list]

            txt_list = [i for i in txt_list if len(i) != 0]

            txt_dict = {}
            current_section = None

            for entry in txt_list:
                if len(entry) == 1:  # Get the Section name
                    current_section = entry[0]
                    txt_dict[current_section] = []
                elif len(entry) == 2:  # Extract the Citation
                    txt_dict[current_section].append(
                        {"Citation": entry[0], "Total Citations": entry[1]}
                    )
                elif len(entry) == 3:  # Extract the Journal name entry or a total 
                    # grab the entry that has the totals for the journal
                    if "Total" in entry[0]:
                        txt_dict[current_section].append(
                            {
                                entry[0]: {
                                    "Total Publications": entry[1],
                                    "Total Citations": entry[2],
                                }
                            }
                        )
                    # grab the entry that has the number of publications and the rank of the journal
                    else:
                        txt_dict[current_section].append(
                            {
                                entry[0]: {
                                    "Number of Publications": entry[1],
                                    "Rank": entry[2],
                                }
                            }
                        )
            # output all the json to a json file for each section
            for key, value in txt_dict.items():
                filename = "../../assets/json_data/" + key.replace(" ", "-") + ".json"
                with open(filename, "w") as file:
                    json.dump({key: value}, file, indent=4)
