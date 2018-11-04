from multiprocessing import Pool
import json
import requests
from requests.exceptions import RequestException
import re
import urllib
from urllib.request import urlretrieve


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
    #                    + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
    #                   + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    pattern = re.compile('<img.*?src="(http://img.*?.jpg)".*?alt="(.*?)".*?>', re.S)
    items = re.findall(pattern, html)
    file_path = "D:\pic\pic"
    for item in items:
        yield {
            'img-src':item[0],
            'img-title':item[1],
        }
        print(item)
        urllib.request.urlretrieve(item[0],file_path +'/{}.jpg'.format(item[1]))

def write_to_file(content):
    with open('babystanding.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main (offset):
    #url = 'http://maoyan.com/board/4?offset=' + str(offset)
    url = 'http://www.1tu.com/search/?category=7&k=%E4%BE%A7%E8%84%B8%E5%B0%8F%E7%8C%AB&pflag=2&skey=&page='+ str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':

     for i in range(4):
        main(offset = i)
