#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/2 19:09
# @Author  : wuyfee
# @File    : run.py.py
# @Software: PyCharm

import pytest

from utils.parseConfFile import ParseConfFile
from utils.sendEmail import SendEmail

do_conf = ParseConfFile()

isSendEmail = do_conf.get_value('BaseSetting', 'isSendEmail')


if __name__ == '__main__':
    # pytest.main(['-s', './testcase/test_RegisterPage.py', '--alluredir', './allure-results'])
    pytest.main()

    # 发送邮件
    if isSendEmail == 'True':
        SendEmail().send_email()

    # 生成测试报告
    # os.system('allure generate ./allure-results -o ./results')