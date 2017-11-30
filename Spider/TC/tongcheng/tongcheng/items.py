# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TongchengItem(scrapy.Item):

    job_url = scrapy.Field()   #详情 url
    job_comp = scrapy.Field()  #公司名
    job_name = scrapy.Field()  # 职位名
    job_degree = scrapy.Field()  # 学历
    job_smoney = scrapy.Field()  # 最低薪资

    job_emoney = scrapy.Field()  # 最高薪资
    job_address = scrapy.Field()  # 公司地址
    job_comp_type = scrapy.Field()  # 公司类型（民营，国企）
    job_comp_snum = scrapy.Field()  # 公司规模（人数）
    job_comp_enum = scrapy.Field()  # 公司规模（人数）

    job_business = scrapy.Field()  # 公司主营 :行业
    job_syear = scrapy.Field()  # 工作经验
    job_eyear = scrapy.Field()  # 工作经验
    job_date_pub = scrapy.Field()  # 发布日期
    job_datetime = scrapy.Field()  # 爬取日志

    job_welfafe = scrapy.Field()  # 公司福利
    job_people = scrapy.Field()  # //招的人数
    job_desc = scrapy.Field()  # 岗位职责
    job_request = scrapy.Field()  # 岗位要求
    job_tag = scrapy.Field()  # 职业标签 //java php等