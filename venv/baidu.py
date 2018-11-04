import requests
import os

def getManyPages(keyword,pages):
    params=[]
    for i in range(10,10*pages+10,10):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        url=requests.get(url,params=i)
        url=url.json()
        url=url.get('data')
        urls.append(url)

    return urls


def getImg(dataList, localPath):

    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    x = 0
    for list in dataList:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                na=i.get('thumbURL')
                name=na.split('/')
                num=len(name)
                open(localPath + '%s' % name[num-1], 'wb').write(ir.content)

            else:
                print('图片链接不存在')

if __name__ == '__main__':
    dataList = getManyPages('李白',30)  # 参数1:关键字，参数2:要下载的页数
    getImg(dataList, 'C:/Users/zy113/Pictures/Saved Pictures')  # 参数2:指定保存的路径