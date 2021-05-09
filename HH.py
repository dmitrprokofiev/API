from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd
import time

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# url = 'https://spb.hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=rust&showClusters=true&page=1'
# response = requests.get(url, headers=headers)
# dom = bs(response.text, "html.parser")
# s_list = dom.find_all('h1', class_='bloko-header-1')


class HH:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = 'https://spb.hh.ru/search/vacancy?clusters=true'
    params = {'enable_snippets' : 'true',
              'salary' : None,
              'st' : 'searchVacancy',
              'text' : None,
              'showClusters' : 'true',
              'page' : None}

    def __init__(self, search):
        self.search = search

    def get_parce(self):
        self.params['text'] = self.search
        while True:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response
            time.sleep(0.5)

    def search_result(self):
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('h1', class_='bloko-header-1')
        k = [[s for s in i.text if s.isdigit()] for i in s_list]
        k = ''.join(k[0])
        return int(k)

    def get_link(self):
        result = []
        for i in range(self.search_result() // 50 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for p in page_list:
                result.append(str(p).split()[5][6:-1])
        return pd.DataFrame(result)

    def get_post(self):
        result = []
        for i in range(self.search_result()//50+1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for i in page_list:
                result.append(i.text)
        return pd.DataFrame(result)

    def pay(self):
        # vacancy-serp-item__sidebar
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('div', class_='vacancy-serp-item__sidebar')
        return s_list

    def df_view(self):
        return pd.concat([self.get_post(), self.get_link()], axis=1)

    def import_xls(self):
        pass

rust = HH('ФСБ')
pprint(rust.df_view())

