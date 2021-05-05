import requests
from pprint import pprint

username = 'dmitrprokofiev'
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url).json()
# 'html_url': 'https://github.com/dmitrprokofiev/API' - tag
# pprint(response[0]['html_url'])
result = [i['html_url'] for i in response]
print('\n'.join(result))