import json
import requests
from requests.exceptions import RequestException
import re
import urllib
from urllib.request import urlretrieve
from multiprocessing import Pool


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
    pattern = re.compile('<img.*?alt="(.*?)".*?src="(https://media.istockphoto.com/.*?=)".*?>', re.S)
    items = re.findall(pattern, html)
    file_path = "D:/pic/smartbracelet/"
    for item in items:
        yield {
            'img-src':item[1],
            'img-title':item[0],
        }
        print(item)
        try:
            name1 = item[1].split(';')
            num = len(name1)
            name=name1[num - 1][:-1]
            urllib.request.urlretrieve(item[1],file_path +'/{}.jpg'.format(name))
            #urllib.request.urlretrieve(item[1], file_path + '/{}.jpg'.format(item[0]))
        except:
            print('error')
            continue

def write_to_file(content):
    with open('istock.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main (offset):
    #url = 'http://maoyan.com/board/4?offset=' + str(offset)
    url = 'https://www.istockphoto.com/hk/圖片/smart-bracelet?page='+ str(offset)+'&phrase=smart%20bracelet'
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(23)])

     #for i in range(40):
       # main(offset = i)
