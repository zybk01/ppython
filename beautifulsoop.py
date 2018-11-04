from bs4 import BeautifulSoup
import urllib.request
import threading
import re
import os
import requests
import time
import gzip
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}

nameshit=input("url/name=")
time_start=time.time()
time1 = time.time()
parammm={'searchkey': nameshit.encode('gbk'),'searchtype': 'articlename','searchbuttom.x': '40','searchbuttom.y': '30'}
# url='http://www.quanshuwang.com/modules/article/search.php?searchkey=%C3%A9%C9%BD%BA%F3%D2%E1&sea' \
#     'rchtype=articlename&searchbuttom.x=40&searchbuttom.y=30'
url='http://www.quanshuwang.com/modules/article/search.php'
urlbook= requests.get(url,parammm)
urrl=urlbook.url

url=urllib.request.urlopen(urrl)
content=url.read().decode('gbk','ignore')
url.close()
bs=BeautifulSoup(content,'html.parser')
url=bs.find_all('div',attrs={'class':"detail"})
try:
    url=url[0].find_all('a')
    # url=url[0]['href']
except Exception as e:
    print('找到多个匹配项')
    page=bs.find_all('a',attrs={'class':'last'})[0].text
    for i in page:
        # urrl=re.findall(r'(.*?)page=',urrl)
        urrl=urrl+'&page='+str(i)
        url = urllib.request.urlopen(urrl)
        content = url.read().decode('gbk', 'ignore')
        url.close()
        bs = BeautifulSoup(content, 'html.parser')
        url = bs.find_all('ul', attrs={'class': "seeWell cf"})
        for uu in url:
            uu=uu.find_all('li')
            for uuu in uu:
                url = uuu.find_all('img')[0]
                # url=url['href'][0]
                if url['alt']==nameshit:
                    url = uuu.find_all('a')[0]
                    urrl = url['href']
                    break
else:
    print('找到匹配项')
url=urllib.request.urlopen(urrl)
content=url.read().decode('gbk','ignore')
url.close()
bs=BeautifulSoup(content,'html.parser')
url=bs.find_all('div',attrs={'class':"detail"})
url=url[0].find_all('a')
url=url[0]['href']
html=urllib.request.urlopen(url)
content=html.read().decode('gbk','ignore')
html.close()
bs=BeautifulSoup(content,'html.parser')
bookname=bs.find_all('title')
bookname=bookname[0].text.strip(' - 小说在线阅读 - 努努书坊')
lis=bs.find_all("div",attrs={'class':'clearfix dirconone'})
numm=[]
threads=[]
i=0

def atoi(s):
 s = s[::-1]
 num = 0
 for i, v in enumerate(s):
  for j in range(0, 10):
   if v == str(j):
      num += j * (10 ** i)
 return num
def getNovelContent(chapter_url, chapter_title, nuum):
    # reg = re.compile(reg)  # 可添加可不添加，增加效率
    title = chapter_title
    # chapter_title = changeChineseNumToArab(chapter_title)
    #
    # # reg = r'第(.*?)章'  # 正则表达的匹配
    # # chaptertitle=re.sub("\D", "" , chapter_title)
    # chaptertitle = re.findall(r'[0-9]+', chapter_title)
    # # chapter_title=chapter_title
    # if len(chaptertitle)>0:
    #     chapter_title=chaptertitle[0]
    #     num=atoi(chapter_title)
    #     numm.append(num)

    chapter_title = nuum[0]

    # print(url)
    # chapter_url = url[0]  # 章节的超链接
    # chapter_title = url[1]  # 章节的名字
    # print(chapter_title)
    chapter_html = urllib.request.Request(chapter_url,headers=headers)


    try:
        chapter_html = urllib.request.urlopen(chapter_html).read()  # 正文内容源代码
    except Exception as e:
        chapter_html = e.partial

    chapter_html = chapter_html.decode("gbk", "ignore")
    chapter_html =BeautifulSoup(chapter_html,'html.parser')
    # chapter_reg = r'<p>.*?</p>'
    # chapter_reg = re.compile(chapter_reg, re.S)
    # chapter_content = re.findall(chapter_reg, chapter_html)
    chapter_content=chapter_html.find_all('div',attrs={'id':'content'})
    if chapter_content:
        numm.append(atoi(nuum[0]))
    for content in chapter_content:

        content=content.text
        content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "     ")
        content = content.replace("<br />", "")
        content = content.replace("&quot;", "")
        content = content.replace('\r\n\r\n', "\n\n")
        # print(content)
        f = open('{}.txt'.format(chapter_title), 'w+',encoding='utf-8')
        f.write(title)
        f.write('\n')
        f.write(content)
        f.close()
if lis:
    k=lis[0].find_all('a')
    for a in k:
        # print(n.text.strip(),n['href'])
        suburl=a['href']
        nuum=re.findall(r'([0-9]+).html',a['href'])
        t = threading.Thread(target=getNovelContent, args=(suburl, a.text.strip(), nuum,))
        i = i + 1
        threads.append(t)
        if (i == 500)or(a == k[len(k) - 1]):
            i = 0
            for t in threads:
                t.start()
            # t1=time.time()
            for t in threads:
                t.join()
            # time.sleep(1)
            time2 = time.time()
            print('totally cost', time2 - time1)
            time1 = time.time()

            threads = []
print(len(numm))
print("shiteater")
time_end=time.time()
print('totally cost',time_end-time_start)
        # contenta=n.find_all('p')
        # f = open('{}.txt'.format(n.text.strip()), 'w')
        # f.write(title)
        # f.write(content)
        # f.close()
f = open('{}.txt'.format(bookname), 'a',encoding='utf-8')
numm.sort()
for j in numm:
    str1=".txt"
    name=(str(j)+str1)
    try:
        fa=open(name,encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
    # fa = open('{}.txt'.format("i"), 'w')
    else:
        contenta=fa.read()
        f.write('\n\n\n\n')
        f.write(contenta)
        fa.close()
        os.remove(name)

