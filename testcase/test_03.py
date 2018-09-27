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


class SignUp(unittest.TestCase):
    # 测试用例
    # @classmethod
    def setUp(self):
        self.url = 'http://123.56.1.184:40000/swagger-ui.html#!/user-controller/signupUsingPOST'
        print("start")
        # self.header = {''}

    # @classmethod
    def tearDown(self):
        print("end")

    def test_signup_01(self):
        # 正常数据
        url = self.url
        data = {
            "mobile": "13120380476",
            "password": "b41cb62ec6767f2e41f9df7a2d161515",
            "validateCode": "1"
        }
        r = requests.post(url, data=json.dumps(data))
        print(r.text)
        u"'测试正常数据"
        print("注册成功~")

    def test_signup_02(self):
        # 异常数据
        url = self.url
        data = {
            "mobile": "asf6d786f",
            "password": "&%D&ascf76dsf5",
            "validateCode": "91r7ew"
        }
        r = requests.post(url, data=json.dumps(data))
        print(r.text)
        u"'测试异常数据"
        print("注册失败！")

    def test_signup_03(self):
        # 异常数据
        url = self.url
        data = {
            "mobile": "asf6d786f",
            "password": "&%D&ascf76dsf5",
            "validateCode": "91r7ew"
        }
        r = requests.post(url, data=json.dumps(data))
        print(r.text)
        u"'测试异常数据"
        print("注册失败！")


if __name__ == "__main__":
        unittest.main()