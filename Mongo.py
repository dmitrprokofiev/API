from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
db = client['headhunter2']
persons = db.persons

def max_pay(sum):
        return [person for person in persons.find({'pay_min': {'$gt': sum}, 'pay_max': {'$gt': sum}})]

# pprint(max_pay())
#
# for person in persons.find({'pay_max' : 10000.0}):
#          pprint(person)

# persons.find({"stats.attack": {$ne: 40}}):
#          pprint(person)

# for person in persons.find({'pay_min': {'$gt': 50000}, 'pay_max': {'$gt': 50000}}):
#     pprint(person)

pprint(max_pay(100000))

# for person in persons.find({'_id' : '40229865'}):
#          pprint(person)

# for person in persons.find({}):
#          pprint(person)