#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/5/31 18:03
# @Author  : wuyfee
# @File    : driverEngine.py
# @Software: PyCharm


import os.path
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH
from utils.logger import Logger
from utils.parseConfFile import ParseConfFile

logger = Logger(logger="DriverEngine", name="DriverEngine").getlog()


class DriverEngine(object):
    __driver = None

    @classmethod
    def get_driver(cls):
        """初始化浏览器对象"""
        chrome_driver_path = f"{DRIVER_PATH}/chromedriver.exe"
        ie_driver_path = f"{DRIVER_PATH}/IEDriverServer.exe"
        # 读取配置配件
        do_conf = ParseConfFile()
        browserName = do_conf.get_value('BaseSetting', 'browserName')
        logger.info("Browser type: {}.".format(browserName))
        testUrl = do_conf.get_value('BaseSetting', 'testURL')
        logger.info("Test URL is {}.".format(testUrl))

        if browserName == "Firefox":
            cls.__driver = webdriver.Firefox()
        elif browserName == "Chrome":
            cls.__driver = webdriver.Chrome(chrome_driver_path)
        elif browserName == "IE":
            cls.__driver = webdriver.Ie(ie_driver_path)
        else:
            logger.info("Please set browser in config.ini. You can choose: Chrome, Firefox, IE")
            return

        cls.__driver.get(testUrl)
        cls.__driver.maximize_window()
        logger.info("Maximize the current window.")
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """完成测试，退出浏览器"""
        logger.info("Test complete！Quit the test now.")
        cls.__driver.quit()
        cls.__driver = None
'''
if __name__ == '__main__':
    pass
    
    DriverEngine.get_driver()
    sleep(2)
    DriverEngine.quit_driver()
    '''