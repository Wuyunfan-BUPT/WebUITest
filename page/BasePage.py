#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/5/31 16:07
# @Author  : wuyfee
# @File    : BasePage.py
# @Software: PyCharm
import time

from selenium.common.exceptions import TimeoutException, NoAlertPresentException

# from utils.logger import Logger
from selenium.webdriver import ActionChains

from config.conf import SCREENSHOT_DIR
from utils.clipboard import ClipBoard
from utils.driverEngine import DriverEngine
from utils.keyboard import KeyBoard
from utils.logger import Logger
from utils.parseConfFile import ParseConfFile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec

logger = Logger(logger="BasePage", name="BasePage").getlog()


class BasePage(object):
    cf = ParseConfFile()

    def __init__(self, driver, timeout=30):
        self.byDic = {
            "id": By.ID,
            "xpath": By.XPATH,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT,
            "name": By.NAME,
            "tag_name": By.TAG_NAME,
            "class_name": By.CLASS_NAME,
            "css_selector": By.CSS_SELECTOR
        }
        self.driver = driver
        self.outTime = timeout

    def find_element(self, by, locator):
        try:
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(self.byDic[by], locator))
            # logger.info('Find the element "{}" by "{}"!'.format(locator, by))
        except TimeoutError as e:
            logger.error(e)
        else:
            return element

    def find_elements(self, by, locator):
        try:
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(self.byDic[by], locator))
            # logger.info('Find the elements "{}" by "{}"!'.format(locator, by))
        except TimeoutError as e:
            logger.error(e)
        else:
            return elements

    def get_attribute(self, by, locator, attribute):
        try:
            element = self.find_element(by, locator)
            attributeValue = element.get_attribute(attribute)
            # logger.info('Find the element "{}" attribute "{}" by "{}"!'.format(locator, attribute, by))
        except TimeoutError as e:
            logger.error(e)
        else:
            return attributeValue

    def is_element_exist(self, by, locator):
        """
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime).until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                logger.error('Element "{}" not exist'.format(locator))
                return False
            return True
        else:
            logger.error('The "{}" error!'.format(by))

    def is_click(self, by, locator):
        """判断某个元素是否可点击"""
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime).until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                logger.error("The element unclickable! {}".format(locator))
                return None
            else:
                return element
        else:
            logger.error('the "{}" error!'.format(by))

    def get_element_text(self, by, locator):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            return element.text
        except AttributeError:
            logger.info('Get "{}" text failed! return None'.format(locator))

    def send_keys(self, by, locator, value=''):
        """写数据"""
        # logger.info('Input "{}".'.format(value))
        try:
            element = self.find_element(by, locator)
            element.clear()
            element.send_keys(value)
        except AttributeError as e:
            logger.error('Error! input "{}". {}'.format(value, e))
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        # logger.info('Clear box value.')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            logger.error('Clear fail!', e)

    def click(self, by, locator):
        """点击某个元素"""
        # logger.info('Info: click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element is not None:
            element.click()
        else:
            logger.warn('The "{}" unclickable!'.format(locator))
            return None

    def get_screenshot(self):
        screenshot_path = SCREENSHOT_DIR
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = f"{screenshot_path}/{rq}.png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            # logger.info("Had take screenshot and save to folder : /screenShots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)

    def forward(self):
        """浏览器前进"""
        self.driver.forward()
        # logger.info("Click forward on current page.")

    def back(self):
        """浏览器后退"""
        self.driver.back()
        # logger.info("Click back on current page.")

    def close(self):
        """关闭窗口"""
        try:
            self.driver.close()
            # logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    @staticmethod
    def sleep(seconds=0):
        """强制等待"""
        # logger.info('Sleep "{}" seconds'.format(seconds))
        time.sleep(seconds)

    def ctrl_v(self, value):
        """ctrl + V 粘贴"""
        # logger.info('Pasting "{}"'.format(value))
        ClipBoard.set_text(value)
        self.sleep(3)
        KeyBoard.two_keys('ctrl', 'v')

    @staticmethod
    def enter_key():
        """enter 回车键"""
        # logger.info('Keydown enter')
        KeyBoard.one_key('enter')

    def handle_mouse(self, by, locator):
        """悬停鼠标"""
        if by.lower() in self.byDic:
            position = self.find_element(by, locator)
            action = ActionChains(self.driver)
            action.move_to_element(position)
            action.perform()
        else:
            logger.error("{} error!".format(by))

    def quit_driver(self):
        DriverEngine.quit_driver()


if __name__ == "__main__":
    pass
