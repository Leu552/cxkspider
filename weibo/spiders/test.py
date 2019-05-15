import urllib3
import requests
import json
import random
import time
from fake_useragent import UserAgent

ua = UserAgent()

def get_data():

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    ]

    UserAgent = random.choice(user_agent_list)

    headers = {
        'Host': 'weibo.com',
        'User-Agent': ua.random,
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'SINAGLOBAL=1505092439785.638.1548912484608; TC-Page-G0=841d8e04c4761f733a87c822f72195f3; _s_tentry=passport.weibo.com; Apache=9246181159618.564.1550212893574; ULV=1550212893586:2:1:1:9246181159618.564.1550212893574:1548912484630; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=5e86081f15aa42603185fffc3db712f7; cross_origin_proto=SSL; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; UM_distinctid=16a1f4014e30-034888a184b62e-58422116-1fa400-16a1f4014e673; un=2978610085@qq.com; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=edef3632d17f5fb3; SSOLoginState=1555324904; YF-Ugrow-SEO-G0=8e667ee9394bfc84054b8fa626d4b0dc; wb_view_log_5681855938=1920*10801; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnaHFwnfa9b6Bn0eVW_jaD5JpX5K2hUgL.Fo-c1h2RSK-4e0n2dJLoI7UhdNiVwHvk; ALF=1586947400; SCF=ApA3TwJO8OkekAZzIkq-v9EJJ7s2OBvMB3YOUA8HJDkRLpQMp7ZAeE6MawHuVMB4HGeoAmRtJq1e3l5otJBkOh0.; SUB=_2A25xscGcDeThGeNI41MZ9SvFyDSIHXVSxrRUrDV8PUNbmtBeLRPTkW9NSD4SFVOkcS02xhwpzupcOpYGDcWIafuA; SUHB=05iqxFrjc87bAc; wvr=6; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74|1555412761|1555412757; webim_unReadCount=%7B%22time%22%3A1555412766585%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D'
    }
    for i in range(1,3):
        headers = {
            'Host': 'weibo.com',
            'User-Agent': ua.random,
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'SINAGLOBAL=1505092439785.638.1548912484608; TC-Page-G0=841d8e04c4761f733a87c822f72195f3; _s_tentry=passport.weibo.com; Apache=9246181159618.564.1550212893574; ULV=1550212893586:2:1:1:9246181159618.564.1550212893574:1548912484630; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=5e86081f15aa42603185fffc3db712f7; cross_origin_proto=SSL; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; UM_distinctid=16a1f4014e30-034888a184b62e-58422116-1fa400-16a1f4014e673; un=2978610085@qq.com; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=edef3632d17f5fb3; SSOLoginState=1555324904; YF-Ugrow-SEO-G0=8e667ee9394bfc84054b8fa626d4b0dc; wb_view_log_5681855938=1920*10801; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnaHFwnfa9b6Bn0eVW_jaD5JpX5K2hUgL.Fo-c1h2RSK-4e0n2dJLoI7UhdNiVwHvk; ALF=1586947400; SCF=ApA3TwJO8OkekAZzIkq-v9EJJ7s2OBvMB3YOUA8HJDkRLpQMp7ZAeE6MawHuVMB4HGeoAmRtJq1e3l5otJBkOh0.; SUB=_2A25xscGcDeThGeNI41MZ9SvFyDSIHXVSxrRUrDV8PUNbmtBeLRPTkW9NSD4SFVOkcS02xhwpzupcOpYGDcWIafuA; SUHB=05iqxFrjc87bAc; wvr=6; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74|1555412761|1555412757; webim_unReadCount=%7B%22time%22%3A1555412766585%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D'
        }
        url = 'https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id=4361379747512186&max_id=4361779607852473&page='+str(i)+'&__rnd='+str(int(time.time()))
        print(url)
        print(headers['User-Agent'])
        res = requests.get(url=url, headers=headers)
        print(res.json())
        print(res.status_code)
        # print(res.json()['data']['html'])


# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = "SINAGLOBAL=1505092439785.638.1548912484608; TC-Page-G0=841d8e04c4761f733a87c822f72195f3; _s_tentry=passport.weibo.com; Apache=9246181159618.564.1550212893574; ULV=1550212893586:2:1:1:9246181159618.564.1550212893574:1548912484630; Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=5e86081f15aa42603185fffc3db712f7; cross_origin_proto=SSL; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=82f55bdb504a04aef59e3e99f6aad4ca; UM_distinctid=16a1f4014e30-034888a184b62e-58422116-1fa400-16a1f4014e673; un=2978610085@qq.com; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=edef3632d17f5fb3; SSOLoginState=1555324904; YF-Ugrow-SEO-G0=8e667ee9394bfc84054b8fa626d4b0dc; wb_view_log_5681855938=1920*10801; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhnaHFwnfa9b6Bn0eVW_jaD5JpX5K2hUgL.Fo-c1h2RSK-4e0n2dJLoI7UhdNiVwHvk; ALF=1586947400; SCF=ApA3TwJO8OkekAZzIkq-v9EJJ7s2OBvMB3YOUA8HJDkRLpQMp7ZAeE6MawHuVMB4HGeoAmRtJq1e3l5otJBkOh0.; SUB=_2A25xscGcDeThGeNI41MZ9SvFyDSIHXVSxrRUrDV8PUNbmtBeLRPTkW9NSD4SFVOkcS02xhwpzupcOpYGDcWIafuA; SUHB=05iqxFrjc87bAc; wvr=6; YF-Page-G0=ee5462a7ca7a278058fd1807a910bc74|1555412761|1555412757; webim_unReadCount=%7B%22time%22%3A1555412766585%2C%22dm_pub_total%22%3A1%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D"
    trans = transCookie(cookie)
    print(trans.stringToDict())

