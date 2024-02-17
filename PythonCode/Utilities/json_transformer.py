import json

class JsonTransformer():
    def __init__(self):
        self.prefix = "/Users/spencerpresley/COSC425/Spencer/Rommel-Center-Research/PythonCode/Utilities/split_files/"
    
    def make_dict_json(self, dictionary):
        new_dictionary = dictionary
        for key, value in new_dictionary.items():
            if 'faculty_set' in value:
                value['faculty_set'] = list(value['faculty_set'])
            if 'department_set' in value:
                value['department_set'] = list(value['department_set'])
            if 'article_set' in value:
                value['article_set'] = list(value['article_set'])
            if 'files' in value:
                value['files'] = [file_path.replace(self.prefix, '') for file_path in value['files']]
                
        with open('categories_and_category_metadata.json', 'w') as json_file:
            json.dump(new_dictionary, json_file, indent=4)