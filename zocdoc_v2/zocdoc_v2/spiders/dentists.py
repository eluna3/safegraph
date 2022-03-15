# -*- coding: utf-8 -*-
import scrapy
import datetime
from zocdoc_v2.items import ZocdocV2Item

class DentistsSpider(scrapy.Spider):
    name = 'dentists'
    allowed_domains = ['zocdoc.com']
    start_urls = [ 'https://www.zocdoc.com/dentists/new-york-46063pm/%s' % page for page in range(1,10) ]

    def parse(self, response):

        selector_object = response.xpath('//article[starts-with(@class,"patient-web-app")]')
        for select in selector_object:
            name_prefix = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-name-prefix")]/text()').extract()
            name_prefix = name_prefix[0].strip() if name_prefix else ''
            name_full = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-name-full")]/text()').extract()
            name_first = name_full[0].strip() if name_full else ''
            name_last = name_full[2].strip() if name_full else ''
            name_suffix = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-name-suffix")]/text()').extract()
            name_suffix = name_suffix[0].strip() if name_suffix else ''
            specialty = select.xpath('.//div[starts-with(@data-test,"doctor-card-info-specialty")]/text()').extract()
            specialty = specialty[0].strip() if specialty else ''
            location = select.xpath('.//div[starts-with(@data-test,"doctor-card-info-location-name")]/text()').extract()
            location = location[0].strip() if location else ''
            address = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-location-address")]/text()').extract()
            address = address[0].strip() if address else ''
            city = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-location-city")]/text()').extract()
            city = city[0].strip() if city else ''
            state = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-location-state")]/text()').extract()
            state = state[0].strip() if state else ''
            zip = select.xpath('.//span[starts-with(@data-test,"doctor-card-info-location-zip")]/text()').extract()
            zip = zip[0].strip() if zip else ''

            item = ZocdocV2Item(
                name_prefix=name_prefix,
                name_first=name_first,
                name_last=name_last,
                name_suffix=name_suffix,
                specialty=specialty,
                location=location,
                address=address,
                city=city,
                state=state,
                zip=zip,
            )
            yield item
