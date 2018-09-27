# coding=utf-8
import xlrd
import smtplib
import time
import xlwt
from xlutils.copy import copy
from email.mime.text import MIMEText
from email.header import Header
import os
# 准备数据
test_data = r'D:\Auto-testing\interfaceTestCase.xlsx'
# 用例目录
test_dir = r'D:\Auto-testing\InterFace-testing\testcase'
# 报告目录
report_dir = r'D:\Auto-testing\InterFace-testing\test_report'


def send_email():
    host_dir = 'smtp.exmail.qq.com'
    username = 'xuesong.zhao@juniuo.com'
    passwd = 'HKzxs8494'

    message = MIMEText(u'接口自动化脚本已经测试完成', 'html', 'utf-8')
    message['From'] = 'xuesong.zhao@juniuo.com'  # 发件地址
    message['To'] = ['xuesong.zhao@juniuo.com', 'lifangzhen@juniuo.com']  # 收件地址
    subject = 'Python SMTP邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    # 创建SMTP对象
    e = smtplib.SMTP(host_dir, 25)
    # 创建与服务主机的连接
    e.connect('smtp.exmail.qq.com')
    print('已连接主机')
    # 登录邮箱服务
    e.login(username, passwd)
    print('已登录')
    # 发送相关邮件内容
    e.sendmail( message['From'],  message['To'], message.as_string())
    print('正在发送......')
    # 发送完毕断开连接
    e.quit()
    print('邮件发送完成~')


def readexcel_data(sheet_value, row_value, col_value):
    # 获取当前文件夹的父目录绝对路径
    BASE_DIR = test_data
    # 展示绝对路径
    print(BASE_DIR)
    # 合并当前路径
    filename = BASE_DIR
    # 打开工作簿
    data = xlrd.open_workbook(filename)
    # 选择工作页
    sheet = data.sheet_by_index(sheet_value)
    # 读取行列数据
    datarow = sheet.row(row_value)[col_value].value
    # 返回读取结果
    return datarow


def writeexcel_data(sheet_value, row_value, col_value, datatext):
    # 获取当前文件夹的父目录绝对路径
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # 合并当前路径u
    filename = os.path.join(BASE_DIR, 'test_data/', 'D:\Auto-testing\interfaceTestCase.xlsx')
    # 打开工作簿
    data = xlwt.open_workbook(filename)
    # 利用原工作簿创建新的工作簿
    newdata = copy(data)
    # 创建工作页
    newWs = newdata.get_sheet(0)
    # 写入行列中数据
    newWs.write(1, 3, datatext)
    # 保存文档
    newdata.save(filename)


