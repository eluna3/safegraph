# -*- coding: utf-8 -*-
import scrapy
import datetime
from hotfrog_v2.items import HotfrogV2Item

# Country URLs
latin_america = []
url_ar = [ 'https://www.hotfrog.com.ar/search/ar/dentistas/%s' % page for page in range(1,7) ]
url_br = [ 'https://www.hotfrog.com.br/search/br/dentistas/%s' % page for page in range(1,51) ]
url_cl = [ 'https://www.hotfrog.cl/search/cl/dentistas/%s' % page for page in range(1,7) ]
url_co = [ 'https://www.hotfrog.com.co/search/co/dentistas/%s' % page for page in range(1,4) ]
url_ec = [ 'https://www.hotfrog.ec/search/ec/dentistas/' ]
url_mx = [ 'https://www.hotfrog.com.mx/search/mx/dentistas/%s' % page for page in range(1,22) ]
url_pe = [ 'https://www.hotfrog.com.pe/search/pe/dentistas/%s' % page for page in range(1,2) ]

# Combine lists
latin_america.extend(url_ar)
latin_america.extend(url_br)
latin_america.extend(url_cl)
latin_america.extend(url_co)
latin_america.extend(url_ec)
latin_america.extend(url_mx)
latin_america.extend(url_pe)

class DentistsSpider(scrapy.Spider):
    name = 'dentists'
    allowed_domains = ['hotfrog.com']
    start_urls = latin_america

    def parse(self, response):

        selector_object = response.xpath('//div[starts-with(@class,"hf-box")]')
        for select in selector_object:
            company_phone = select.xpath('./div/div/div[1]/div/a/@href').extract()
            company_phone = company_phone[0].strip().replace('tel:','') if company_phone else ''
            company_name = select.xpath('./div/div/div[2]/h3/a/strong/text()').extract()
            company_name = company_name[0].strip().title()
            company_address = select.xpath('./div/div/div[2]/span/text()').extract()
            company_address = company_address[0].strip().title().split(", ") if company_address else ''
            company_website = select.xpath('./div/div/div[2]/p/small/span/a/@data-href').extract()
            company_website = company_website[0].strip() if company_website else ''

            item = HotfrogV2Item(
                company_name=company_name,
                company_phone=company_phone,
                company_address=company_address,
                company_website=company_website,
            )
            yield item
