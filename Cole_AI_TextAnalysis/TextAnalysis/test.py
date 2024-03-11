topic_dict = {}
abstract_list = []
with open('abstracts_to_categories.json', 'r') as file:
    for line in file:
        data = json.loads(line)
        abstract_list.append(data)

print(abstract_list)