import json


class GetArxivCatsFromJson:
    def __init__(self):
        self.json_file_path = "./arxiv_metadata_formatted.json"
        self.unique_cats_set = set()
        self.unique_cats_list = []
        self.cat_per_ab_list = []
        self.arxiv_ab_cat_dict = {}
        self.vocab_set = set()

    def open_json(self):
        with open(self.json_file_path, "r") as file:
            data = json.load(file)
        return data

    def get_cats(self):
        # open json and read each line
        with open(self.json_file_path, "r") as file:
            data = json.load(file)
            for json_obj in data:
                cats = json_obj["categories"].split(" ")
                self.unique_cats_set.update(cats)
        self.unique_cats_list = list(self.unique_cats_set)
        return self.unique_cats_list

    def get_cats_for_each_abstract(self):
        with open("arxiv_metadata_formatted.json", "r") as file:
            data = json.load(file)
            for json_obj in data:
                # Splitting the 'categories' string into a list of categories
                cats = json_obj["categories"].split()
                # Appending the list of categories for this object to the categories_list
                self.cat_per_ab_list.append(cats)
        return self.cat_per_ab_list

    def get_arxiv_ab_cat_dict(self):
        data = self.open_json()
        for json_obj in data:
            # Extracting the abstract and categories
            ab = json_obj["abstract"]
            cats = json_obj["categories"].split()
            # Using the abstract as the key and the list of categories as the value
            self.arxiv_ab_cat_dict[ab] = cats
        return self.arxiv_ab_cat_dict

    def get_vocab(self):
        data = self.open_json()

        for json_obj in data:
            text = json_obj["abstract"]

            words = text.split()

            self.vocab_set.update(words)

    def get_vocab_set(self):
        return self.vocab_set

    def get_vocab_size(self):
        return len(self.vocab_set)


if __name__ == "__main__":
    extractor = GetArxivCatsFromJson()
    extractor.get_vocab()
    print_set = extractor.get_vocab_set()
    print_size = extractor.get_vocab_size()

    print(print_set)
    print("\n\n")
    print(print_size)
