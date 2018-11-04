from PIL import Image
import os
datapath = r'D:/pic/maozi/maozi/'
filelist =os.listdir(datapath)
for infile in filelist:
    try:
        img=Image.open(datapath+infile)
        img.save('D:/pic/maozi/maozi1/'+infile)
    except:
        continue
