import requests
from pprint import pprint

class VK:
    _acces_token = '7ae4381313757f207145b586be86dde0190155f74ceef9ad1a230d7c8e52742e8927abe03693eb5bb611d'

    def __init__(self, id):
        self.id = id

    def friends_get(self):
        url = 'https://api.vk.com/method/friends.get?user_id={}&fields=bdate&access_token={}&v=5.130'.format(self.id, self._acces_token)
        response = requests.get(url)
        response = response.json()
        for i in response['response']['items']:
            print(i['first_name'], i['last_name'], i['id'])

    def bannned(self): # черный список
        url = 'https://api.vk.com/method/account.getBanned?user_id={}&fields=bdate&access_token={}&v=5.130'.format(self.id, self._acces_token)
        response = requests.get(url)
        response = response.json()
        for i in response['response']['profiles']:
            print(i['first_name'], i['last_name'])

Buchkin = VK('46454373')
Ageev = VK('134066584')
Dmitrii = VK('320944047')
# pprint(Buchkin.friends_get())
# print(Buchkin.bannned())
pprint(Dmitrii.friends_get())