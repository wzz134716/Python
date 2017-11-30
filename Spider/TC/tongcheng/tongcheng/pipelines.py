# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('127.0.0.1','root','123456','jobs',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


class TongchengMysqlPipeline(MysqlPipeline):
    def process_item(self,item,spider):
        sql = 'insert into job(job_url,job_comp,job_name,job_degree,job_smoney,job_emoney,job_address,job_comp_type,job_comp_snum,job_comp_enum,job_business,job_syear,job_eyear,job_date_pub,job_datetime,job_welfafe,job_people,job_desc,job_request,job_tag) ' \
              'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update job_date_pub=values(job_date_pub),job_smoney=VALUES(job_smoney),job_emoney=values(job_emoney)'
        try:
            self.cursor.execute(sql,(item["job_url"],item["job_comp"],item["job_name"],item["job_degree"],item["job_smoney"],item["job_emoney"],item["job_address"],item["job_comp_type"],item["job_comp_snum"],item["job_comp_enum"],item["job_business"],item["job_syear"],item["job_eyear"],item["job_date_pub"],item["job_datetime"],item["job_welfafe"],item["job_people"],item["job_desc"],item["job_request"],item["job_tag"]))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print('执行语句失败')
        # 返回交给下一个管道文件处理
        return item

