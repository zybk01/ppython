#爬取flickr网页点赞数超过50的图片
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 09:01:48 2018

@author: as
"""

import tupianurl
import json
import os
from lxml import etree
import requests
from urllib import parse
import time
import random
from hashlib import md5
import urllib.request
from http import cookiejar
import urllib.response
import json
import flickrapi

api_key = u'b4638d6e784ce43472a556b0e9d832af'
api_secret = u'a9448ab32d39c296'

keyward='hdr'
num=20000
path='D:\pythonwork\zxyflickr\pic'


if not (os.path.exists(path)):
    os.makedirs(path)

import flickrapi

flickr=flickrapi.FlickrAPI(api_key,api_secret,cache=True)



def flickr_walk(keyward,path,mode,num):
    if not(os.path.exists(path+keyward+'/'+mode)):
        os.makedirs(path+keyward+'/'+mode)
    count = 0
    photos = flickr.walk(text=keyward,
                 extras='url_'+mode,
                 per_page=4000)
    count=0
    for photo in photos:
        count+=1
        if (count>=num):
            break
        try:
            url=photo.get('url_'+mode)
            id1=photo.get('id')
            owner=photo.get('owner')
            file_name=id1+'_'+owner
            faves = flickr.photos_getFavorites(photo_id=id1)
            countfaves = faves.find('photo').get('total')
            comments = flickr.photos_comments_getList(photo_id=id1)
            countcomments = len(comments.findall('.//comment'))
            if int(countfaves)+int(countcomments) > 50:
                print(url)
                urllib.request.urlretrieve(url,path+keyward+'/'+mode+'/'+file_name+'_'+mode+".jpg")
            else:
                print("pass")
        except Exception as e:
            print('failed to download image')

#headers = {
#    "Origin": " https://www.instagram.com/",
#    "Referer": " https://www.instagram.com/morisakitomomi/",
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                  "Chrome/58.0.3029.110 Safari/537.36",
#    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#    "accept-encoding": "gzip, deflate, sdch, br",
#    "accept-language": "zh-CN,zh;q=0.8",
#    "X-Instragram-AJAX": "1",
#    "X-Requested-With": "XMLHttpRequest",
#    "Upgrade-Insecure-Requests": "1",
#}

# def save_image_links(links):
#     with open('images.txt', 'w') as f:
#         for link in links:
#             f.write(link + '\n')
#     print('共保存了' + str(len(links)) + '张图片。')


# def save_video_links(links):
#     with open('videos.txt', 'w') as f:
#         for link in links:
#             f.write(link + '\n')
#     print('共保存了' + str(len(links)) + '个视频。')
#mode_list=['s','q','t','m','n','z','c','b','h','k','o','-']
mode_list=['z']
for mode in mode_list:
    flickr_walk(keyward,path,mode,num)

