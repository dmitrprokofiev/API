from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)
db = client['headhunter2']
persons = db.persons

def max_pay(sum):
        return [person for person in persons.find({'pay_min': {'$gt': sum}, 'pay_max': {'$gt': sum}})]

pprint(max_pay(100000))

