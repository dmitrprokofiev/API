import requests
from lxml import html
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = "https://news.mail.ru/"
client = MongoClient('127.0.0.1', 27017)
db = client['news_mail']
persons = db.persons

def go():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return html.fromstring(response.text)
    else:
        raise ValueError

def go_parce():
    today = datetime.today()
    news = []
    elements = go().xpath("//ul//li")
    for el in elements:
        new= {}
        new['date'] = today.strftime("%m/%d/%Y") # т.к. новости каждый день новые то присваиваем им сегодняшнюю дату
        new['name'] = ''.join([i.replace('\xa0', '') for i in el.xpath(".//text()")])
        new['link'] = ''.join([i for i in el.xpath(".//@href")])
        new['_id'] = ''.join([i for i in new['link'] if i.isdigit()]) # делаем id уникальным по  id из ссылки для mongoDB

        news.append(new)
    return news

def into_mongo(into):
     for i in into:
         if i not in [s for s in persons.find({})]:
             persons.insert_one(i)


parcing = go_parce()
into_mongo(parcing)
pprint(len([s for s in persons.find({})])) # проверка на добавление не уникальных записей


