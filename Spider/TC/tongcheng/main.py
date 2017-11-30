from scrapy import cmdline
import os

os.chdir('tongcheng/spiders')

cmdline.execute('scrapy runspider a58job.py'.split())