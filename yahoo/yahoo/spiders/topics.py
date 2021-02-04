import scrapy
from yahoo.items import YahooItem


class TopicsSpider(scrapy.Spider):
    name = 'topics'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://yahoo.co.jp/']

    def parse(self, response):
        for topic in response.css('div#tabTopics1'):
            item = YahooJapanItem()
            item['headline'] = topic.css('a::text').extract()
            yield item
