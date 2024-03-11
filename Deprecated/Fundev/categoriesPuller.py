import json

try:
    file = open('keyPaths.json', 'r')
except:
    print("file not found")


data = json.load(file)

for i, j in data['Plant Sciences'].items():
    print(i, j)

file.close()