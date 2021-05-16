import requests
from lxml import html
from pymongo import MongoClient
from pprint import pprint

class Yandex_Parce:
    headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    url = "https://yandex.ru/news"

    def __init__(self, region):
        self.region = region

    def go(self):
        self.url = self.url+"/region/"+self.region
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return html.fromstring(response.text)
        else:
            raise ValueError

#     def go_parce(self):
#         news = []
#         elements = self.go().xpath("//div[@class='mg-grid__col mg-grid__col_xs_8']")
#         return elements
#
#
# murmansk = Yandex_Parce('murmansk')
# pprint(murmansk.go())

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = "https://news.mail.ru/"
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)
elements = dom.xpath("//ul//li")
name = dom.xpath("//ul/li//text()")
pprint(len(elements))
pprint(len(name))