# -*- coding: utf-8 -*-
# @Author: lc
# @Date:   2017-09-25 23:54:24
# @Last Modified by:   LC
# @Last Modified time: 2017-09-29 20:59:13


####################################################################################################################
# Download images from google with specified keywords for searching
# search query is created by "main_keyword + supplemented_keyword"
# if there are multiple keywords, each main_keyword will join with each supplemented_keyword
# mainly use urllib, and each search query will download at most 100 images due to page source code limited by google
# allow single process or multiple processes for downloading
####################################################################################################################


import os
import time
import tupianurl
import logging
import urllib.request
import urllib.error
from multiprocessing import Pool

log_file = 'download.log'
logging.basicConfig(level=logging.DEBUG, filename=log_file, filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s  %(message)s")


def download_page(url):
    """download raw content of the page

    Args:
        url (str): url of the page

    Returns:
        raw content of the page
    """
    try:
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
        headers['Referer'] = 'https://www.google.com'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        return str(resp.read())
    except Exception as e:
        print('error while downloading page {0}'.format(url))
        logging.error('error while downloading page {0}'.format(url))
        return None


def parse_page(url):
    """parge the page and get all the links of images, max number is 100 due to limit by google

    Args:
        url (str): url of the page

    Returns:
        A set containing the urls of images
    """
    page_content = download_page(url)
    if page_content:
        link_list = url.findall('"ou":"(.*?)"', page_content)
        if len(link_list) == 0:
            print('get 0 links from page {0}'.format(url))
            logging.info('get 0 links from page {0}'.format(url))
            return set()
        else:
            return set(link_list)
    else:
        return set()


def download_images(main_keyword, supplemented_keywords, download_dir):
    """download images with one main keyword and multiple supplemented keywords

    Args:
        main_keyword (str): main keyword
        supplemented_keywords (list[str]): list of supplemented keywords

    Returns:
        None
    """
    image_links = set()
    print('Process {0} Main keyword: {1}'.format(os.getpid(), main_keyword))

    # create a directory for a main keyword
    img_dir = download_dir + main_keyword + '/'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)


    print('Process {0} supplemented keyword: {1}'.format(os.getpid(), supplemented_keywords[j]))
    search_query = (main_keyword + ' '+ supplemented_keywords).replace(' ', '%20')
    # url = 'https://www.google.com/search?q=' + search_query + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
    url = 'https://www.google.com/search?q=' + search_query + '&source=lnms&tbm=isch'
    image_links = image_links.union(parse_page(url))
    print('Process {0} get {1} links so far'.format(os.getpid(), len(image_links)))
    time.sleep(2)
    print("Process {0} get totally {1} links".format(os.getpid(), len(image_links)))

    print("Start downloading...")
    count = 1
    for link in image_links:
        try:
            req = urllib.request.Request(link, headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'})
            response = urllib.request.urlopen(req)
            data = response.read()
            print(data)
            file_path = img_dir + '{0}.jpg'.format(count)
            with open(file_path, 'wb') as wf:
                wf.write(data)
            print('Process {0} fininsh image {1}/{2}.jpg'.format(os.getpid(), main_keyword, count))
            count += 1
        except urllib.error.URLError as e:
            logging.error('URLError while downloading image {0}\nreason:{1}'.format(link, e.reason))
            continue
        except urllib.error.HTTPError as e:
            logging.error(
                'HTTPError while downloading image {0}\nhttp code {1}, reason:{2}'.format(link, e.code, e.reason))
            continue
        except Exception as e:
            logging.error(
                'Unexpeted error while downloading image {0}\nerror type:{1}, args:{2}'.format(link, type(e), e.args))
            continue

    print("Finish downloading, total {0} errors".format(len(image_links) - count))


if __name__ == '__main__':
    main_keywords = 'infant'

    supplemented_keywords = 'standing'

    download_dir = 'D:\infant standing'

    # download with single process
    # for i in range(len(main_keywords)):
    #     download_images(main_keywords[i], supplemented_keywords, download_dir)

    # download with multiple process
    p = Pool()  # number of process is the number of cores of your CPU
    p.apply_async(download_images, args=(main_keywords, supplemented_keywords, download_dir))
    p.close()
    p.join()
    print('All fininshed')