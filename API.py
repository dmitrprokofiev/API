import requests
from pprint import pprint

class Repo:
    def __init__(self, username):
        self.username = username

    def parce(self):
        url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(url)
        return response

    def get_parse(self):
        if self.parce().status_code == 200:
            return self.parce()
        else:
            raise ValueError('Сервер не отвечает')

    def result_parce(self):
        response = self.get_parse().json()
        result = [i['html_url'] for i in response]
        return result

    def output(self):
        print(f"У пользователя {self.username} имеется {len(self.result_parce())} репозиториев:{', '.join(self.result_parce())}")
              #TO DO добавить \n

Dmitrii = Repo('dmitrprokofiev')
Dmitrii.output()
