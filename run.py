#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/2 19:09
# @Author  : wuyfee
# @File    : run.py.py
# @Software: PyCharm

import os
import pytest

if __name__ == '__main__':
    # pytest.main(['-s', './testcase/test_RegisterPage.py', '--alluredir', './allure-results'])
    pytest.main()

    # 生成测试报告
    # os.system('allure generate ./allure-results -o ./results')