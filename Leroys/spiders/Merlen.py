import scrapy
from scrapy.http import HtmlResponse

class MerlenSpider(scrapy.Spider):
    name = 'Merlen'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(MerlenSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}&suggest=true']

        #0.41

    def parse(self, response:HtmlResponse):
        product_links = response.xpath("//div[@class='phytpj4_plp largeCard']//a/@href").extract()
        pass
