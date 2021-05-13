from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)
db = client['test_database']
collection = db.test_collection
print(collection)