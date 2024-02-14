import pandas as pd
import torch
import numpy as np
import json

File = pd.read_csv('../assets/Prop_Data.csv')

# create dictionary of proposals
row_dict = {i: File.loc[i].to_dict() for i in range(0, File.shape[0])}

output_json = 'Proposals.json'

# fill the file
with open(output_json, 'w') as json_file:
    for i in range(0, len(row_dict)):
        json.dump(row_dict[i], json_file, indent=4)

print("Row inserted into JSON file successfully")
