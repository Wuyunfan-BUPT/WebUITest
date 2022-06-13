#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/12 10:13
# @Author  : wuyfee
# @File    : internPage.py
# @Software: PyCharm
from page.BasePage import BasePage
from utils.keyboard import KeyBoard
from utils.parseConfFile import ParseConfFile


class InternPage(BasePage):
    do_conf = ParseConfFile()
    searchBox = do_conf.get_value('InternRecruitment', 'searchBox')

    searchButton = do_conf.get_value('InternRecruitment', 'searchButton')
    # loginFailMessage = do_conf.get_value('LoginPageElements', 'loginFailMessage')
    # loginSuccessMessage = do_conf.get_value('LoginPageElements', 'loginSuccessMessage')

    def search_click(self, inputText, resultBy, resultLocator):
        """测试搜索框，使用鼠标点击[查询]框的方式"""
        self.send_keys(*self.searchBox, inputText)
        self.click(*self.searchButton)
        self.sleep(1)
        message = self.get_element_text(resultBy, resultLocator)
        return message

    def search_enter(self, inputText, resultBy, resultLocator):
        """测试搜索框，使用键盘输入[enter]的方式"""
        self.send_keys(*self.searchBox, inputText)
        KeyBoard.key_down('enter')
        KeyBoard.key_down('enter')
        self.sleep(2)
        message = self.get_element_text(resultBy, resultLocator)
        return message

    def select_post(self, cityBy, cityLocator, postBy, postLocator, resultBy, resultLocator):
        """选择城市+岗位"""
        self.click(cityBy, cityLocator)
        self.click(postBy, postLocator)
        self.sleep(3)
        message = self.get_element_text(resultBy, resultLocator)

        return message

