import scrapy


class YahooItem(scrapy.Item):
    headline = scrapy.Field()
    # url = scrapy.Field()
