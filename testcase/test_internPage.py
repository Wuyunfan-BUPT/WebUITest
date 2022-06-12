#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/12 11:08
# @Author  : wuyfee
# @File    : test_internPage.py
# @Software: PyCharm


import pytest

from utils.excelUtil import ExcelUtil
from utils.logger import Logger

logger = Logger(logger="test_internPage", name="test_internPage").getlog()


class TestInternPage:

    @pytest.mark.parametrize(
        "testName, inputText, resultBy, resultLocator, resultMessage",
        ExcelUtil().read_excel('internRecruitmentSearch'))
    def test_search_click(self, testName, inputText, resultBy, resultLocator, resultMessage, get_internPage):
        """测试[搜索框] , 使用鼠标点击的方式"""
        logger.info("TestInterPage::test_searchBox by click case: {}".format(testName))
        message = get_internPage.search_click(inputText, resultBy, resultLocator)
        assert resultMessage == message

    @pytest.mark.parametrize(
        "testName, inputText, resultBy, resultLocator, resultMessage",
        ExcelUtil().read_excel('internRecruitmentSearch'))
    def test_search_enter(self, testName, inputText, resultBy, resultLocator, resultMessage, get_internPage):
        """测试[搜索框]，使用键盘输入Enter的方式"""
        logger.info("TestInterPage::test_searchBox by enter case: {}".format(testName))
        message = get_internPage.search_enter(inputText, resultBy, resultLocator)
        assert resultMessage == message

    @pytest.mark.parametrize(
        "testName, cityBy, cityLocator, postBy, postLocator, resultMessage, resultBy, resultLocator",
        ExcelUtil().read_excel('internRecruitment'))
    def test_select_post(self, testName, cityBy, cityLocator, postBy, postLocator, resultMessage, resultBy, resultLocator, get_internPage):
        """测试 [选择城市+岗位]"""
        logger.info("TestInterPage::test_selectPost case: {}".format(testName))
        message = get_internPage.select_post(cityBy, cityLocator, postBy, postLocator, resultBy, resultLocator)
        assert resultMessage == message
