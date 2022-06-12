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
from page.PageObject.internPage import InternPage
from utils.driverEngine import DriverEngine
from utils.parseConfFile import ParseConfFile
from utils.sendEmail import SendEmail

do_conf = ParseConfFile()
login = do_conf.get_value('HomePageElements', 'login')
register = do_conf.get_value('HomePageElements', 'register')
home = do_conf.get_value('HomePageElements', 'homePage')
intern = do_conf.get_value('HomePageElements', 'internshipHirePage')


@pytest.fixture(scope='session')
def init_pages():
    # 先清空report目录
    shutil.rmtree(REPORT_DIR)
    os.mkdir(REPORT_DIR)

    driver = DriverEngine().get_driver()
    home_page = HomePage(driver=driver, timeout=2)
    login_page = LoginPage(driver=driver, timeout=2)
    register_page = RegisterPage(driver=driver, timeout=2)
    intern_Page = InternPage(driver=driver, timeout=2)
    print("home_page---login_page---register_page")
    yield home_page, login_page, register_page, intern_Page
    DriverEngine().quit_driver()


@pytest.mark.run(order=1)
@pytest.fixture(scope='function')
def get_homePage(init_pages):
    homePage = init_pages[0]
    homePage.click(*home)
    yield homePage


@pytest.mark.run(order=2)
@pytest.fixture(scope='function')
def get_internPage(init_pages):
    internPage = init_pages[3]
    internPage.click(*intern)
    yield internPage


@pytest.mark.run(order=3)
@pytest.fixture(scope='function')
def get_registerPage(init_pages):
    registerPage = init_pages[2]
    registerPage.click(*register)
    yield registerPage


@pytest.mark.run(order=4)
@pytest.fixture(scope='function')
def get_loginPage(init_pages):
    loginPage = init_pages[1]
    loginPage.click(*login)
    yield loginPage


