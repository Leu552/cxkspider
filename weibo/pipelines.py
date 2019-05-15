# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings


class WeiboPipeline(object):
    def __init__(self, ):
        self.conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            user=settings.MYSQL_USER,
            port=3306,
            passwd=settings.MYSQL_PASSWORD,
            db=settings.MYSQL_DBNAME,
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 调用插入数据的方法
        self.insertData(item)
        return item

 # 插入数据方法
    def insertData(self, item):
        try:
            sql = "INSERT INTO wyf_repost (uid, uname, uurl, word,urank, followers_count, follow_count, gender) VALUES (%s, '%s', '%s', '%s', %s, %s, %s, '%s')"
            # print(sql)
            params = (item['uid'], item['uname'], item['uurl'], item['uword'], item['urank'], item['followers_count'], item['follow_count'], item['gender'])
            print(sql % params)
            self.cursor.execute(sql % params)
            self.conn.commit()
            print(self.conn.commit())
        except Exception as error:
            print(error)
            pass
        return item