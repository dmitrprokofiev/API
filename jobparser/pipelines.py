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
        if spider.name == 'superjob':
            item['_id'] = int(''.join([i for i in item['link'].split('-')[-1] if i.isdigit()]))
            if len(item['salary']) == 3:
                if item['salary'][0] == 'от':
                    item['min_salary'] = int(''.join([i for i in item['salary'][2] if i.isdigit()]))
                    item['max_salary'] = None
                    item['currency'] = ''.join([i for i in item['salary'][2] if i.isalpha()])
                else:
                    item['min_salary'] = None
                    item['max_salary'] = int(''.join([i for i in item['salary'][2] if i.isdigit()]))
                    item['currency'] = ''.join([i for i in item['salary'][2] if i.isalpha()])
            elif len(item['salary']) > 3:
                item['min_salary'] = int(''.join([i for i in item['salary'][0] if i.isdigit()]))
                item['max_salary'] = int(''.join([i for i in item['salary'][1] if i.isdigit()]))
                item['currency'] = ''.join([i for i in item['salary'][3] if i.isalpha()])
            else:
                item['min_salary'] = None
                item['max_salary'] = None
                item['currency'] = None
            del item["salary"]
        elif spider.name == "hhru":
            # item['_id'] = int(item['link'].split('/')[4].split('?')[0])
            # if len(item["salary"]) > 6:
            #     item['min_salary'] = int(item['salary'][1].replace('\xa0', ''))
            #     item['max_salary'] = int(item['salary'][3].replace('\xa0', ''))
            #     item['currency'] = ''.join([i for i in item['salary'][5] if i.isalpha()])
            # elif len(item["salary"]) == 4:

            # else:
            #     item['min_salary'] = None
            #     item['max_salary'] = None
            #     item['currency'] = None
            # del item["salary"]
            return item
        print()

        # collection = self.mongobase[spider.name]
        # collection.insert_one(item)

        # return item

