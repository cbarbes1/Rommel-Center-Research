import json

data = []

# load existing JSON data
with open("arxiv-metadata-oai-snapshot.json", "r") as file:
    for line in file:
        data.append(json.loads(line))

# Write the JSON data back to the file with indentation for readability
with open("arxiv_metadata_formatted.json", "w") as file:
    json.dump(data, file, indent=4)
