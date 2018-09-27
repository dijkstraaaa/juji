# coding=utf-8
import unittest
import HTMLTestRunner
from public import SendEmail
import time
from unittest import TestLoader
from bs4 import BeautifulSoup
import html5lib


# 用例目录
test_suite_dir = r'D:\Auto-testing\InterFace-testing\testcase\\'
# 报告目录
report_dir = r'D:\Auto-testing\InterFace-testing\test_report\\'


def creatsuite():

    testunit = unittest.TestSuite()
    test_dir = test_suite_dir
    package_tests = unittest.defaultTestLoader.discover(test_dir,
                                                        pattern='*.py',
                                                        top_level_dir=None)
    for test_suite in package_tests:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


alltestnames = creatsuite()

if __name__ == '__main__':
    print("开始main")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = report_dir
    filename = test_report+now+'result.html'
    print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'Uney接口测试报告',
        description=u'测试用例执行情况'
    )
    runner.run(alltestnames)
    fp.close()
    new_report = SendEmail.new_report(test_report)
    SendEmail.send_file(new_report)


