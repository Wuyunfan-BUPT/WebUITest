#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/5/31 16:01
# @Author  : wuyfee
# @File    : conf.py
# @Software: PyCharm


from datetime import datetime
import os


# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# 日志目录
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
# driver地址
DRIVER_PATH = os.path.join(ROOT_DIR, 'driverType')
# 截图保存目录
SCREENSHOT_DIR = os.path.join(ROOT_DIR, 'screenShots')
# Excel地址
EXCEL_DIR = os.path.join(ROOT_DIR, 'data')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 需要发送的测试报告目录
EMAIL_PATH = os.path.join(ROOT_DIR, 'report_email')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')
