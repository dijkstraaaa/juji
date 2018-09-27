import unittest
import requests

from public.BASEWAY import *
import json
# 准备数据
test_data = r'D:\Auto-testing\interfaceTestCase.xlsx'
# 用例目录
test_dir = r'D:\Auto-testing\InterFace-testing\testcase\\'
# 报告目录
report_dir = r'D:\Auto-testing\InterFace-testing\test_report\\'


class Index(unittest.TestCase):
    # 测试用例
    def setUp(self):
        pass

    def test_openhome(self):  # 打开首页
        r = requests.get("http://123.56.1.184:40000/swagger-ui.html")
        print(r.status_code)
        if r.status_code == 200:
            print("success")
        else:
            print("failed")

    def test_result(self):
        # url1 = readexcel_data(0, 1, 0)
        r = requests.get("http://123.56.1.184:40000/swagger-ui.html")
        print(r.status_code)
        code = 200
        try:
            self.assertEqual(r.status_code, code, msg='testing')
            print("+++++test success+++++")
        except:
            print("+++++test failed+++++")



