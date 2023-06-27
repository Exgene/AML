import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MySpider(CrawlSpider):
    name = 'web_crawler'
    start_urls = ['https://www.example.com']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.css('title::text').get()
        images = response.css('img::attr(src)').getall()

        data = {
            'Title': title,
            'Images': images,
            'URL': response.url
        }

        yield data
