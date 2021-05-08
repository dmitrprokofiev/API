from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
url = 'https://spb.hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=rust&showClusters=true&page=2'
response = requests.get(url, headers=headers)
dom = bs(response.text, "html.parser")
s_list = dom.find_all(class_='resume-search-item__name')
pprint(len(s_list))
