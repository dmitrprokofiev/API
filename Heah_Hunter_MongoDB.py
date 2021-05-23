from Head_Hunter import HeadHunter

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

            mongoDB.append(mongo)
        return mongoDB


head = Mongo_Hunter()
print(head.add_mongo())