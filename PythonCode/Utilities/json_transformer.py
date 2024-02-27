import json

def convert_sets_to_lists(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return {k: convert_sets_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_sets_to_lists(item) for item in obj]
    else:
        return obj

class JsonTransformer():
    def __init__(self):
        self.prefix = "/Users/spencerpresley/COSC425/Spencer/Rommel-Center-Research/PythonCode/Utilities/split_files/"
    
    def make_dict_json(self, dictionary):
        new_dictionary = convert_sets_to_lists(dictionary)
        
        for value in new_dictionary.values():
            if 'files' in value:
                value['files'] = [file_path.replace(self.prefix, '') for file_path in value['files']]
                
        # for key, value in new_dictionary.items():
        #     if 'faculty_set' in value:
        #         value['faculty_set'] = list(value['faculty_set'])
        #     if 'department_set' in value:
        #         value['department_set'] = list(value['department_set'])
        #     if 'article_set' in value:
        #         value['article_set'] = list(value['article_set'])
        #     if 'files' in value:
        #         value['files'] = [file_path.replace(self.prefix, '') for file_path in value['files']]
                
        with open('categories_and_category_metadata.json', 'w') as json_file:
            json.dump(new_dictionary, json_file, indent=4)
            
    def remove_files(self):
        json_file_path = 'categories_and_category_metadata.json'
        
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
            
        # Remove "files" key and values from each category
        for category in data.values():
            if "files" in category:
                del category["files"]
                
        # Write modified data back into json
        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
            
if __name__ == '__main__':
    jt = JsonTransformer()
    jt.remove_files()