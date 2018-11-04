from scrapy import cmdline
# import time
cmdline.execute(['scrapy','crawl','ahthor'])
# import urllib.request
# coding:utf-8
# import requests
# from bs4 import BeautifulSoup
# cookie = 'SINAGLOBAL=1786227901938.7551.1522245701948; UM_distinctid=1648e1cc79f0-08d20e8b42b42-5e442e19-100200-1648e1cc7a430d; wvr=6; UOR=,,login.sina.com.cn; wb_view_log_1728342843=1366*7681; YF-V5-G0=3717816620d23c89a2402129ebf80935; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5pqy4OYuF3qJCiIZTq1Ody5JpX5KMhUgL.Fo2Neon0ShzRShe2dJLoI79Awgiueh2t; ALF=1570954600; SSOLoginState=1539418602; SCF=AmfMq9ToEvZYiRRVL89F-tW_xsc9buZltVHStmg3aDAxYh2gDV2jN7k5Rv4k0kJVDwxzZwQQ3IADHSiXvrzfGB0.; SUB=_2A252xdm8DeRhGedJ6VoS9CzEzz-IHXVVs0x0rDV8PUNbmtBeLUuskW9NVipOhWF5samXZICNY1vHvJ1Z_jrU37_e; SUHB=0V5k05zTPOT0o9; YF-Page-G0=f70469e0b5607cacf38b47457e34254f; _s_tentry=login.sina.com.cn; Apache=1921202223499.3142.1539418610934; ULV=1539418611131:65:6:5:1921202223499.3142.1539418610934:1539341004803'
# headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#                                                                             'Accept-Encoding': 'gzip, deflate, br',
#                                                                             'Accept-Language': 'zh-CN,zh;q=0.9',
#                                                                             'Cache-Control': 'max-age=0',
#                                                                             'Connection': 'keep-alive',
#                                                                             'Cookie': cookie,
#                                                                             'Host':'weibo.com',
#                                                                             'Referer': 'https://weibo.com/1728342843/fans?rightmod=1&wvr=6',
#                                                                             'Upgrade-Insecure-Requests': '1',
#                                                                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# urrl = 'https://weibo.com/u/1728342843/home?wvr=5'
# wbdata = requests.get(urrl,headers=headers)
# # requests.get()
# # time.sleep(3)
# # wbdata=wbdata.encoding('gbk','ignore')
# soup = BeautifulSoup(wbdata,'html.parser')
# soup=soup.find_all('script')
# print(soup)
