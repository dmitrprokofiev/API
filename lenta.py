import requests
from lxml import html
from pprint import pprint

headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
url = 'https://lenta.ru'
response = requests.get(url, headers=headers)
dom = html.fromstring(response.text)
news = []
elements = dom.xpath("//div[@class='span4']/section/div")
for el in elements:
    new = {}
    names = el.xpath(".//div[@class='titles']//text()")
    link = el.xpath(".//div[@class='titles']//@href")
    new['date'] = el.xpath(".//span/span[1]//text()")
    new['link'] = [url+i if 'lenta' not in i else i for i in link]
    new['names'] = [i.replace('\xa0', '') for i in names]

    news.append(new)

pprint(news)


