# encoding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
import unittest
import time
import os

from idna import unicode


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((\
        Header(name, 'utf-8').encode(),\
        addr.encode('utf-8')if isinstance(addr, unicode) else addr))


def send_file(file_new):
    smtpserver = 'smtp.exmail.qq.com'
    user = 'XXX@XX.com'
    password = 'XXX'
    sender = 'XXX@XX.com'
    receiver = ['XXX@XX.com']
    file = open(file_new, 'rb').read()

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    subject = '接口自动化测试报告--'+now

    att = MIMEText(file, 'html', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = '接口自动化测试报告.txt' "

    msgRoot = MIMEMultipart('mixed')
    msgRoot['Subject'] = Header(subject, 'utf-8').encode()
    msgRoot['From'] = 'XXX@XX.com'
    msgRoot['To'] = 'XXX@XX.com'
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    print('已连接主机')
    smtp.login(user,password)
    print('登录成功')
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    print('正在发送......')
    smtp.quit()
    print('邮件发送完成~')


def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new
