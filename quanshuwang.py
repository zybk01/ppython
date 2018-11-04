# import socket
# import re
#
# # 创建tcp套接字
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 创建和服务器的连接
# tcp_socket.connect(("www.baidu.com", 80))
#
# # 拼接请求报文
# request_line = "GET / HTTP/1.1\r\n"
# request_header = "Host: www.baidu.com\r\n"
# User_Agent = "User-Agent: Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/59.0\r\n"
# request_data = request_line + request_header + User_Agent + "\r\n"
#
# # 发送请求报文,编码
# tcp_socket.send(request_data.encode())
#
# # 接收响应报文
# recv_data = tcp_socket.recv(4096)
# # 解码
# recv_data = recv_data.decode()
# print(recv_data)
# # 关闭连接
# tcp_socket.close()
#
import time
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
urrl = input("Please intput your url:")
html = urllib.request.urlopen(urrl).read()
html = html.decode("gbk")  # 转成该网址的格式
    # <li><a href="http://www.quanshuwang.com/book/44/44683/15379609.html" title="引子 穿越的唐家三少，共2744字">引子 穿越的唐家三少</a></li>  #参考
reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'  # 正则表达的匹配
reg = re.compile(reg)  # 可添加可不添加，增加效率
bookname1 = re.findall(r'<div class="chapName"><span class="r">(.*?)</span><strong>', html)
bookname = re.findall(r'"article_title">(.*?)</a></div>', html)
bookname[0]=bookname[0]+"-"+bookname1[0]
urls = re.findall(reg, html)
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
        try:
            chapter_html = chapter_html.decode("GBK","ignore")
        except UnicodeDecodeError as e:
            print(e)
            chapter_html = chapter_html.decode("gb18030")
        chapter_html=str(chapter_html)
        chapter_reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;.*?<br />(.*?)<script type="text/javascript">'
        chapter_reg = re.compile(chapter_reg, re.S)
        chapter_content = re.findall(chapter_reg, chapter_html)
        for content in chapter_content:
            content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "      ")
            content = content.replace("<br />", "")
            content = content.replace('\r\n\r\n', "\n\n")
            # print(content)
            f = open('{}.txt'.format(chapter_title), 'w')
            f.write(title)
            f.write(content)
            f.close()
threads = []
i = 0  # ##这个是演示多线程爬取
length=len(urls)
for url in urls:
        # 开了100线程，这样开100线程去爬100页面的详情页面，因为fang.com只能看100页
        chapter_url = url[0]  # 章节的超链接
        chapter_title = url[1]  # 章节的名字
        nuum = re.findall(r'/([0-9]+).html', chapter_url)
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
           # t2=time.time()
           # print("damnshit",t2-t1)
           threads=[]
# print("fuckshit")
f = open('{}.txt'.format(bookname[0]), 'a')
numm.sort()
for j in numm:
    str1=".txt"
    name=(str(j)+str1)
    if j==333:
        print("333")
    try:
        fa = open(name)
    except FileNotFoundError as e:
        print(e)
        # fa = open('{}.txt'.format("i"), 'w')
    else:
        contenta = fa.read()
        f.write('\n\n\n\n')
        f.write(contenta)
        fa.close()
        os.remove(name)
# getNovelContent()
print("over")