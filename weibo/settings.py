# -*- coding: utf-8 -*-
import random
from fake_useragent import UserAgent
ua = UserAgent()


PROXIES = ['http://116.209.54.2:9999', 'http://61.176.223.7:58822', 'http://183.148.146.206:9999',
           'http://110.52.235.38:9999', 'http://110.52.235.44:9999', 'http://116.209.58.167:9999',
           ]
# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#         'Host': 'weibo.com',
#         'User-Agent': ua.random,
#         'X-Requested-With': 'XMLHttpRequest',
#         'Cookie': 'SINAGLOBAL=1505092439785.638.1548912484608; TC-Page-G0=841d8e04c4761f733a87c822f72195f3; _s_tentry=passport.weibo.com; Apache=9246181159618.564.1550212893574; ULV=1550212893586:2:1:1:9246181159618.564.1550212893574:1548912484630; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=5e86081f15aa42603185fffc3db712f7; cross_origin_proto=SSL; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; UM_distinctid=16a1f4014e30-034888a184b62e-58422116-1fa400-16a1f4014e673; un=2978610085@qq.com; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=edef3632d17f5fb3; SSOLoginState=1555324904; YF-Ugrow-SEO-G0=8e667ee9394bfc84054b8fa626d4b0dc; wb_view_log_5681855938=1920*10801; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnaHFwnfa9b6Bn0eVW_jaD5JpX5K2hUgL.Fo-c1h2RSK-4e0n2dJLoI7UhdNiVwHvk; ALF=1586947400; SCF=ApA3TwJO8OkekAZzIkq-v9EJJ7s2OBvMB3YOUA8HJDkRLpQMp7ZAeE6MawHuVMB4HGeoAmRtJq1e3l5otJBkOh0.; SUB=_2A25xscGcDeThGeNI41MZ9SvFyDSIHXVSxrRUrDV8PUNbmtBeLRPTkW9NSD4SFVOkcS02xhwpzupcOpYGDcWIafuA; SUHB=05iqxFrjc87bAc; wvr=6; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74|1555412761|1555412757; webim_unReadCount=%7B%22time%22%3A1555412766585%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D'
#     }
HTTPERROR_ALLOWED_CODES = [403]
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'weibo.middlewares.ProxyMiddleware': 123,
   'weibo.middlewares.WeiboDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'weibo.pipelines.WeiboPipeline': 300,
}


# Mysql 配置信息
# 根据你的环境修改
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'weibo_cxk'     # 数据库名
MYSQL_USER = 'root'         # 数据库用户
MYSQL_PASSWORD = 'ljc123'   # 数据库密码

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
