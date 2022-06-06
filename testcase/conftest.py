#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 21:29
# @Author  : wuyfee
# @File    : conftest.py
# @Software: PyCharm
import os
from time import sleep

import pytest
import shutil

from config.conf import REPORT_DIR
from page.PageObject.HomePage import HomePage
from page.PageObject.LoginPage import LoginPage
from page.PageObject.RegisterPage import RegisterPage
from utils.driverEngine import DriverEngine
from utils.parseConfFile import ParseConfFile
from utils.sendEmail import SendEmail

do_conf = ParseConfFile()
login = do_conf.get_value('HomePageElements', 'login')
register = do_conf.get_value('HomePageElements', 'register')
home = do_conf.get_value('HomePageElements', 'homePage')
isSendEmail = do_conf.get_value('BaseSetting', 'isSendEmail')


@pytest.fixture(scope='session')
def init_pages():
    # 先清空report目录
    shutil.rmtree(REPORT_DIR)
    os.mkdir(REPORT_DIR)

    driver = DriverEngine().get_driver()
    home_page = HomePage(driver=driver, timeout=2)
    login_page = LoginPage(driver=driver, timeout=2)
    register_page = RegisterPage(driver=driver, timeout=2)
    print("home_page---login_page---register_page")
    yield home_page, login_page, register_page
    DriverEngine().quit_driver()
    # 是否发送邮件
    if isSendEmail == 'True':
        SendEmail().send_email()


@pytest.fixture(scope='class')
def get_homePage(init_pages):
    homePage = init_pages[0]
    homePage.click(*home)
    yield homePage


@pytest.fixture(scope='class')
def get_loginPage(init_pages):
    loginPage = init_pages[1]
    loginPage.click(*login)
    yield loginPage


@pytest.fixture(scope='class')
def get_registerPage(init_pages):
    registerPage = init_pages[2]
    registerPage.click(*register)
    yield registerPage
