#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 19:41
# @Author  : wuyfee
# @File    : test_loginPage.py
# @Software: PyCharm


import pytest

from utils.excelUtil import ExcelUtil
from utils.logger import Logger
from utils.parseConfFile import ParseConfFile

logger = Logger(logger="test_loginPage", name="test_loginPage").getlog()


class TestLoginPage:
    do_conf = ParseConfFile()
    login = do_conf.get_value('HomePageElements', 'login')
    register = do_conf.get_value('HomePageElements', 'register')
    captchaImg = do_conf.get_value('LoginPageElements', 'captchaImg')

    @pytest.mark.parametrize(
        "testName, email, password, captcha, resultMessage, resultBy, resultLocator, isSuccess",
        ExcelUtil().read_excel('login'))
    def test_login(self, testName, email, password, captcha, resultMessage, resultBy, resultLocator, isSuccess,
                   get_loginPage):
        """ [登录] 操作用例"""
        # get_loginPage.click(*self.login)
        logger.info("test_login case: {}".format(testName))
        message = get_loginPage.login(email, password, captcha, resultBy, resultLocator, isSuccess)
        # 先写入日志
        if message == resultMessage:
            logger.info("PASS!")
        else:
            logger.error("Failed! test_logonPage_login: {} ====> {} != {}".format(testName, message, resultMessage))
        assert message == resultMessage

    def test_forgetPassword(self, get_loginPage):
        """测试 [忘记密码] 链接"""
        # get_loginPage.click(*self.login)
        logger.info("test_forgetPassword case: {}".format("忘记密码按钮"))
        message = get_loginPage.click_forgetPassword()
        assert message == "回答问题找回密码"

    def test_register(self, get_loginPage):
        """测试 [注册新用户] 链接"""
        # get_loginPage.click(*self.register)
        logger.info("test_register case: {}".format("注册新用户"))
        message = get_loginPage.click_register()
        assert message == "用户注册"

    def test_changeCaptcha(self, get_loginPage):
        """测试 [换一张】 链接"""
        logger.info("test_changeCaptcha case: {}".format("[换一张]"))
        src = get_loginPage.get_attribute(self.captchaImg[0], self.captchaImg[1], "src")
        change_src = get_loginPage.click_changeCaptcha("src")
        assert src != change_src

    def test_protocol(self, get_loginPage):
        """测试 [《广发证券互联网用户服务协议》] 链接"""
        logger.info("test_protocol case: {}".format("[广发证券互联网用户服务协议]"))
        message = get_loginPage.click_protocol()
        assert message == "广发证券互联网用户服务协议"

    def test_agree(self, get_loginPage):
        """测试 [我已阅读并同意] 按钮"""
        logger.info("test_agreeCheckox case: {}".format("同意协议按钮"))
        message_false, message_true = get_loginPage.click_agree()
        assert (not message_false) and message_true

    '''
    def test_login_success(self, get_loginPage):
        """测试 [登录成功] 情形"""
        # get_loginPage.click(*self.login)
        message = get_loginPage.login_success("wyf_mohen@163.com", "Abc123", "FHJV")
        assert message == '退出'

    @pytest.mark.parametrize("email, password, captcha, errorMessage", ExcelUtil().read_excel('login'))
    def test_login_fail(self, email, password, captcha, errorMessage, get_loginPage):
        """测试 [登录失败] 情形"""
        # get_loginPage.click(*self.login)
        error_text = get_loginPage.login_fail(email, password, captcha)
        assert error_text == errorMessage

   
    '''
    '''
    #@data(*ExcelUtil().read_excel())
    #@unpack
    @pytest.mark.parametrize("username, password", ExcelUtil().read_excel())
    def test_login(self, username, password):
        pass
        # print(username, password)

    '''


if __name__ == '__main__':
    pytest.main(['-vs'])
