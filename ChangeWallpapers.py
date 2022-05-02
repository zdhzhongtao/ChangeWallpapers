# -*- coding: utf-8 -*-
'''
Date: 2022-05-02 19:22:19
LastEditors: Zhong.donghong
LastEditTime: 2022-08-02 22:04:40
Description: 切换桌面壁纸，放在一个文件夹下随机选择
'''
import random
import ctypes
import time
import os
from logger import logger

path = r"C:\Users\HomeDevelop\Pictures\ChangeWallpapers"
def file_filter(f):
    if f[-4:] in ['.jpg', '.png', '.bmp']:
        return True
    else:
        return False


def changePic():
    files = os.listdir(path);  # 打开存储图片文件夹中的图片目录
    files = list(filter(file_filter, files))
    filepath = path +"\\" + random.choice(files);  # 随机选取某张图片，建立绝对地址
    logger.info(filepath)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)  # 设置桌面壁纸

def lockWin():
    while True:
        changePic()
        time.sleep(30 * 60);  # 睡眠半个小时

if __name__ == '__main__':
    changePic()
    # lockWin() //静态默认修改
