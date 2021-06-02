import scrapy
from scrapy.http import HtmlResponse
from Leroys.items import LeroyItem
from scrapy.loader import ItemLoader


class MerlenSpider(scrapy.Spider):
    name = 'Merlen'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(MerlenSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}&suggest=true']


    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@data-qa-pagination-item='right']/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        product_links = response.xpath("//div[@class='phytpj4_plp largeCard']//a/@href").extract()
        for link in product_links:
            yield response.follow(link, callback=self.parce_link)

    def parce_link(self, response:HtmlResponse):
        loader = ItemLoader(item=LeroyItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos', "//img[@alt='image thumb']/@src")
        loader.add_value('link', response.url)
        loader.add_xpath('price', "//span[@slot='price']/text()")
        loader.add_xpath('article', "//span[@slot='article']/text()")
        loader.add_xpath('text', "//uc-pdp-section-vlimited/div/p/text()")
        yield loader.load_item()

        # name = response.xpath("//h1/text()").extract_first()
        # photos = response.xpath("//img[@alt='image thumb']/@src").extract()
        # link = response.url
        # price = response.xpath("//span[@slot='price']/text()").extract()
        # article = response.xpath("//span[@slot='article']/text()").extract()
        # text = response.xpath("//uc-pdp-section-vlimited/div/p/text()").extract()
        # item = LeroyItem(name=name, photos=photos, link=link, price=price, article=article, text=text)
        # yield item
