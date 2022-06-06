#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Project : Guangfa UI test
# @Time    : 2022/6/4 19:16
# @Author  : wuyfee
# @File    : sendEmail.py
# @Software: PyCharm

import smtplib
import zipfile
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import os
import time

from config.conf import EMAIL_PATH, REPORT_DIR
from utils.logger import Logger
from utils.parseConfFile import ParseConfFile

logger = Logger(logger="sendEmail", name="sendEmail").getlog()


class SendEmail:
    def __init__(self):
        do_conf = ParseConfFile()
        self.username = do_conf.get_value('Email', 'username')  # 发件人姓名
        self.email = do_conf.get_value('Email', 'email')  # 发件人邮箱账号
        self.password = do_conf.get_value('Email', 'password')  # 发件人邮箱密码
        self.receiver = do_conf.get_value('Email', 'receiver')  # 收件人
        self.emailPath = EMAIL_PATH  # 报告压缩目录
        self.report_path = REPORT_DIR  # 报告目录

    def zip_report(self, reportZip_name):
        """将报告打包成zip文件"""
        if os.path.exists(reportZip_name):
            os.remove(reportZip_name)
        z = zipfile.ZipFile(reportZip_name, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(self.report_path):
            fpath = dirpath.replace(self.report_path, '')
            fpath = fpath and fpath + os.sep or ''
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()
        logger.info("测试报告压缩完成！")

    def send_email(self):
        """发送email"""
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取本地时间 转换成日期
        reportZip_name = f"{rq}_自动化测试报告.zip"  # 要压缩的文件名
        self.zip_report(os.path.join(self.emailPath, reportZip_name))
        send_file = os.path.join(self.emailPath, reportZip_name)  # 要发送文件的位置
        try:
            # 创建一个带附件的实例
            message = MIMEMultipart()
            self.receiver = self.receiver.split(',')
            message['From'] = formataddr([self.username, self.email])
            logger.info('发件人姓名：{}'.format(self.username))
            logger.info('发件人邮箱：{}'.format(self.email))
            message['To'] = ','.join(self.receiver)
            logger.info('收件人邮箱：{}'.format(self.receiver))
            message['Subject'] = reportZip_name

            # 邮件正文内容
            message.attach(MIMEText('附件为自动化测试报告.zip', 'plain', 'utf-8'))

            # 构造附件1，传送当前目录下的 report.zip 文件
            att1 = MIMEText(open(send_file, 'rb').read(), 'base64', 'utf-8')
            logger.info('读取附件')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "自动化测试报告.zip"))
            message.attach(att1)
            logger.info('添加附件')

            server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            logger.info('连接QQ邮箱smtp服务')
            server.login(self.email, self.password)
            logger.info('连接成功')
            server.sendmail(self.email, self.receiver, message.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            logger.info("邮件发送成功")
        except Exception:
            logger.error("邮件发送失败", exc_info=1)
