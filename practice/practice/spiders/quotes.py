# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    # response に取得したHTMLソースが渡される
    def parse(self, response):
        # response.encoding = response.apparent_encoding

        for quote in response.css('div.quote'):
            item = PracticeItem()
            item['author'] = quote.css('small.author::text').extract_first()
            item['text'] = quote.css('span.text::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
