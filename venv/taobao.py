import json
import requests
from requests.exceptions import RequestException
import re
import urllib
from urllib.request import urlretrieve
from multiprocessing import Pool


def get_one_page(url):
    headers = {
        'cookie':'miid=8960473920965734766; l=ApiYNfTJhgeifK1jDMZMHKRk6MgqgfwL; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=163cf435e16328-00619d13c10a26-5d4e211f-1fa400-163cf435e17255; cna=+CMnEKQScH4CAQo2N8S/N8AJ; wf_tid=00ad3e536ed8; wf_rid=0fd7591f1120; ctoken=aQfkeQzGW-ewhr-jxavwjBjr; v=0; unb=827121410; sg=%E5%8F%B909; t=f42b5df52711693a307601aea5c70ad9; _l_g_=Ug%3D%3D; skt=6451bc939c504445; cookie2=2a552c8e24d907a332abfe9774b59ed0; cookie1=U7KqWCcz%2BwJZTeOu7tcFiCWdaQSfiyA7armIfrF2QK4%3D; csg=53519fd3; uc3=vt3=F8dBzrmSETx5uNQnQpI%3D&id2=W8tzMM9Q5DjP&nk2=pxCGPdU%2BsnM%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTUzMzAzMTM4Mw%3D%3D; tracknick=%5Cu5462%5Cu5583%5Cu548F%5Cu53F9; lgc=%5Cu5462%5Cu5583%5Cu548F%5Cu53F9; _cc_=WqG3DMC9EA%3D%3D; dnk=%5Cu5462%5Cu5583%5Cu548F%5Cu53F9; _nk_=%5Cu5462%5Cu5583%5Cu548F%5Cu53F9; cookie17=W8tzMM9Q5DjP; tg=0; mt=ci=9_1; _tb_token_=5504de37be8ed; uc1=cookie14=UoTfKLaeadH0qA%3D%3D&lng=zh_CN&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie21=U%2BGCWk%2F7pY%2FF&tag=8&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261533034533010; isg=BP__gJr4mFYdEp2V7xIdnNZJjtNJTFFNj39EhZHOqq72oB8imbTj1n265jD7wSv-',
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
    pattern = re.compile('<img data-ks-lazyload="(//g.search.alicdn.com/img.*?.jpg).*?.jpg".*?src="(.*?)">', re.S)
    items = re.findall(pattern, html)
    file_path = "D:/pic/耳骨/"
    for item in items:
        print(item[0])
        try:
            name1=item[0].split('/')
            num=len(name1)
            name=name1[num-1][:-4]
            print(name)
            itemurl='http:'+item[0]
            print(itemurl)
            urllib.request.urlretrieve(itemurl,file_path +'{}.jpg'.format(name))
            #urllib.request.urlretrieve(item[1], file_path + '/{}.jpg'.format(item[0]))
        except:
            print('erro')
            continue

def write_to_file(content):
    with open('istock.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main (offset):
    #url = 'http://maoyan.com/board/4?offset=' + str(offset)
    keyword='耳骨配饰'
    url = 'http://uland.taobao.com/sem/tbsearch?keyword='+str(keyword)+ '&page='+str(offset)
    html = get_one_page(url)
    parse_one_page(html)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main, [i for i in range(100)])

     #for i in range(100):
        #main(i)