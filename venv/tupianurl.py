


import os
import shutil
import operator

def name_replace():
  out_path='D:/pic/' #图片移动的文件夹
  f = open('D:/pic/试用.txt', 'r') #txt文档路径
  lines = f.readlines()  # 读取全部内容
  for line in lines:
    print(line)
    rootdir_all = 'D:/pic/试用/'  # 总文件夹
    rootdirs= os.listdir(rootdir_all) #子文件夹
    for rootdir in rootdirs:
      rootdir=os.path.join(rootdir_all,rootdir)
      print(rootdir)
      pic_names=os.listdir(rootdir)
      for pic_name in pic_names:
          try:
            if operator.eq(pic_name,line[:-1]):
              shutil.move(os.path.join(rootdir,pic_name),os.path.join(out_path,pic_name))
              print('找到相应图片：',pic_name)
            else:
              continue
          except:
            continue


if __name__ == '__main__':
  name_replace()

'''
import os
import shutil
import operator

def name_replace():
  out_path='D:/pic/' #图片移动的文件夹
  f = open('D:/pic/试用.txt', 'r') #txt文档路径
  lines = f.readlines()  # 读取全部内容
  for line in lines:
    print(line)
    rootdir_all = 'D:/pic/试用/'  # 文件夹
    pic_names= os.listdir(rootdir_all) #图片文件

    for pic_name in pic_names:
        try:
          if operator.eq(pic_name[:-4],line[:-5]):
            shutil.move(os.path.join(rootdir_all,pic_name),os.path.join(out_path,pic_name))
            print('找到相应图片：',pic_name)
          else:
            continue
        except:
          continue


if __name__ == '__main__':
  name_replace()
'''