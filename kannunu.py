
import os
import re
import urllib.request
import threading
# coding: utf-8


common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                            '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key] = common_used_numerals_tmp[key]


def chinese2digits(uchars_chinese):
    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
                # total =total + r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total


num_str_start_symbol = ['一', '二', '两', '三', '四', '五', '六', '七', '八', '九',
                        '十']
more_num_str_symbol = ['零', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿']


def changeChineseNumToArab(oriStr):
    lenStr = len(oriStr);
    aProStr = ''
    if lenStr == 0:
        return aProStr;

    hasNumStart = False;
    numberStr = ''
    for idx in range(lenStr):
        if oriStr[idx] in num_str_start_symbol:
            if not hasNumStart:
                hasNumStart = True;

            numberStr += oriStr[idx]
        else:
            if hasNumStart:
                if oriStr[idx] in more_num_str_symbol:
                    numberStr += oriStr[idx]
                    continue
                else:
                    numResult = str(chinese2digits(numberStr))
                    numberStr = ''
                    hasNumStart = False;
                    aProStr += numResult

            aProStr += oriStr[idx]
            pass

    if len(numberStr) > 0:
        resultNum = chinese2digits(numberStr)
        aProStr += str(resultNum)

    return aProStr


testStr = ['两百三十二', '我有两百三十二块钱', '十二个套餐', '一亿零八万零三百二十三', '今天天气真不错',
           '百分之八十 discount rate很高了', '千万不要',
           '这个invoice value值一百万',
           '我的一百件商品have quality',
           '找一找我的收藏夹里，有没有一个眼镜', ]

# for tstr in testStr:
    # print(tstr + ' = ' + changeChineseNumToArab(tstr))

# 定义一个爬取网络小说的函数
def atoi(s):
 s = s[::-1]
 num = 0
 for i, v in enumerate(s):
  for j in range(0, 10):
   if v == str(j):
      num += j * (10 ** i)
 return num
# html = urllib.request.urlopen("http://www.quanshuwang.com/book/44/44683").read()
# urrl="http://www.kanunu8.com/files/yuanchuang/201106/3172.html"
# urrl="http://www.kanunu8.com/book3/6565/index.html"
urrl = input("Please intput your url:")
html = urllib.request.urlopen(urrl).read()
html = html.decode("gbk")  # 转成该网址的格式
# html=re.findall(r'<table width="1050" height="2" (.*?)',html)
    # <li><a href="http://www.quanshuwang.com/book/44/44683/15379609.html" title="引子 穿越的唐家三少，共2744字">引子 穿越的唐家三少</a></li>  #参考
#       <td width="25%"><a href="3172/82937.html">第一节 《小云雨诀》</a></td>
reg2 = r'<td><a href="(.*?)/(.*?)">(.*?)</a></td>'  # 正则表达的匹配
# reg = re.compile(reg)  # 可添加可不添加，增加效率
reg= r'<td width="25%"><a href="(.*?)/(.*?)">(.*?)</a></td>'
bookname = re.findall(r'<title>(.*?) - 小说在线阅读 - 努努书坊</title>', html)
# bookname = re.findall(r'<h2><b>(.*?)</b></h2></Td>', html)
# if len(bookname) == 0:
#     bookname= re.findall(r'<h1><strong><font color="#dc143c">(.*?)</font></strong></h1></td>', html)
# if len(bookname) == 0:
#     bookname = re.findall(r'<strong><font color="#dc143c" size="4"> (.*?)</font><strong></td>', html)
urls = re.findall(reg, html)
urlss=re.findall(reg2,html)
sigg=0
nsigg=0
preurl=re.findall(r'(.*?).html',urrl)
if (len(urls)==0)&(len(urlss)==0):
    reg2=r'<td><a href="(.*?)">(.*?)</a></td>'
    reg = r'<td width="25%"><a href="(.*?)">(.*?)</a></td>'
    sigg=1
    preurl = re.findall(r'(.*?)/index.html', urrl)
    urls = re.findall(reg, html)
    urlss = re.findall(reg2, html)
if (len(urls)==0)&(len(urlss)==0):
    reg=r'<td width="33%"><a target="_blank" href="(.*?)">(.*?)</a></td>'
    reg2 = r'<td><a target="_blank" href="(.*?)">(.*?)</a></td>'
    sigg=1
    nsigg=1
    preurl=[]
    preurl.append("http://www.kanunu8.com")
    urls = re.findall(reg, html)
    urlss = re.findall(reg2, html)
m=re.findall(r'.ht(.*?)l',urrl)
if len(m)==0:
    preurl = []
    preurl.append(urrl[0:len(urrl)-1])

for i in urlss:
    urls.append(i)
numm=[]
def getNovelContent(chapter_url,chapter_title,nuum):

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

        chapter_title=nuum[0]
        numm.append(atoi(nuum[0]))
        # print(url)
        # chapter_url = url[0]  # 章节的超链接
        # chapter_title = url[1]  # 章节的名字
        # print(chapter_title)
        chapter_html = urllib.request.urlopen(chapter_url).read()  # 正文内容源代码
        chapter_html = chapter_html.decode("gbk","ignore")
        chapter_html=str(chapter_html)
        chapter_reg = r'<p>.*?</p>'
        chapter_reg = re.compile(chapter_reg, re.S)
        chapter_content = re.findall(chapter_reg, chapter_html)
        for content in chapter_content:
            content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "     ")
            content = content.replace("<br />", "")
            content = content.replace("&quot;", "")
            content = content.replace('\r\n\r\n', "\n\n")
            # print(content)
            f = open('{}.txt'.format(chapter_title), 'w+')
            f.write(title)
            f.write(content)
            f.close()
threads = []
length=len(urls)
i = 0  # ##这个是演示多线程爬取
for url in urls:
        # 开了100线程，这样开100线程去爬100页面的详情页面，因为fang.com只能看100页
        if sigg==0:
            chapter_url = url[1]  # 章节的超链接
            chapter_title = url[2]  # 章节的名字
        else:
            chapter_url = url[0]  # 章节的超链接
            chapter_title = url[1]  # 章节的名字
        if nsigg==0:
            nuum = re.findall(r'([0-9]+).html',chapter_url)
        else:
            nuum = re.findall(r'/([0-9]+).html', chapter_url)
        chapter_url = preurl[0] + "/" + chapter_url
        # print(url)
        t = threading.Thread(target=getNovelContent, args=(chapter_url,chapter_title,nuum,))
        i = i+1
        threads.append(t)

        if (i == 100) | (url == urls[length-1]):
           i=0
           for t in threads:
               t.start()
           # t1=time.time()
           for t in threads:
               t.join()
           print("shiteater")
           threads=[]
f = open('{}.txt'.format(bookname[0]), 'a')
numm.sort()
for j in numm:
    str1=".txt"
    name=(str(j)+str1)
    try:
        fa=open(name)
    except FileNotFoundError as e:
        print(e)
    # fa = open('{}.txt'.format("i"), 'w')
    else:
        contenta=fa.read()
        f.write('\n\n')
        f.write(contenta)
        fa.close()
        os.remove(name)
# getNovelContent()
print("over")