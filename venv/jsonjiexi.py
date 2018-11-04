# -*- coding:utf-8 -*-
import json
import os

rootdir = 'D:/pic/json/'  #json文件夹地址
lists= os.listdir(rootdir)
print(len(lists))
txtpath='D:/pic/data.txt'#输出数据txt文件的地址
x=0
for list in lists:
    print(x)
    x+=1
    with open(rootdir+list,encoding='utf-8') as f:
      temp = json.load(f)
      print(list)
      for j in range(0,len(temp['animal_boundingbox_landmark_list'])):
          #print(j)
          id = temp["image_id"]
          #f.writelines('image_id:' + str(id) + '\n')
          topx = temp['animal_boundingbox_landmark_list'][j]['bbox']['left'][0]
          topy = temp['animal_boundingbox_landmark_list'][j]['bbox']['left'][1]
          rightx = temp['animal_boundingbox_landmark_list'][j]['bbox']['top'][0]
          righty=temp['animal_boundingbox_landmark_list'][j]['bbox']['top'][1]
          bottomx = temp['animal_boundingbox_landmark_list'][j]['bbox']['right'][0]
          bottomy = temp['animal_boundingbox_landmark_list'][j]['bbox']['right'][1]
          leftx = temp['animal_boundingbox_landmark_list'][j]['bbox']['bottom'][0]
          lefty = temp['animal_boundingbox_landmark_list'][j]['bbox']['bottom'][1]
          pointx=min(bottomx,topx,rightx,leftx)
          pointy=min(bottomy,topy,righty,lefty)
          maxy=max(bottomy,topy,righty,lefty)
          maxx=max(bottomx,topx,rightx,leftx)
          w=maxx-pointx
          h=maxx-pointy
          idtemp=temp['animal_boundingbox_landmark_list'][j]['image_boundingbox_attributes']
          try:
              id=idtemp[0]["category_id"]

              if int(id) == 71:
                  g= open(txtpath, 'a',encoding='utf-8')
                  g.writelines(list[:-5]+'.jpg'+' adult '+str(pointx)+' '+str(pointy)+' '+str(w)+' '+str(h)+'\n')
              elif int(id) == 0:
                  g = open(txtpath, 'a', encoding='utf-8')  # 输出数据txt文件的地址
                  g.writelines(list[:-5]+'.jpg'+ ' unknown ' + str(pointx) + ' ' + str(pointy) + ' ' + str(w) + ' ' + str(h) + '\n')
              elif int(id) == 1:
                  g = open(txtpath, 'a', encoding='utf-8')  # 输出数据txt文件的地址
                  g.writelines(list[:-5]+'.jpg' + ' dog ' + str(pointx) + ' ' + str(pointy) + ' ' + str(w) + ' ' + str(h) + '\n')
              elif int(id) == 2:
                  g = open(txtpath, 'a', encoding='utf-8')  # 输出数据txt文件的地址
                  g.writelines(list[:-5]+'.jpg' + ' cat ' + str(pointx) + ' ' + str(pointy) + ' ' + str(w) + ' ' + str(h) + '\n')
              elif int(id) == 55:
                  g = open(txtpath, 'a', encoding='utf-8')  # 输出数据txt文件的地址
                  g.writelines(list[:-5]+'.jpg' + ' otheranimal ' + str(pointx) + ' ' + str(pointy) + ' ' + str(w) + ' ' + str(h) + '\n')
              elif int(id) == 70:
                  g = open(txtpath, 'a', encoding='utf-8')  # 输出数据txt文件的地址
                  g.writelines(list[:-5]+'.jpg' + ' baby ' + str(pointx) + ' ' + str(pointy) + ' ' + str(w) + ' ' + str(h) + '\n')
              else:
                  print('此条分类失败')
                  continue
          except:
              print(list+"此文档有问题")
              continue
