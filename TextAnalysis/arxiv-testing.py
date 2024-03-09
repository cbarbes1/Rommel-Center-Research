import json

with open("/home/colebarbes/arxiv-metadata.json", "r") as file:
    data = json.load(file)

print(data["Computer Science"])
