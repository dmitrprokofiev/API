import requests
from pprint import pprint

# username = 'dmitrprokofiev'
# url = f"https://api.github.com/users/{username}/repos"
# response = requests.get(url).json()
#
# result = [i['html_url'] for i in response]
# print('\n'.join(result))

class Repo:
    def __init__(self, username):
        self.username = username

    def parce(self):
        url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(url).json()
        result = [i['html_url'] for i in response]
        return result

Dmitrii = Repo('dmitrprokofiev')
print(Dmitrii.parce())