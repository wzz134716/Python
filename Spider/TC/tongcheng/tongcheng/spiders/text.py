# -*- coding: utf-8 -*-
import scrapy


class TextSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['bj.58.com']
    start_urls = ['http://bj.58.com/zpshengchankaifa/31784788971057x.shtml']

    def parse(self, response):
        url = response.url

        job_comp = response.css('.comp_baseInfo_title .baseInfo_link a::text').extract()[0]
        job_name = response.xpath('//div[@class="pos_base_info"]/span[@class="pos_title"]/text()').extract()[0]
        job_name = response.css('.pos_base_info span::text').extract()[0]


        print(job_comp,job_name)
