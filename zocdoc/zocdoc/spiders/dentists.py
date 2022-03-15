# -*- coding: utf-8 -*-
import scrapy
import datetime

class DentistsSpider(scrapy.Spider):
    name = 'dentists'
    allowed_domains = ['zocdoc.com']
    start_urls = [
        'https://www.zocdoc.com/dentists/new-york-46063pm/%s' % page for page in range(1,10)
    ]

    # CSV settings
    custom_settings= {
        'FEED_URI': "zocdoc_NY_dentists" + datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M") + ".csv",
           'FEED_FORMAT': 'csv',
           'FEED_EXPORT_FIELDS': [
               'name_prefix',
               'name_full',
               'name_suffix',
               'specialty',
               'address',
               'city',
               'state',
               'zip_code',
           ],
    }

    # Scraper settings
    def parse(self, response):

        # Extract data using xpath
        name_prefix=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[1]/a/h3/span[1]/text()').extract()
        name_full=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[1]/a/h3/span[2]').extract()
        name_suffix=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[1]/a/h3/span[3]/text()').extract()
        specialty=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[2]/text()').extract()
        address=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[3]/div/span[1]/text()').extract()
        city=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[3]/div/span[2]/text()').extract()
        state=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[3]/div/span[3]/text()').extract()
        zip_code=response.xpath('//*[@data-test="profList"]/section/div[3]/article/div/div[1]/div/div/div[1]/div[2]/div[3]/div/span[4]/text()').extract()

        row_data=zip(name_prefix, name_full, name_suffix, specialty, address, city, state, zip_code)

        # Making extracted data row wise
        for item in row_data:

            # create a dictionary to store the scraped info
            scraped_info = {

                # key:value
                'name_prefix':       item[0].strip(),
                'name_full':         item[1].strip().replace('<span data-test="doctor-card-info-name-full" itemprop="name">','').replace('<!-- --> <!-- -->',' ').replace('</span>',''),
                'name_suffix':       item[2].strip(),
                'specialty':         item[3].strip(),
                'address':           item[4].strip(),
                'city':              item[5].strip(),
                'state':             item[6].strip(),
                'zip_code':          item[7].strip(),
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
