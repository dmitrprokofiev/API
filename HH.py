import json
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd
import time
import openpyxl

class HH:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = 'https://hh.ru/search/vacancy?clusters=true'
    params = {'enable_snippets' : 'true',
              'salary' : None,
              'st' : 'searchVacancy',
              'text' : None,
              'showClusters' : 'true',
              'page' : None}

    def __init__(self, search):
        self.search = search

    def get_parce(self): # проверка на ответ о сервера
        self.params['text'] = self.search
        while True:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code == 200:
                return response
            time.sleep(1)

    def search_result(self): # выводит количество найденных вакансий
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('h1', class_='bloko-header-1')
        k = [i.text for i in s_list]
        k = k[0].replace('\xa0', '')
        return int(k[:k.index('в')])

    def get_link(self): # парсит ссылки вакансий через срезы
        result = []
        for i in range(self.search_result() // 50 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for p in page_list:
                result.append(str(p).split()[5][6:-1])
        return result

    def get_link_href(self): # тот же метод что и get_link только через get('href')
        result = []
        for i in range(self.search_result() // 50 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'})
            for p in page_list:
                result.append(p.get('href').split('?')[0])
        return result

    def get_post(self): # парсит наименование вакансий
        result = []
        for i in range(self.search_result()//50+1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for i in page_list:
                result.append(i.text)
        return result

    def pay(self):  # парсит зарплаты
        result = []
        for x in range(self.search_result()//50+1):
            self.params['page'] = x
            dom = bs(self.get_parce().text, "html.parser")
            s_list = dom.find_all('div', {'class':'vacancy-serp-item'})
            s = [i.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'}) for i in s_list]
            for i in s:
                if i == None:
                    result.append(i)
                else:
                    result.append(i.text)
        return result

    def pay_iterate(self): # извлекаем зарплату отельно друг от друга
        result = []
        for i in self.pay():
            if i == None:
                i = [None, None]
                result.append(i)
            else:
                m_1 = ''.join(i.split('\u202f'))
                m_2 = [i for i in m_1.split() if i.isdigit()]
                result.append(m_2)
        for i in result:
            if len(i) == 1:
                i.append(i[0])
        return result

    def salary(self): # парсим валюту
        result = []
        for i in self.pay():
            if i == None:
                result.append(i)
            else:
                result.append(i[-4:])
        return result

    def pay_min(self):
        result = []
        for i in self.pay_iterate():
            if i[0] == None:
                result.append(i[0])
            else:
                result.append(int(i[0]))
        return result

    def pay_max(self):
        result = []
        for i in self.pay_iterate():
            if i[1] == None:
                result.append(i[1])
            else:
                result.append(int(i[1]))
        return result

    def parce_id(self): # извлекаем id каждой вакансии
        return [i.split('/')[4] for i in self.get_link_href()]

    def df_view(self): # объединяет данные в твблицу
        data =  pd.concat([pd.Series(self.parce_id()), pd.Series(self.get_post()), pd.Series(self.get_link()),
                          pd.Series(self.pay_min()), pd.Series(self.pay_min()), pd.Series(self.salary())], axis=1)
        data.columns = ['id', 'name', 'link', 'pay_min', 'pay_max', 'salary']
        return data

    def import_xls(self): # импортирует, полученные данные в файл xlsx
        self.df_view().to_excel(f'{self.search}.xlsx')

    def import_csv(self): # есть проблема в присутствии спецсимвола   в зарплате
        self.df_view().to_csv(f'{self.search}.csv')

    # добавить метод преобразования dataframe в json
    # извлечь id вакансий в href + изменить наименования столбцов
    # импортировать json в mongo db
    # переписать метод парсинга зарплат отдельный метод на мин зарплату, и отдельный метод на максимальную зарплату

teacher = HH('python')
result = teacher.search_result()
pprint(result)
# k = '147\xa0вакансий «rust»'
# k = k.replace('\xa0', '')
# pprint(k[:k.index('в')])

