# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotfrogV2Item(scrapy.Item):

    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_phone = scrapy.Field()
    company_address = scrapy.Field()
    company_website = scrapy.Field()
