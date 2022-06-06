#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/5/31 16:24
# @Author  : wuyfee
# @File    : parseConfFile.py
# @Software: PyCharm

import configparser
from config.conf import CONF_PATH


class ParseConfFile(object):

    def __init__(self):
        self.file = CONF_PATH
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file, encoding='utf-8')

    def get_all_sections(self):
        """获取所有的section，返回一个列表"""
        return self.conf.sections()

    def get_all_options(self, section):
        """获取指定section下所有的option, 返回列表"""
        return self.conf.options(section)

    def get_value(self, section, option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try:
            value = self.conf.get(section, option)
            if '->' in value:
                value = tuple(value.split('->'))
            return value
        except configparser.NoOptionError as e:
            print('error:', e)
        return 'error: No option "{}" in section: "{}"'.format(option, section)

    def get_option_value(self, section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value


if __name__ == '__main__':
    parse = ParseConfFile()
    sections = parse.get_all_sections()
    print("sectuons:", sections)
    options = parse.get_all_options(sections[0])
    print("options:", options)
    options_val = parse.get_option_value(sections[0])
    print("option_val", options_val)
    loc = parse.get_value(sections[0], options[0])
    print("loc:", loc)
