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
    params = {'page' : None}

    def __init__(self, search):
        self.search = search

    def get_parce(self): # проверка на ответ о сервера
        while True:
            response = requests.get(self.url+self.search, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response
            time.sleep(0.5)

    def search_result(self): # выводит количество найденных вакансий
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('span', {"class": '_2xFS1'})
        k = [[s for s in i.text if s.isdigit()] for i in s_list]
        k = ''.join(k[0])
        return int(k)

    def get_link_href(self): # тот же метод что и get_link только через get('href')
        result = []
        for i in range(self.search_result() // 20 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all('a', class_='_6AfZ9')
            for p in page_list:
                result.append(self.url[:26] + p.get('href'))
        return pd.DataFrame(result)

    def get_post(self):  # парсит наименование вакансий
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('a', class_='_6AfZ9')
        k = [i.text for i in s_list]
        return pd.DataFrame(k)

    def pay(self):  # парсит зарплаты
        result = []
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('span', class_='_2Wp8I')
        l = [i.text.replace('\xa0', '') for i in s_list]
        zp = [''.join([s for s in i if s.isdigit()]) for i in l]
        for i in zp:
            if len(i) > 7:
                pass

    def df_view(self): # объединяет данные в твблицу
        pass

    def import_xls(self): # импортирует, полученные данные в файл xlsx
        pass

    def import_csv(self):
        pass


kuznec = SuperJob('python')
pprint(kuznec.search_result())
