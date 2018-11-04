# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item,Field


class sounditem(Item):
    file_urls = Field()
class SpidersoundSpider(scrapy.Spider):
    name = 'spidersound'
    # allowed_domains = ['''']
    start_urls = 'http://sc.chinaz.com/tag_yinxiao/HaQian.html'


    def start_requests(self):
        yield scrapy.Request(self.start_urls, callback=self.parse, headers={'User-Agent': 'Mozilla/5.0'}, dont_filter=True)
    def parse(self, response):
        for sel in response.css('#musiclist > div > p.z > a::attr(href)'):
            soundurl=sel.extract()
            yield scrapy.Request(soundurl, callback=self.parse)

        for sel1 in response.xpath('//*[@id="downmusic"]/@thumb'):
            sound=sounditem()
            soundurl=[]
            soundurl.append(sel1.extract())
            sound['file_urls']=soundurl
            yield sound
        # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        # if soundurl:
        #     # next_url = response.urljoin(next_url)
        #

