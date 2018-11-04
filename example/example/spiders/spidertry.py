# -*- coding: utf-8 -*-
import scrapy
import json

class SpidertrySpider(scrapy.Spider):
    name = 'spidertry'
    # allowed_domains = ['zhihu.com']
    start_urls = 'http://www.crup.com.cn/Book/BindCourseList'
    param={'Keywords':'电子技术','Page': '1','Size': '10','PageCount': '','OrderByType': '','IssueDate': '',
           'Classify': '','Parent': '','Qualifications': '1','Series': ''}

    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls, callback=self.parse,headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                                            'Accept-Encoding': 'gzip, deflate',
                                                                            'Accept-Language': 'zh-CN,zh;q=0.9',
                                                                            'Cookie':'Hm_lvt_27ad556c2ff2cdcaf4f5255518c49365=1539505142, 1539505332;ASP.NET_SessionId = 5vr5ca3rsuxcpjvrtnpqbjmb;Hm_lpvt_27ad556c2ff2cdcaf4f5255518c49365 = 1539505576',
                                                                            'Connection': 'keep-alive',
                                                                            'Content-Length':'140',
                                                                            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
                                                                            'Host': 'www.crup.com.cn',
                                                                            'Origin':'http://www.crup.com.cn',
                                                                            'X-Requested-With': 'XMLHttpRequest',
                                                                            'Referer': 'http://www.crup.com.cn/Book/List?keyword=%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF',
                                                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
                             formdata={'Keywords':'电子技术','Page': '1','Size': '10','PageCount': '2','OrderByType': '','IssueDate': '',
                                   'Classify': '','Parent': '','Qualifications': '1.','Series': ''},

                             dont_filter=True)
        # yield scrapy.Request(self.start_urls, callback=self.parse,headers={'Accept': 'application/json, text/javascript, */*; q=0.01',
        #                                                                     'Accept-Encoding': 'gzip, deflate',
        #                                                                     'Accept-Language': 'zh-CN,zh;q=0.9',
        #                                                                     'Cookie':'Hm_lvt_27ad556c2ff2cdcaf4f5255518c49365=1539505142, 1539505332;ASP.NET_SessionId = 5vr5ca3rsuxcpjvrtnpqbjmb;Hm_lpvt_27ad556c2ff2cdcaf4f5255518c49365 = 1539505576',
        #                                                                     'Connection': 'keep-alive',
        #                                                                     'Content-Length':'140',
        #                                                                     'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        #                                                                     'Host': 'www.crup.com.cn',
        #                                                                     'Origin':'http://www.crup.com.cn',
        #                                                                     'X-Requested-With': 'XMLHttpRequest',
        #                                                                     'Referer': 'http://www.crup.com.cn/Book/List?keyword=%E7%94%B5%E5%AD%90%E6%8A%80%E6%9C%AF',
        #                                                                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'},
        #                      meta={'Keywords':'电子技术','Page': '1','Size': '10','PageCount': '2','OrderByType': '','IssueDate': '',
        #                            'Classify': '','Parent': '','Qualifications': '1.','Series': ''},

                             # dont_filter=True)
    def parse(self, response):
        lis=response.text
        lis=json.loads(lis)
        # lis=eval(lis)
        lis=lis['model']
        for listt in lis:
            wblist=listt
            for wbitem in wblist:
                wbtest=wbitem['title']
                yield  wbitem


