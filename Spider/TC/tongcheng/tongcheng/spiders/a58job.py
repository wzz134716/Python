# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from tongcheng.items import TongchengItem
from datetime import timedelta
from scrapy_redis.spiders import RedisCrawlSpider
import re



class A58jobSpider(RedisCrawlSpider):
    name = '58job'
    allowed_domains = ['bj.58.com']
    redis_key = 'A58jobSpider:urls'

    rules = (

        Rule(LinkExtractor(allow=r'http://bj.58.com/[a-z]+/$'), follow=True),
        Rule(LinkExtractor(allow=r'bj.58.com/[a-z]+/\d+x.shtml'), callback='parse_item', follow=True),

    )
    print('-----')
    num_pattern = re.compile(r'\d+')

    def parse_item(self, response):
        # print(response.url)

        item = TongchengItem()

        url = response.url

        job_url = url.split('?')[0]
        print('***')
        print(job_url)


        job_comp = response.xpath('//div[@class="baseInfo_link"]/a/text()').extract()[0]

        job_name = response.xpath('//span[@class="pos_title"]/text()').extract()[0]

        job_degree = response.xpath('//span[@class="item_condition"]/text()').extract()[0]

        if 'daiding' in response.text:
            job_smoney = 0
            job_emoney = 0
        else:
            money = response.xpath('//span[@class="pos_salary"]/text()').extract()[0]
            danwei = response.xpath('//span[@class="font18"]/text()').extract()[0]
            if '元以上/月' in danwei:
                job_smoney = int(money[:-3])
                job_emoney = int(money[:-3])
            else:
                job_smoney = int(money.split('-')[0][:-3])
                job_emoney = int(money.split('-')[1][:-3])

        job_address = response.xpath('//div[@class="pos-area"]/span[2]/text()').extract()[0]

        if 'mqIcon' in response.text:
            job_comp_type = '国企'
        else:
            job_comp_type = '民企'

        job_comp_num = response.xpath('//p[@class="comp_baseInfo_scale"]/text()').extract()[0]
        if '以上' in job_comp_num:
            job_comp_snum = int(job_comp_num[:-3])
            job_comp_enum = int(job_comp_num[:-3])
        else:
            job_comp_snum = int(job_comp_num.lower().replace('人','').split('-')[0])
            job_comp_enum = int(job_comp_num.lower().replace('人','').split('-')[1])

        job_business = response.xpath('//a[@class="comp_baseInfo_link"]/text()').extract()[0]

        job_year = response.xpath('//span[@class="item_condition border_right_None"]/text()').extract()[0]
        if '不限' in job_year:
            job_syear = 0
            job_eyear = 0
        else:
            job_syear = int(job_year.lower().replace('年','').split('-')[0])
            job_eyear = int(job_year.lower().replace('年','').split('-')[1])

        wytime = response.xpath('//span[@class="pos_base_num pos_base_update"]').extract()[0]
        if '天前' in wytime:
            res = self.num_pattern.search(wytime).group()
            job_date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
        else:
            job_date_pub = datetime.datetime.now().strftime('%Y-%m-%d')

        job_datetime = datetime.datetime.now()

        job_welfafe = response.xpath('//span[@class="pos_welfare_item"]/text()').extract()
        job_welfafe = ','.join(job_welfafe)

        job_people = response.xpath('//span[@class="item_condition pad_left_none"]/text()').extract()[0]
        job_people = job_people.lower().replace('招','')
        job_people = job_people.lower().replace('人','')
        job_people = int(job_people)

        job_desc = response.xpath('//div[@class="shiji"]/p/text()').extract()
        job_desc = ' '.join(job_desc)

        job_request = response.xpath('//div[@class="des"]/text()').extract()
        job_request = ' '.join(job_request)

        job_tag = response.xpath('//a[@class="comp_baseInfo_link"]/text()').extract()[0]


        item['job_url'] = job_url
        item['job_comp'] = job_comp
        item['job_name'] = job_name
        item['job_degree'] = job_degree
        item['job_smoney'] = job_smoney
        item['job_emoney'] = job_emoney
        item['job_address'] = job_address
        item['job_comp_type'] = job_comp_type
        item['job_comp_snum'] = job_comp_snum
        item['job_comp_enum'] = job_comp_enum
        item['job_business'] = job_business
        item['job_syear'] = job_syear
        item['job_eyear'] = job_eyear
        item['job_date_pub'] = job_date_pub
        item['job_datetime'] = job_datetime
        item['job_welfafe'] = job_welfafe
        item['job_people'] = job_people
        item['job_desc'] = job_desc
        item['job_request'] = job_request
        item['job_tag'] = job_tag


        def process_date(self, value):
            if '天前' in value:
                res = self.num_pattern.search(value).group()
                date_pub = (datetime.datetime.now() - timedelta(days=int(res))).strftime('%Y-%m-%d')
            else:
                date_pub = datetime.datetime.now().strftime('%Y-%m-%d')
            return date_pub


        yield item
