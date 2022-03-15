# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZocdocV2Item(scrapy.Item):

    # define the fields for your item here like:
    name_prefix = scrapy.Field()
    name_first = scrapy.Field()
    name_last = scrapy.Field()
    name_suffix = scrapy.Field()
    specialty = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip = scrapy.Field()
