# *****************************
# ****** 2018 3.14  ***********
# *****  Author: LQ  **********
# ****** Python 3.6.3 *********
# **** 用于爬取谷歌的图片********
# *****************************

# ****本脚本还是存有一些问题的，没有很好解决google的反爬机制以及google的翻页问题
# *******本脚本运行时需要本机安装 Chrome 浏览器以及Chrome的驱动，同时需要selenium库的支撑********
from selenium import webdriver
import time
import urllib
from bs4 import BeautifulSoup as bs
import re
import os

# ****************************************************
base_url_part1 = 'https://www.hellorf.com/image/search/'
base_url_part2 = '?image_type='  # base_url_part1以及base_url_part2都是固定不变的，无需更改
search_query = '猫吃食'  # 检索的关键词，可自己输入你想检索的关键字
location_driver = 'D:/download/Chrome/Chrome driver/chromedriver.exe'  # Chrome驱动程序在电脑中的位置


class Crawler:
    def __init__(self):
        self.url = base_url_part1 + search_query+base_url_part2

    # 启动Chrome浏览器驱动
    def start_brower(self):
        # 启动火狐浏览器
        driver = webdriver.Firefox()
        # 最大化窗口，因为每一次爬取只能看到视窗内的图片
        driver.maximize_window()
        # 浏览器打开爬取页面
        driver.get(self.url)
        return driver

    def downloadImg(self, driver):
        t = time.localtime(time.time())
        foldername = str(t.__getattribute__("tm_year")) + "-" + str(t.__getattribute__("tm_mon")) + "-" + str(
            t.__getattribute__("tm_mday"))  # 定义文件夹的名字
        picpath = 'D:\pic\低头猫\%s' % (foldername)  # 下载到的本地目录
        if not os.path.exists(picpath):  # 路径不存在时创建一个
            os.makedirs(picpath)
        # 下载图片的本地路径 D:/ImageDownload/~~

        # 记录下载过的图片地址，避免重复下载
        img_url_dic = {}
        # 当鼠标的位置小于最后的鼠标位置时,循环执行
        js = "var q=document.documentElement.scrollTop=10000"
        print('1')
        driver.execute_script(js)
        print('2')
        time.sleep(2)
        # 获取页面源码
        html_page = driver.page_source
        # 利用正则
        pattern= re.compile('<img.*?class.*?data-original="(https://.*?.jpg)".*?alt="(.*?)">', re.S)
        imglist= re.findall(pattern, html_page)


            # ??这段代码问题?
        for imgurl in imglist:
            yield {
                'img-title': imgurl[1],
                'img-src': imgurl[0]
            }
            try:
                target = picpath + '\\%s.jpg' % imgurl[1]
                urllib.request.urlretrieve(imgurl[0], target)
                time.sleep(1)
            except:
                continue

    def run(self):
        print('''      ************************************* 
        **      Welcome to use Spider      ** 
        *************************************''')

        driver = self.start_brower()
        self.downloadImg(driver)
        driver.close()
        print("Download has finished.")


if __name__ == '__main__':
    craw = Crawler()
    craw.run()




