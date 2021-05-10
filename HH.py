
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
            time.sleep(2)

    def search_result(self): # выводит количество найденных вакансий
        dom = bs(self.get_parce().text, "html.parser")
        s_list = dom.find_all('h1', class_='bloko-header-1')
        k = [[s for s in i.text if s.isdigit()] for i in s_list]
        k = ''.join(k[0])
        return int(k)

    def get_link(self): # парсит ссылки вакансий через срезы
        result = []
        for i in range(self.search_result() // 50 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for p in page_list:
                result.append(str(p).split()[5][6:-1])
        return pd.DataFrame(result)

    def get_link_href(self): # тот же метод что и get_link только через get('href')
        result = []
        for i in range(self.search_result() // 50 + 1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all('a', {'data-qa' : 'vacancy-serp__vacancy-title'})
            for p in page_list:
                result.append(p.get('href'))
        return pd.DataFrame(result)

    def get_post(self): # парсит наименование вакансий
        result = []
        for i in range(self.search_result()//50+1):
            self.params['page'] = i
            dom = bs(self.get_parce().text, "html.parser")
            page_list = dom.find_all(class_='resume-search-item__name')
            for i in page_list:
                result.append(i.text)
        return pd.DataFrame(result)

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
        return pd.DataFrame(result)

    def pay_iterate(self):
        result = []
        for i in self.pay():
            if i == None:
                result.append(i)
            else:
                m_1 = ''.join(i.split('\u202f'))
                m_2 = [''.join((i.split())) for i in m_1 if i.isdigit()]
                m_3 = [i for i in ''.join(m_2)]
                result.append(m_3)
        return result

    def df_view(self): # объединяет данные в твблицу
        return pd.concat([self.get_post(), self.get_link(), self.pay()], axis=1)

    def import_xls(self): # импортирует, полученные данные в файл xlsx
        self.df_view().to_excel(f'{self.search}.xlsx')

    def import_csv(self): # есть проблема в присутствии спецсимвола   в зарплате
        self.df_view().to_csv(f'{self.search}.csv')

teacher = HH('учитель музыки')
pprint(teacher.pay())


# m = ['110\u202f000 – 160\u202f000 руб.',
#  '40\u202f000 – 80\u202f000 руб.',
#  '50\u202f000 – 70\u202f000 руб.', 'до 15\u202f000 руб.']
# m_1 = [''.join(i.split('\u202f')) for i in m]
# m_2 = [i.split() for i in m_1]
# m_3 = [[s for s in i if s.isdigit()] for i in m_2]
# pprint(m_3)
