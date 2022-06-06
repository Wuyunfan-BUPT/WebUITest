#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/3 12:17
# @Author  : wuyfee
# @File    : test_RegisterPage.py
# @Software: PyCharm


import pytest

from utils.excelUtil import ExcelUtil
from utils.logger import Logger
from utils.parseConfFile import ParseConfFile

logger = Logger(logger="test_registerPage", name="test_registerPage").getlog()


class TestRegisterPage:
    do_conf = ParseConfFile()
    # login = do_conf.get_value('HomePageElements', 'login')
    # register = do_conf.get_value('HomePageElements', 'register')
    captchaImg = do_conf.get_value('RegisterElements', 'captchaImg')

    @pytest.mark.parametrize(
        "testName, email, password, confirmPassword, passwordQuestion, questionAnswer, captcha, resultMessage,"
        "resultBy, resultLocator, isSuccess",
        ExcelUtil().read_excel('register'))
    def test_register(self, testName, email, password, confirmPassword, passwordQuestion, questionAnswer, captcha,
                      resultMessage, resultBy, resultLocator, isSuccess, get_registerPage):
        """测试 [注册] 情形"""
        # get_registerPage.click(*self.register)
        logger.info("test_register case: {}".format(testName))
        logger.info("case info: {} -- {} -- {} -- {} -- {} -- {} -- {} -- {}".format(email, password, confirmPassword,
                                                                                     passwordQuestion, questionAnswer,
                                                                                     captcha, resultMessage, isSuccess))

        message = get_registerPage.click_register(email, password, confirmPassword, passwordQuestion, questionAnswer,
                                                  captcha, resultBy, resultLocator, isSuccess)
        assert message == resultMessage.split(',')

    def test_changeCaptcha(self, get_registerPage):
        """测试 [换一张】 链接"""
        logger.info("test_RegisterPage: test_changeCaptcha case")
        src = get_registerPage.get_attribute(*self.captchaImg, "src")
        change_src = get_registerPage.click_changeCaptcha("src")
        assert src != change_src

    def test_protocolLink(self, get_registerPage):
        """测试 [《广发证券互联网用户服务协议》] 链接"""
        logger.info("test_RegisterPage: test_protocolLink case")
        message = get_registerPage.click_protocolLink()
        assert message == "广发证券互联网用户服务协议"

    def test_agreeCheckBox(self, get_registerPage):
        """测试 [我已阅读并同意] 按钮"""
        logger.info("test_RegisterPage: test_agreeCheckBox case")
        message_true, message_false = get_registerPage.click_agreeCheckBox()
        assert message_true and (not message_false)


if __name__ == '__main__':
    pytest.main(['-vs'])
