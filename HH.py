from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# url = 'https://spb.hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text=rust&showClusters=true&page=1'
# response = requests.get(url, headers=headers)
# dom = bs(response.text, "html.parser")
# s_list = dom.find_all(class_='resume-search-item__name')
# pprint([i for i in s_list])


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
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code == 200:
            return response
        else:
            raise ValueError('Сервер не отвечает')

    def get_post(self):
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all(class_='resume-search-item__name')
        return pd.DataFrame([i.text for i in s_list])

    def get_link(self):
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all(class_='resume-search-item__name')
        return pd.DataFrame([str(i).split()[5][6:-1] for i in s_list])

    def page(self):
        result = []
        for i in range(3):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for i in page_list:
                result.append(i.text)
        return pd.DataFrame(result)

    def pay(self):
        pass

    def df_view(self):
        return pd.concat([self.get_post(), self.get_link()], axis=1)

    def import_xls(self):
        pass

rust = HH('rust')
pprint(rust.page())