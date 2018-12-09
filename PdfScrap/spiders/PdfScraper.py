# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 16:39:18 2018

@author: Talha.Iftikhar
"""
import scrapy

class PdfScraper(scrapy.Spider):
    name="pdfscrap"
    start_urls=['https://storpool.com/pdf-materials']
    #print("Outside")
    
    def parse(self, response):
        #print("test")
        for pdfinfo in response.xpath('//div[contains(@class,"x-prompt message-left")]'):
            #print(pdf)
            href=pdfinfo.xpath('//div[contains(@class,"x-prompt-section x-prompt-section-button")]/a/@href').extract()
            for hrefs in href:
                print(hrefs)
                print(1)
                yield scrapy.Request(hrefs, callback=self.save_pdf)
            

        
    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)