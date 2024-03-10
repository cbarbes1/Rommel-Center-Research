import json


def convert_sets_to_lists(obj):
    """Recursively convert sets in the object to lists for JSON serialization."""
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return {k: convert_sets_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_sets_to_lists(item) for item in obj]
    else:
        return obj


class JsonTransformer:
    def __init__(self):
        # Initialization can include any required setup. The prefix is no longer needed.
        pass

    def make_dict_json(self, dictionary):
        """
        Serializes a dictionary to a JSON file, converting sets to lists as needed.
        Assumes that the dictionary values may already be partially serialized by CategoryInfo.to_dict().

        Parameters:
            dictionary (dict): The dictionary to serialize, where values are expected to be dictionaries themselves.
        """
        # Convert sets to lists in the dictionary for JSON serialization.
        # This is a precaution in case there are nested sets not handled by CategoryInfo.to_dict().
        new_dictionary = convert_sets_to_lists(dictionary)

        # Serialize the dictionary to JSON, writing to 'categories_and_category_metadata.json'.
        with open("categories_and_category_metadata.json", "w") as json_file:
            json.dump(new_dictionary, json_file, indent=4)

if __name__ == "__main__":
    jt = JsonTransformer()
    jt.remove_files()
