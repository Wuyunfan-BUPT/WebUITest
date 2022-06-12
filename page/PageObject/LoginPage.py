#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 18:48
# @Author  : wuyfee
# @File    : LoginPage.py
# @Software: PyCharm
from page.BasePage import BasePage
from utils.parseConfFile import ParseConfFile


class LoginPage(BasePage):
    do_conf = ParseConfFile()
    emailAddressBox = do_conf.get_value('LoginPageElements', 'emailAddressBox')
    passwordBox = do_conf.get_value('LoginPageElements', 'passwordBox')
    captchaBox = do_conf.get_value('LoginPageElements', 'captchaBox')
    bottomSubmit = do_conf.get_value('LoginPageElements', 'bottomSubmit')
    agree = do_conf.get_value('LoginPageElements', 'agree')
    protocol = do_conf.get_value('LoginPageElements', 'protocol')
    protocolMessage = do_conf.get_value('LoginPageElements', 'protocolMessage')
    register = do_conf.get_value('LoginPageElements', 'register')
    registerMessage = do_conf.get_value('LoginPageElements', 'registerMessage')
    forgetPassword = do_conf.get_value('LoginPageElements', 'forgetPassword')
    forgetPasswordMessage = do_conf.get_value("LoginPageElements", "forgetPasswordMessage")
    changeCaptcha = do_conf.get_value('LoginPageElements', 'changeCaptcha')
    captchaImg = do_conf.get_value('LoginPageElements', 'captchaImg')
    # loginFailMessage = do_conf.get_value('LoginPageElements', 'loginFailMessage')
    # loginSuccessMessage = do_conf.get_value('LoginPageElements', 'loginSuccessMessage')

    def login(self, email, password, captcha, resultBy, resultLocator, isSuccess):
        """测试登录用例"""
        self.input_emailAddress(email)
        self.input_password(password)
        self.input_captcha(captcha)
        self.click_bottom()
        # self.click(*self.bottomSubmit)
        self.sleep(1)
        message = self.get_element_text(resultBy, resultLocator)
        # 如果登录成功，跳转回原来的登录界面
        if isSuccess == 'Y':
            self.click(resultBy, resultLocator)
        return message

    '''

    def login_success(self, email, password, captcha):
        self.input_emailAddress(email)
        self.input_password(password)
        self.input_captcha(captcha)
        self.click(*self.bottomSubmit)
        message = self.get_element_text(*self.loginSuccessMessage)  # self.get_element_text(*self.loginSuccessMessage)
        self.click(*self.loginSuccessMessage)
        return message

    def login_fail(self, email, password, captcha):
        self.input_emailAddress(email)
        self.input_password(password)
        self.input_captcha(captcha)
        self.click(*self.bottomSubmit)
        self.sleep(1)
        return self.get_element_text(*self.loginFailMessage)
    '''

    def click_register(self):
        """点击 [注册新用户]"""
        handles = self.driver.window_handles
        self.click(*self.register)
        self.driver.switch_to.window(handles[-1])
        message = self.get_element_text(*self.registerMessage)
        self.back()
        return message

    def click_forgetPassword(self):
        """点击 [忘记密码]"""
        self.click(*self.forgetPassword)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        message = self.get_element_text(*self.forgetPasswordMessage)
        self.back()
        return message

    def click_changeCaptcha(self, attribute):
        """点击 [换一张]"""
        self.click(*self.changeCaptcha)
        message = self.get_attribute(*self.captchaImg, attribute)
        return message

    def click_protocol(self):
        """点击广发证券协议链接"""
        self.click(*self.protocol)
        message = self.get_element_text(*self.protocolMessage)
        self.back()
        return message

    def click_agree(self):
        """点击同意协议选项"""
        self.click(*self.agree)
        message_false = self.find_element(*self.bottomSubmit).is_enabled()
        self.click(*self.agree)
        message_true = self.find_element(*self.bottomSubmit).is_enabled()
        return message_false, message_true
    '''
    def emailBox_clipboard(self, text):
        """粘贴剪切板内容"""
        ClipBoard.set_text(text)
        if text is not None:
            self.send_keys(*self.emailAddressBox, ClipBoard.get_text())
        else:
            self.clear_emailAddressBox()
        message =

    '''



    def input_emailAddress(self, email):
        """在邮件地址框输入邮件信息"""
        if email is not None:
            self.clear_emailAddressBox()
            self.send_keys(*self.emailAddressBox, email)
        else:
            self.clear_emailAddressBox()

    def input_password(self, password):
        """在邮件地址框输入邮件信息"""
        if password is not None:
            self.clear_passwordBox()
            self.send_keys(*self.passwordBox, password)
        else:
            self.clear_passwordBox()

    def input_captcha(self, captcha):
        """在邮件地址框输入邮件信息"""
        if captcha is not None:
            self.clear_captchaBox()
            self.send_keys(*self.captchaBox, captcha)
        else:
            self.clear_captchaBox()


    def clear_emailAddressBox(self):
        """清除邮箱地址框的内容"""
        self.clear(*self.emailAddressBox)

    def clear_passwordBox(self):
        """清除登录密码框的内容"""
        self.clear(*self.passwordBox)

    def clear_captchaBox(self):
        """清除验证码框的内容"""
        self.clear(*self.captchaBox)

    def clear_all(self):
        "清除邮件地址、登录密码、验证码框的内容"
        self.clear_emailAddressBox()
        self.clear_passwordBox()
        self.clear_captchaBox()
        
    def click_bottom(self):
        """点击登录按钮"""
        self.click(*self.bottomSubmit)
    

