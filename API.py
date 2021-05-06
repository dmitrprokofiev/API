import requests
import json

class Repo:
    def __init__(self, username):
        self.username = username

    def parce(self):
        url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(url)
        return response

    def get_parse(self): # проверка ответа от сервера
        if self.parce().status_code == 200:
            return self.parce()
        else:
            raise ValueError('Сервер не отвечает')

    def result_parce(self): # охраняем список репозиториев пользователя
        response = self.get_parse().json()
        result = [i['html_url'] for i in response]
        return result

    def output(self): # выводим в удобочитаемый вид
        print(f"У пользователя {self.username} имеется {len(self.result_parce())} репозиториев:{', '.join(self.result_parce())}")
              #TO DO добавить \n

    def save_json(self): # сохраняем в json-файл
        with open('repo_{}.json'.format(self.username), 'w', encoding='utf-8') as js:
            js.write(json.dumps(self.parce().json(), ensure_ascii=False))

Dmitrii = Repo('dmitrprokofiev')
# Apache = Repo('apache')
Dmitrii.output()
# Dmitrii.save_json()