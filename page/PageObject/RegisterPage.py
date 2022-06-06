#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 18:49
# @Author  : wuyfee
# @File    : RegisterPage.py
# @Software: PyCharm
from page.BasePage import BasePage
from utils.parseConfFile import ParseConfFile


class RegisterPage(BasePage):
    do_conf = ParseConfFile()
    emailAddressBox = do_conf.get_value('RegisterElements', 'emailAddressBox')
    passwordBox = do_conf.get_value('RegisterElements', 'passwordBox')
    confirmPasswordBox = do_conf.get_value('RegisterElements', 'confirmPasswordBox')
    passwordQuestion = do_conf.get_value('RegisterElements', 'passwordQuestion')
    questionAnswer = do_conf.get_value('RegisterElements', 'questionAnswer')
    captchaBox = do_conf.get_value('RegisterElements', 'captchaBox')
    bottomSubmit = do_conf.get_value('RegisterElements', 'bottomSubmit')
    agreeCheckBox = do_conf.get_value('RegisterElements', 'agreeCheckBox')
    protocol = do_conf.get_value('RegisterElements', 'protocol')
    protocolMessage = do_conf.get_value('RegisterElements', 'protocolMessage')
    changeCaptcha = do_conf.get_value('RegisterElements', 'changeCaptcha')
    captchaImg = do_conf.get_value('RegisterElements', 'captchaImg')
    # errorMessages = do_conf.get_value('RegisterElements', 'errorMessages')
    captchaErrorMessage = do_conf.get_value('RegisterElements', 'captchaErrorMessage')

    def click_register(self, email, password, confirmPassword, passwordQuestion, questionAnswer, captcha,
                       resultBy, resultLocator, isSuccess):
        """测试 [注册] 页面注册选项"""
        self.input_emailAddress(email)
        self.input_password(password)
        self.input_confirmPassword(confirmPassword)
        self.input_passwordQuestion(passwordQuestion)
        self.input_questionAnswer(questionAnswer)
        self.input_captcha(captcha)

        self.click(*self.agreeCheckBox)
        self.click(*self.bottomSubmit)
        self.click(*self.agreeCheckBox)
        message = self.get_message_text(resultBy, resultLocator)
        if isSuccess == 'Y':
            self.click(resultBy, resultLocator)
        return message

    def click_changeCaptcha(self, attribute):
        """[换一张] 验证码"""
        self.click(*self.changeCaptcha)
        message = self.get_attribute(*self.captchaImg, attribute)
        return message

    def click_protocolLink(self):
        """点击 [广发证券协议] 链接"""
        self.click(*self.protocol)
        message = self.get_element_text(*self.protocolMessage)
        self.back()
        return message

    def click_agreeCheckBox(self):
        """点击同意协议选项"""
        self.click(*self.agreeCheckBox)
        message_true = self.find_element(*self.bottomSubmit).is_enabled()
        self.click(*self.agreeCheckBox)
        message_false = self.find_element(*self.bottomSubmit).is_enabled()
        return message_true, message_false

    def input_emailAddress(self, email):
        """在 [邮件地址] 输入邮件信息"""
        if email is not None:
            self.send_keys(*self.emailAddressBox, email)
        else:
            self.clear_emailAddress()

    def input_password(self, password):
        """在 [邮件地址] 输入邮件信息"""
        if password is not None:
            self.send_keys(*self.passwordBox, password)
        else:
            self.clear_password()

    def input_confirmPassword(self, confirmPassword):
        """在 [确认密码] 输入密码"""
        if confirmPassword is not None:
            self.send_keys(*self.confirmPasswordBox, confirmPassword)
        else:
            self.clear_confirmPassword()

    def input_passwordQuestion(self, question):
        """在 [密码问题] 输入密码问题"""
        if question is not None:
            self.send_keys(*self.passwordQuestion, question)
        else:
            self.clear_passwordQuestion()

    def input_questionAnswer(self, answer):
        """在 [问题答案] 输入问题答案"""
        if answer is not None:
            self.send_keys(*self.questionAnswer, answer)
        else:
            self.clear_questionAnswer()

    def input_captcha(self, captcha):
        """在 [验证码] 输入验证码"""
        if captcha is not None:
            self.send_keys(*self.captchaBox, captcha)
        else:
            self.clear_captcha()

    def get_message_text(self, resultBy, resultLocator):
        """获取结果信息"""
        self.sleep(1)
        messageList = self.find_elements(resultBy, resultLocator)
        messages = []
        for message in messageList:
            if message.text != "":
                messages.append(message.text)
        captchaMessage = self.get_element_text(*self.captchaErrorMessage)
        if captchaMessage != "":
            messages.append(captchaMessage)
        return messages

    def clear_emailAddress(self):
        """清除 [邮件地址] 框内容"""
        self.clear(*self.emailAddressBox)

    def clear_password(self):
        """清除 [登录密码] 框内容"""
        self.clear(*self.passwordBox)

    def clear_confirmPassword(self):
        """清除 [确认密码] 框内容"""
        self.clear(*self.confirmPasswordBox)

    def clear_passwordQuestion(self):
        """清除 [密码问题] 框内容"""
        self.clear(*self.passwordQuestion)

    def clear_questionAnswer(self):
        """清除 [问题答案] 框内容"""
        self.clear(*self.questionAnswer)

    def clear_captcha(self):
        """清除 [验证码] 框内容"""
        self.clear(*self.captchaBox)
