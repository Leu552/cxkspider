# coding=utf-8
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy
import requests
from ..items import WeiboItem
from fake_useragent import UserAgent
import random
import json
import time
from scrapy.selector import Selector

ua = UserAgent()

class CxkSpider(scrapy.Spider):


    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'wyf'
    # start_urls = []
    # # 给start_urls加入不同页面的地址
    # for i in range(1,5):
    #     time.sleep(1)
    #     start_urls.append('https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4361379747512186&max_id=4361779607852473&page='+str(i)+'&__rnd='+str(int(time.time())))
    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    # allowed_domains = ['weibo.com']


    def start_requests(self):

        for i in range(22000,30000,2):
            time.sleep(random.randint(1,4))
            headers = {
                'Referer': 'https://m.weibo.cn/detail/4362729449834537',
                'User-Agent': ua.random,
                'X-Requested-With': 'XMLHttpRequest',
            }
            # Cookie='SINAGLOBAL=1505092439785.638.1548912484608; TC-Page-G0=841d8e04c4761f733a87c822f72195f3; _s_tentry=passport.weibo.com; Apache=9246181159618.564.1550212893574; ULV=1550212893586:2:1:1:9246181159618.564.1550212893574:1548912484630; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=5e86081f15aa42603185fffc3db712f7; cross_origin_proto=SSL; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; UM_distinctid=16a1f4014e30-034888a184b62e-58422116-1fa400-16a1f4014e673; un=2978610085@qq.com; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=edef3632d17f5fb3; SSOLoginState=1555324904; YF-Ugrow-SEO-G0=8e667ee9394bfc84054b8fa626d4b0dc; wb_view_log_5681855938=1920*10801; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnaHFwnfa9b6Bn0eVW_jaD5JpX5K2hUgL.Fo-c1h2RSK-4e0n2dJLoI7UhdNiVwHvk; ALF=1586947400; SCF=ApA3TwJO8OkekAZzIkq-v9EJJ7s2OBvMB3YOUA8HJDkRLpQMp7ZAeE6MawHuVMB4HGeoAmRtJq1e3l5otJBkOh0.; SUB=_2A25xscGcDeThGeNI41MZ9SvFyDSIHXVSxrRUrDV8PUNbmtBeLRPTkW9NSD4SFVOkcS02xhwpzupcOpYGDcWIafuA; SUHB=05iqxFrjc87bAc; wvr=6; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74|1555412761|1555412757; webim_unReadCount=%7B%22time%22%3A1555412766585%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D'

            url = 'https://m.weibo.cn/api/statuses/repostTimeline?id=4362729449834537&page=' + str(i)

            yield scrapy.Request(url=url, headers=headers, callback=self.parse)
            # response是根据start_urls请求的结果，也可以用start_requests自己编写
    def parse(self,response):

            print(response)


            # 记得要加 . 表示从当前节点
            # [0]是拿取第一个列表内容文本，如果没有则会拿到一个列表
            x = json.loads(response.body)

            relist = x['data']['data']
            # print(len(relist))
            for i in relist:
                # 理解成实例化吧
                item = WeiboItem()
                utxt = str(i['raw_text']).split('//',1)[0].replace('@','/@').replace(' ','')
                url = str(i['user']['profile_url']).split('//', 1)[1].split('?',1)[0]

                # soup = BeautifulSoup(relist, "html.parser")
                # selector = Selector(response=soup)
                # posts = soup.select('span')
                # for i in posts:
                #


                print('++++++++++++++++++++++++++++++++++++++内容start++++++++++++++++++++++++++++++++++++++++++++++')
                # print(i)
                # print(i['user']['id'])
                # print(utxt)
                item['uid'] = i['user']['id']
                item['uurl'] = url
                item['uname'] = i['user']['screen_name']
                item['uword'] = utxt
                # item['vip'] = utxt
                item['gender'] = i['user']['gender']
                item['urank'] = i['user']['urank']
                item['followers_count'] = i['user']['followers_count']
                item['follow_count'] = i['user']['follow_count']
                print(item['uname'])

                print('++++++++++++++++++++++++++++++++++++++内容end++++++++++++++++++++++++++++++++++++++++++++++')
                # print(soup)
                yield item

