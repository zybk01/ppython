import os
import MTLabFace
import cv2
import shutil


def test_fd():
    rootdir = '/peishi1/peishi1/downloadData/560202126464'
    lists = os.listdir(rootdir)
    for list in lists:
        pic_path=os.path.join(rootdir,list)
        image = cv2.imread(pic_path)
        config = MTLabFace.MTFaceConfig()
        config.MeituCrop = True
        config.EXTERN_LEFT = 0.4
        config.EXTERN_RIGHT = 0.4
        config.EXTERN_BOTTOM = 0.2
        config.EXTERN_UP = 0.6
        config.CROP_SIZE_H = 100
        config.CROP_SIZE_W = 100
        result = MTLabFace.FaceFeatureDetect(image, config)
        try:
            if len(result) == 0:
                shutil.move(pic_path,os.path.join('data_team_2018/peishi1/',list))    #data_team_2018/peishi1/替换成你想保存到的文件夹
        except:
            continue

test_fd()





