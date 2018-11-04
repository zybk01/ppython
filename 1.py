import scrapy
scrapy.version_info
print('shiteater')
from bs4 import BeautifulSoup
import urllib.request
import threading
import re
import os
import json
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
url="https://www.amap.com/search?id=B01C302873&city=230109&geoobj=118.670253%7C31.974002%7C118.974437%7C32.114852&que" \
    "ry_""type=IDQ&query=%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E9%A6%86&zoom=12"
resp=requests.get(url,headers=headers)
print(resp.text)
json_dict=json.loads(resp.text)