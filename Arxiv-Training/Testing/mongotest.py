from pymongo import MongoClient


client = MongoClient('mongodb+srv://cbarbes02:@cluster0.7sjpccn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


db = client['mydatabase']


collection = db['mycollection']

collection.insert_one({'name': 'Alice', 'age': 30})

for document in collection.find():
    print(document)

collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})


collection.delete_one({'name': 'Alice'})

client.close()
