# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapy.crawler import Settings


class BigdataPipeline(object):
    quotes_name = 'quotes'
    quotesInsert = '''insert into quotes(text,author,tags)
                        values('{text}','{author}','{tags}')'''

    def __init__(self, settings):
        self.settings = settings


    def process_item(self, item, spider):

        print("==============================================================================================")
        print(item)
        print(item)
        print("==============================================================================================")
        if spider.name == "sp01":
            sqltext = self.quotesInsert.format(
                text=pymysql.escape_string(item['text']),
                author=pymysql.escape_string(item['author']),
                tags=pymysql.escape_string(item['tags']))
            # spider.log(sqltext)
            # self.cursor.execute(sqltext)

        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        print("-------------------------00000000000000--------------")
        print(self.settings.get('MYSQL_HOST'))
        print(self.settings.get('MYSQL_PORT'))
        print(self.settings.get('MYSQL_DBNAME'))
        print(self.settings.get('MYSQL_USER'))
        print(self.settings.get('MYSQL_PASSWD'))
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
