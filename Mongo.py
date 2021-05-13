from pymongo import MongoClient
from pprint import pprint


client = MongoClient('127.0.0.1', 27017)

db = client['headhunter']

persons = db.persons

print(len([i for i in persons.find({'_id' : "43274836"})]))

# for person in persons.find({'id' : "43274836"}):
#     pprint(person)