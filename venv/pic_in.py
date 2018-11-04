#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import requests
import json
import base64
import cv2
from PIL import Image
import numpy as np
import traceback
import time


def get_statistic(img):
    """
    assume the shape of img array is (height, width).
    """
    from numpy import array
    t = array(img)
    stats = {}
    print(t.shape)
    h, w, c = t.shape
    assert(t.ndim==3)
    for i in range(h):
        for j in range(w):
            elem = tuple(t[i,j])
            n = stats.get(elem, 0)
            stats[elem] = (n+1)
    print("stats:", len(stats))
    return stats


def save_image(path, img):
    data_dir = os.path.dirname(path)
    if not os.path.exists(data_dir):
	    os.makedirs(data_dir)
    cv2.imwrite(path, img)

def walk_dir(root_dir):
    root_dir = root_dir.rstrip("/")
    i = 0
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.jpg'):
                i += 1
                #image_path = os.path.join(root, filename)
                image_path = root_dir+'/'+filename
                print('============',  i, image_path , "=================")
                try:
                    process2(image_path)
                except Exception as e:
                    print("Exception happens:", e)
                    print(traceback.format_exc())
                    time.sleep(2)

# requires utf8 path name
def process2(file_path):
    save_dir = os.path.dirname(file_path)
    save_dir = save_dir.rstrip("/")
    file_name1 = file_path.split('/')
    num = len(file_name1)
    file_name = file_name1[num - 1]
    print("file_name: ", file_name)
    image_name = file_name[:-4]
    #face_mask_path = os.path.join(save_dir, image_name+'_mask.png') #根据图片命名改规则处
    #mix_path = os.path.join(save_dir+'_mix', image_name+'_mix.jpg') #输出覆盖上mask的图不覆盖原图，会重新建一个文件命名为：图片名_mix
    face_mask_path = save_dir+'/'+image_name + '_mask.png'
    mix_path = save_dir + '/'+image_name + '_mix.jpg'
    print(file_path)
    print(face_mask_path)
    print(mix_path)
    face_mix_img = cv2.imread(file_path)
    get_statistic(face_mix_img)
    face_mask_img = cv2.imread(face_mask_path)
    print('origin:', face_mix_img.shape)
    #print('mask:', face_mask_img.shape)
    # merge mask into original image
    alpha = 0.5
    cv2.addWeighted(face_mask_img, alpha, face_mix_img, 1 - alpha, 0, face_mix_img)
    save_image(mix_path, face_mix_img)


# requires utf8 path name
def process(file_path):
    save_dir = os.path.dirname(file_path)
    save_dir = save_dir.rstrip("/")
    file_name1 = file_path.split('/')
    num = len(file_name1)
    file_name = file_name1[num - 1]
    print("file_name: ", file_name)
    image_name = file_name[:-4]
    #face_mask_path = os.path.join(save_dir+'_mask', image_name+'_mask.png')
    face_mask_path = save_dir + '_mask'+ image_name + '_mask.png'
    #mix_path = os.path.join(save_dir+'_mix', image_name+'_mix.jpg')
    mix_path = save_dir + '_mix'+ image_name + '_mix.jpg'
    print(file_path)
    print(face_mask_path)
    print(mix_path)
    face_mix_img = cv2.imread(file_path)
    face_mask_img = cv2.imread(face_mask_path)
    get_statistic(face_mix_img)
    # merge mask into original image
    alpha = 0.5
    cv2.addWeighted(face_mask_img, alpha, face_mix_img, 1 - alpha, 0, face_mix_img)
    save_image(mix_path, face_mix_img)

if __name__ == "__main__":
    data_dir = 'D:/pic/图片替换/1/' #图片存放路径
    walk_dir(data_dir)