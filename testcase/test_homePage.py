#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 13:45
# @Author  : wuyfee
# @File    : test_homePage.py
# @Software: PyCharm

from utils.excelUtil import ExcelUtil
from utils.logger import Logger
import pytest

logger = Logger(logger="test_homePage", name="test_homePage").getlog()


class TestHomePage:
    '''
    do_conf = ParseConfFile()
    homePage = do_conf.get_value('HomePageElements', 'homePage')
    knowGuangfa = do_conf.get_value('HomePageElements', 'knowGuangfa')

    @pytest.mark.run(order=1)
    def test_homePage(self, get_homePage):
        """点击 [首页] 按钮"""
        get_homePage.click_home_page_menu(*self.homePage)

    '''

    @pytest.mark.parametrize(
        "testName, by, locator, resultBy, resultLocator, resultMessage, isBack",
        ExcelUtil().read_excel('others'))
    def test_homePage_menu(self, testName, by, locator, resultBy, resultLocator,
                           resultMessage, isBack, get_homePage):
        """点击 [首页菜单] 各按钮"""
        logger.info("test_homePage_menu case: %s" % testName)
        message = get_homePage.click_homePage_menu(by, locator, resultBy, resultLocator, isBack)
        try:
            assert message == resultMessage
            logger.info("PASS!")
        except AssertionError as ae:
            print(ae)
            logger.error("Fail! test_homePage_menu: %s ====> %s != %s" % testName % message % resultMessage)

    @pytest.mark.parametrize(
        "testName, handleBy, handleLocator, by, locator, jumpPage, resultBy, resultLocator, attribute, resultMessage",
        ExcelUtil().read_excel('knowGuangfa'))
    def test_knowGuangfa(self, testName, handleBy, handleLocator, by, locator, jumpPage, resultBy, resultLocator,
                         attribute, resultMessage, get_homePage):
        """点击 [认识广发] 按钮"""
        logger.info("test_knowGuangfa case: %s" % testName)
        message = get_homePage.click_knowGuangfa(handleBy, handleLocator, by, locator, jumpPage, resultBy, resultLocator)
        try:
            assert message == resultMessage
            logger.info("PASS!")
        except AssertionError as ae:
            logger.error("Fail! test_homePage_menu->test_knowGuangfa: %s ====> %s != %s" % testName % message % resultMessage)

    @pytest.mark.parametrize(
        "testName, handleBy, handleLocator, by, locator, resultBy, resultLocator, resultMessage",
        ExcelUtil().read_excel('peopleInGuangfa'))
    def test_peopleInGuangfa(self, testName, handleBy, handleLocator, by, locator, resultBy, resultLocator,
                             resultMessage, get_homePage):
        """点击 [人在广发] 按钮"""
        logger.info("test_peopleInGuangfa case: %s" % testName)
        message = get_homePage.click_peopleInGuangfa(handleBy, handleLocator, by, locator, resultBy, resultLocator)
        try:
            assert message == resultMessage
            logger.info("PASS!")
        except AssertionError as ae:
            logger.error("Fail! test_homePage_menu->test_peopleInGuangfa: %s ====> %s != %s" % testName % message % resultMessage)


if __name__ == '__main__':
    pytest.main(['-vs'])
