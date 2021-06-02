# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst

def change_url(value):
    try:
        result = value.replace('w_82', 'w_2000').replace("h_82", 'h_2000')
        return result
    except Exception:
        return value

class LeroyItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field(input_processor=MapCompose(change_url))
    link = scrapy.Field()
    price = scrapy.Field()
    article = scrapy.Field()
    text = scrapy.Field()
