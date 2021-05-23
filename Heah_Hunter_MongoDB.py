from Head_Hunter import HeadHunter
from pprint import pprint

class Mongo_Hunter(HeadHunter):
    def add_mongo(self):
        mongoDB = []
        page_list = self.soup.find_all('div', {'class': 'vacancy-serp-item'}) or \
                    self.soup.find_all('div', {'class': 'vacancy-serp-item vacancy-serp-item_premium'})
        for p in page_list:
            mongo = {}
            mongo['link'] = p.find('a', {'class' : 'bloko-link'}).get('href').split('?')[0]
            mongo['name'] = p.find('a', {'class' : 'bloko-link'}).text
            mongo['_id'] = int(mongo['link'].split('/')[-1])

            try:
                pay = p.find('span', {'data-qa' : 'vacancy-serp__vacancy-compensation'}).text.replace('\u202f', '')
                if pay.split()[0].isdigit():
                    mongo["pay_min"] = int(pay.split()[0])
                    mongo["pay_max"] = int(pay.split()[2])
                    mongo["currency"] = pay.split()[3]
                else:
                    mongo["pay_min"] = int(pay.split()[1])
                    mongo["pay_max"] = mongo["pay_min"]
                    mongo["currency"] = pay.split()[2]
            except:
                mongo["pay_min"] = None
                mongo["pay_max"] = None
                mongo["currency"] = None

            mongoDB.append(mongo)
        return mongoDB


head = Mongo_Hunter()
pprint(head.add_mongo())