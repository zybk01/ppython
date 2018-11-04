from selenium import webdriver



browsel=webdriver.Chrome()
# cookie = {}
b='_zap=de5676cb-bb4f-4c9d-8d90-25384e635155; d_c0="AFDveLz1bw2PTiYCuGSnVRat68QuCj3QMlY=|1523631801"; __utma=51854390.1821916671.1537006036.1537006036.1537006036.1; __utmz=51854390.1537006036.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; __utmv=51854390.100-1|2=registration_date=20151015=1^3=entry_date=20151015=1; z_c0="2|1:0|10:1538129429|4:z_c0|92:Mi4xRmZNd0FnQUFBQUFBVU85NHZQVnZEU1lBQUFCZ0FsVk5GVXliWEFDa3hqTVVVdUpuXzczc052ZDk5cFp4cGY2cTZn|339c88045f8e346717914ec991d4c4ee2ce39fd4399435ca842d176adf2fb4be"; tst=r; q_c1=bde427046dff441fb24b9a6023bd6430|1539340258000|1522215058000; __gads=ID=df46f6c1ff43e988:T=1539962758:S=ALNI_MapDjQf2Ly-J0Uw5aF6QYJYF_DRfQ; _xsrf=3b924ce1-5ea0-4399-9843-d0468879c758; tgw_l7_route=3072ae0b421aa02514eac064fb2d64b5'
# for line in b.split(';'):
#     key, value = line.split('=', 1)
#     cookie[key] = value
cookies = {}
b = b.split("; ")
for co in b:
    co = co.strip()
    p = co.split('=')
    value = co.replace(p[0]+'=', '').replace('"', '')
    cookies[p[0]]= value

# browsel.get_cookies()
browsel.add_cookie(cookies)
browsel.get('http://www.zhihu.com')
