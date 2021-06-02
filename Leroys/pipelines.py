# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from items import LeroyItem

class LeroyPipeline:
    def process_item(self, item, spider):
        print()
        return item

class LeroyPhotos(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except TypeError as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [i[1] for i in results if i[0]]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
