# -*- coding: utf-8 -*-
import scrapy
import datetime

class DentistsEC_Spider(scrapy.Spider):
    name = 'dentists_ec'
    allowed_domains = ['hotfrog.ec']
    start_urls = [
        'https://www.hotfrog.ec/search/ec/dentistas/'
    ]

    # CSV settings
    custom_settings= {
        'FEED_URI': "hotfrog_EC_dentists" + datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M") + ".csv",
           'FEED_FORMAT': 'csv',
           'FEED_EXPORT_FIELDS': [
               'company_phone',
               'company_name',
               'company_address',
           ],
    }

    # Scraper settings
    def parse(self, response):

        # Extract data using xpath
        company_phone=response.xpath('/html/body/main/section/div/div[2]/div/div/div/div[1]/div/a/@href').extract()
        company_name=response.xpath('/html/body/main/section/div/div[2]/div/div/div/div[2]/h3/a/strong/text()').extract()
        company_address=response.xpath('/html/body/main/section/div/div[2]/div/div/div/div[2]/span/text()').extract()

        row_data=zip(company_phone, company_name, company_address)

        # Making extracted data row wise
        for item in row_data:

            # create a dictionary to store the scraped info
            scraped_info = {

                # key:value
                'company_phone':             item[0].strip().replace('tel:+59','+59 '),
                'company_name':              item[1].strip().title().replace('  ',' '),
                'company_address':           item[2].strip().title(),
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
