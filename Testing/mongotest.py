from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("localhost", 27017)

# Specify the database name
db = client["newdatabase"]

# Specify the collection name
collection = db["newcollection"]

# Insert a document into the collection
collection.insert_one({"key": "value"})

# Verify that the database exists
print(client.list_database_names())
