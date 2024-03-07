import json

# load existing JSON data
with open("file_paths.json", "r") as file:
    data = json.load(file)

# Write the JSON data back to the file with indentation for readability
with open("file_paths.json", "w") as file:
    json.dump(data, file, indent=4)
