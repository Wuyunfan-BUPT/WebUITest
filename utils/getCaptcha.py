#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/2 19:49
# @Author  : wuyfee
# @File    : getCaptcha.py
# @Software: PyCharm
import time

from selenium import webdriver
from PIL import Image, ImageEnhance
import pytesseract

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://job.gf.com.cn/signup/login')
        self.driver.maximize_window()

    def test1(self):
         #获取验证码图片
        t = time.time() #获取当前时间
        picture_name1 = str(t)+'.png'
        self.driver.save_screenshot(picture_name1) #保存截屏
        ce = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/form/div[3]/div[2]/img")
        print(ce.location)

        left = ce.location['x']
        top = ce.location['y']
        right = ce.size['width'] + left + 140
        height = ce.size['height'] + top+140

        im = Image.open(picture_name1)
         # 抠图
        img = im.crop((left+110, top+110, right, height))

        t = time.time()
        picture_name2 = str(t)+'.png'
        img = img.convert('RGBA')  # 转换模式：L | RGB
        img = img.convert('L')  # 转换模式：L | RGB
        img = ImageEnhance.Contrast(img)  # 增强对比度
        img = img.enhance(2.0)  # 增加饱和度

        img.save(picture_name2)#这里就是截取到的验证码图片

        self.driver.close()

        image1 = Image.open(picture_name2)
        str1 = pytesseract.image_to_string(image1)
        print(str1)

if __name__ == '__main__':
    case = TestCase()
    case.test1()
