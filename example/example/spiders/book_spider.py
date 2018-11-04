#-*coding:utf-8-*-
import scrapy
import csv
from scrapy import Item,Field

class bookitem(Item):
    name=Field()
    price=Field()


class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls ='http://books.toscrape.com/'
    def start_requests(self):
        yield scrapy.Request(self.start_urls,callback=self.parse,headers={'User-Agent':'Mozilla/5.0'},dont_filter=True)
    def parse(self, response):
        for sel in response.css('article.product_pod'):
            book=bookitem()
            book['name'] = sel.xpath('./h3/a/@title').extract_first()
            book['price'] = sel.css('p.price_color::text').extract_first()
            yield book
        next_url=response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_url:
            next_url=response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)