from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd
import time
import openpyxl


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# url = 'https://russia.superjob.ru/vacancy/search/?'
# params = {'keywords' : 'пескоструйщик'}
# response = requests.get(url, headers=headers, params=params)
# dom = bs(response.text, "html.parser")
# s_list = dom.find_all('a', class_='_6AfZ9')
# pprint(s_list)


class SuperJob:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 8.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = 'https://russia.superjob.ru/vacancy/search/?keywords='

    def __init__(self, search):
        self.search = search

    def get_parce(self): # проверка на ответ о сервера
        while True:
            response = requests.get(self.url+self.search, headers=self.headers)
            if response.status_code == 200:
                return response
            time.sleep(0.5)

    def search_result(self): # выводит количество найденных вакансий
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('span', {"class": '_2xFS1'})
        k = [[s for s in i.text if s.isdigit()] for i in s_list]
        k = ''.join(k[0])
        return int(k)


kuznec = SuperJob('пескоструйщик')
pprint(kuznec.search_result())