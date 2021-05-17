import requests
from lxml import html
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = 'https://lenta.ru'
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)

client = MongoClient('127.0.0.1', 27017)
db = client['news_lenta']
persons = db.persons

def parce_news():
    today = datetime.today()
    news = []
    elements = dom.xpath("//div[@class='span4']/section/div")
    for el in elements:
        new = {}
        new['date'] = today.strftime("%m/%d/%Y")  # т.к. новости каждый день новые то присваиваем им сегодняшнюю дату
        names = el.xpath(".//div[@class='titles']//text()")
        link = el.xpath(".//div[@class='titles']//@href")
        new['date'] = ''.join([i for i in el.xpath(".//span/span[1]//text()")])
        new['link'] = ''.join(url+i if 'lenta' not in i else i for i in link)
        new['names'] = ''.join([i.replace('\xa0', '') for i in names])
        new['_id'] = new['link']  # делаем id уникальным по  id из ссылки сайта для mongoDB
        news.append(new)
    return news

def into_mongo(into):
    for i in into:
        if i not in [s for s in persons.find({})]:
            persons.insert_one(i)

parcing = parce_news()
into_mongo(parcing)
pprint(len([s for s in persons.find({})])) # проверка на добавление не уникальных записей
