from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Leroys import settings
from Leroys.spiders.Merlen import MerlenSpider

if __name__=='__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(MerlenSpider, search='шкаф')

    process.start()