#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/1 11:12
# @Author  : wuyfee
# @File    : logger.py
# @Software: PyCharm


import logging
import os.path
import time

from config.conf import LOG_DIR


class Logger(object):
    def __init__(self, logger, name):
        """
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        log_path = LOG_DIR
        log_name = os.path.join(log_path, f'{name}_{rq}.log')
        # log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'
        # log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
