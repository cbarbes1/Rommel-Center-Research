import json

with open('categories_and_category_metadata.json', 'r') as file:
    data = json.load(file)

print(data)