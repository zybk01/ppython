# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import re
import requests
import urllib




def get_content(keyword):
    contents = []
    for page in range(0, 20):
            picpage=2*page-1
            url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={1}page={2}'.format(keyword,keyword, picpage)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            content = response.read()
            content = content.decode('utf-8')  # python3
            response.close()
            # print content
            lists = re.findall(r'<div class="p-img">.*?</div>', content, re.S)
            for li in lists:
                tem = re.search(r'<img width.*?src|data-lazy-img="(.*?)"', li, re.S)
                src1 = tem.group(1)
                if isinstance(src1, str):
                    src1 = 'http:' + src1
                    contents.append(src1)
    # print contents

    # jsoncontent = json.dumps(contents, ensure_ascii=False, encoding='utf-8')
    return contents


# 用图片url下载图片并保存成制定文件名
def downloadJPG(imgUrl, fileName):
    urllib.request.urlretrieve(imgUrl, fileName)


# 批量下载图片，默认保存到当前目录下
def batchDownloadJPGs(imgUrls, path='D:/pic/手表/'):  # 图片需要保存的地址
    # 用于给图片命名
    for url in imgUrls:
        print(url)
        name=url.split('/')
        num=len(name)
        picname=name[num-1][:-4]
        downloadJPG(url, path+'{0}.jpg'.format(picname))  # 将多个路径组合


# 封装：从网页下载图片
def download():
    jpgs = get_content('%E6%89%8B%E8%A1%A8')  # 输入关键字，不能是汉字，要去网址复制
    batchDownloadJPGs(jpgs)


def main():
    download()


if __name__ == '__main__':
    main()