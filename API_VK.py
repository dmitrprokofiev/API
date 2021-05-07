import requests

class VK:
    def __init__(self):
        pass


url = 'https://api.vk.com/method/users.get?user_ids=id205766304&fields=bdate&access_token=7ae4381313757f207145b586be86dde0190155f74ceef9ad1a230d7c8e52742e8927abe03693eb5bb611d&v=5.130'
access_token = '7ae4381313757f207145b586be86dde0190155f74ceef9ad1a230d7c8e52742e8927abe03693eb5bb611d'
response = requests.get(url)
print(response.text)