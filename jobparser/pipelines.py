# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from items import JobparserItem

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancy999

    def process_item(self, item, spider):
        # Здесь обработка item'a
        if spider.name == 'superjob':
            item['_id'] = int(''.join([i for i in item['link'].split('-')[-1] if i.isdigit()]))
            if len(item['salary']) == 3:
                if item['salary'][0] == 'от':
                    item['min_salary'] = int(''.join([i for i in item['salary'][2] if i.isdigit()]))
                    item['max_salary'] = None
                    item['currency'] = ''.join([i for i in item['salary'][2] if i.isalpha()])
                    del item["salary"]
                else:
                    item['min_salary'] = None
                    item['max_salary'] = int(''.join([i for i in item['salary'][2] if i.isdigit()]))
                    item['currency'] = ''.join([i for i in item['salary'][2] if i.isalpha()])
                    del item["salary"]
            elif len(item['salary']) > 3:
                item['min_salary'] = int(''.join([i for i in item['salary'][0] if i.isdigit()]))
                item['max_salary'] = int(''.join([i for i in item['salary'][1] if i.isdigit()]))
                item['currency'] = ''.join([i for i in item['salary'][3] if i.isalpha()])
                del item["salary"]
            else:
                item['min_salary'] = None
                item['max_salary'] = None
                item['currency'] = None
                del item["salary"]

            return item


        # collection = self.mongobase[spider.name]
        # collection.insert_one(item)

        # return item

