import scrapy


class PracticeItem(scrapy.Item):
    # def __unicode__(self):
    #     return repr(self).decode('unicode_escape')

    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
