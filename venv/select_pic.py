import os
import shutil

def select_picture():
  rootdirfirst= 'D:/pic/图片替换/1/' #文件夹1
  listsfirst = os.listdir(rootdirfirst)

  rootdirsecond = 'D:/pic/图片替换/2/'  # 文件夹2
  listssecond = os.listdir(rootdirsecond)

  rootdirthird = '/peishi1/peishi1/downloadData/560202126464'  # 文件夹3
  liststhird = os.listdir(rootdirthird)

  out_path='D:/pic/pic/'#符合图片保存的文件夹

  #首先判断文件夹2中满足条件的图片
  x=1
  for listsecond in listssecond:
    try:
      if listsecond in listsfirst:
        print(x)
        shutil.move(os.path.join(rootdirsecond,listsecond),os.path.join(out_path,listsecond))
        x+=1
      else:
        continue
    except:
      continue
  #然后判断文件夹3中满足条件的图片
  x=1
  for listthird in liststhird:
    try:
      if listthird in listsfirst:
        print(x)
        shutil.move(os.path.join(rootdirthird,listthird),os.path.join(out_path,listsecond))
        x+=1
      else:
        continue
    except:
      continue


if __name__ == '__main__':
    select_picture()