import io
import os
import sys
import urllib
from urllib import parse
from urllib.request import urlretrieve
from requests.exceptions import RequestException
import urllib.request
file_save='D:/pic/'
f = open('D:/pic/sweaterchain.txt', 'r')
lines = f.readlines()#读取全部内容
for line in lines:
    try:
            url=line
            print(url)
            name1=line.split('/')
            num=len(name1)
            print(num)
            file_path = file_save + name1[num-5]+'.jpg'
            print('1')
            #urllib.request.urlretrieve(url, file_path )
            resp = urllib.request.urlopen(url)
            print('2')
            respHtml = resp.read()
            picFile = open(file_path, "wb")
            print('3')
            picFile.write(respHtml)
            picFile.close()

        #urllib.request.urlretrieve(url,file_path +'{}.jpg'.format(line))


    except:
        print('下载失败')
        continue