from multiprocessing import Pool
import json
import requests
from requests.exceptions import RequestException
import re
import urllib
from urllib.request import urlretrieve


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
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
    pattern = re.compile('<img.*?alt="(.*?)".*?src="(https.*?.jpg)".*?>', re.S)
    items = re.findall(pattern, html)
    file_path = "D:/Python学习"
    for item in items:
        yield {
            'img-title':item[0],
            'img-src':item[1],
        }
        print(item)
        urllib.request.urlretrieve(item[1],file_path +'/{}.jpg'.format(item[0]))

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main (offset):
    #url = 'http://maoyan.com/board/4?offset=' + str(offset)
    url = 'https://movie.douban.com/top250?start='+ str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':

     for i in range(10):
        main(offset = i * 25)
    #pool = Pool()
    #pool.map(main, [i * 25 for i in range(10)])
