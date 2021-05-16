import requests
from lxml import html
from pymongo import MongoClient
from pprint import pprint

# class Mail_News:
#     headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
#     url = "https://news.mail.ru/"
#
#
#     def go(self):
#         response = requests.get(self.url, headers=self.headers)
#         if response.status_code == 200:
#             return html.fromstring(response.text)
#         else:
#             raise ValueError
#
#     def go_parce(self):
#         news = []
#         elements = self.go().xpath("//ul//li")
#         for el in elements:
#             new= {}
#             new['name'] = ''.join([i.replace('\xa0', '') for i in el.xpath(".//text()")])
#             new['link'] = ''.join([i for i in el.xpath(".//@href")])
#             new['_id'] = ''.join([i for i in new['link'] if i.isdigit()])
#
#             news.append(new)
#         return news
#
#
# search = Mail_News()
# pprint(search.go())

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = "https://news.mail.ru/"
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)
news = []
elements = dom.xpath("//ul//li")
for el in elements:
    new= {}
    new['name'] = ''.join([i.replace('\xa0', '') for i in el.xpath(".//text()")])
    new['link'] = ''.join([i for i in el.xpath(".//@href")])
    new['_id'] = ''.join([i for i in new['link'] if i.isdigit()])

    news.append(new)
pprint(len(elements))
# pprint(len(name))
pprint(news)