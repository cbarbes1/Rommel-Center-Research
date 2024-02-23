import json

try:
    file = open('keyPaths.json', 'r')
except:
    print("file not found")


data = json.load(file)

for i in data['Plant Sciences']:
    print(i)

file.close()