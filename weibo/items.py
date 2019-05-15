# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 用户名
    uid = scrapy.Field()
    # 用户转发配字
    uurl = scrapy.Field()
    # 用户名
    uname = scrapy.Field()
    # 用户转发配字
    uword = scrapy.Field()
    # 用户是否VIP
    # vip = scrapy.Field()
    # 用户性别
    gender = scrapy.Field()
    # 用户登记
    urank = scrapy.Field()
    # 用户粉丝数
    followers_count = scrapy.Field()
    # 用户关注数
    follow_count = scrapy.Field()
    pass
