#! -*- encoding:utf-8 -*-

import requests
import time
import json
from lxml import etree
from selenium import webdriver
import os
from bs4 import BeautifulSoup

proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

proxyUser = "HV6P1A2H183B4GXD"
proxyPass = "94B919D71ED54D05"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

# api_url = r"https://www.xiaohongshu.com/web_api/sns/v3/search/note?keyword=baby&page=1&page_size=20"

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

# if don't add this; proxy can't craw data
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",}
image_headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    'referer': 'https://www.xiaohongshu.com/search_result/%E5%86%BB%E5%B9%B2%E7%B2%89',
      "Host": "www.xiaohongshu.com",
    # "Connection": "keep-alive",
    "cookie": "HMACCOUNT=322E9093F9FDEA5C; BIDUPSID=C251C4B5EE01CDC2A4A90A1C53196A22; PSTM=1490691911; __cfduid=d148ef209d08d926617699182c6c166451518325663; BAIDUID=D5958F52925FC41297F1D3A2E14EB04F:FG=1; BDUSS=JST05RRUtLc0ZvOHNVTGpNbnp2REozbVRUTDlGVXplSlJ1Y2h-WERJZGlXR3BiQVFBQUFBJCQAAAAAAAAAAAEAAAAtwI0YxNjgq9O9zL4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGLLQltiy0JbWj; PSINO=7; H_PS_PSSID=26939_1435_21088_18560_22157; BDSFRCVID=ooPsJeCCxG3AX1O7j2zCe71FklZUbK1_B4q23J; H_BDCLCKID_SF=JJIfoDL2tCvbfP0k2-rHhPkehxJeanLXKKOLVb7OLPOkeqOJ2Mt5LqvLXNJBJJTm5RkDKJvsyf5DOIj3L6OaD6tpexbH55uOJbut3J; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; HMVT=d0ae755ac51e3c5ff9b1596b0c09c826|1533289961|",
    "accept": "application/json, text/plain, */*",
}

# for i in range(50):
#     resp4 = requests.get(api_url, headers=headers,proxies=proxies)
#     resp3 = requests.get(ip_url, proxies=proxies).text
#     print(resp3)
#     print(resp4.text)

def craw(key_word, start_page, page_count):
    for page in range(start_page, page_count):
        api_url = "https://www.xiaohongshu.com/web_api/sns/v3/search/note?keyword=%s&page=%s&page_size=20" % (key_word, page+1)
        print(api_url)
        response = requests.get(api_url, headers=headers, proxies=proxies)
        print(response)
        response = json.loads(response.text)
        data = response['data']['notes']
        for note in data:
            # only image url; we don't need video
            if note['type'] == 'normal':
                id = note['id']
                image_url = 'https://www.xiaohongshu.com/discovery/item/%s' % id
                print("start %s" % image_url)

                browser = webdriver.Chrome()
                try:
                    browser.get(image_url)
                    # 如果10秒内没有加载完成就会报错
                    # selenium.common.exceptions.TimeoutException: Message: timeout: Timed out receiving message from renderer: 1.684
                    browser.set_page_load_timeout(3.5)
                except Exception:
                    browser.close()
                    continue
                time.sleep(1.5)

                # print(api_data)
                try:
                    # this is str of html
                    html = browser.page_source
                    html = etree.HTML(html)
                    script_text = html.xpath('/html/body/script/text()')
                    api_data = json.loads(script_text[0].lstrip('window.__INITIAL_SSR_STATE__='))
                    image_list = api_data['NoteView']['noteInfo']['images']
                except Exception:
                    browser.close()
                    continue

                if image_list != []:
                    for image_index in image_list:
                        image_url = image_index['url'].lstrip('//')
                        all_image_url.append(image_url)
                        with open('./data.txt', 'a+', encoding='utf-8') as f:
                            f.write(image_url + '\n')
                            f.close()

                # bsObj = BeautifulSoup(html, "html.parser")

                # response_html = requests.get(image_url, headers=image_headers, proxies=proxies)
                # html = etree.HTML(response_html.content.decode())
                # script_text = html.xpath('/html/body/script/text()')
                # # this is data including in script of html; we find it, then get the url of image
                # api_data = json.loads(script_text[0].lstrip('window.__INITIAL_SSR_STATE__='))
                print("end %s" % image_url)
                browser.close()


if __name__ == '__main__':
    all_image_url = []
    # key_world = str('???')
    # crawl(key_world)
    print("Running tests...")
    page_count = 50
    start = 0
    craw("毛衣链", start, page_count)
    print('Finish!!')