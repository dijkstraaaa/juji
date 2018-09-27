import unittest
import urllib
from urllib import request
from urllib import parse
from urllib.request import urlopen
import requests
import hashlib
import http
import xml.etree.ElementTree as Etree
from bs4 import BeautifulSoup
import json
import io
from lxml import etree
import http.cookiejar


class Logout(unittest.TestCase):
    # 退出登录
    @classmethod
    def setUpClass(cls):
        print("start")

    @classmethod
    def tearDownClass(cls):
        print("end")

    def test_logout(self):
        values = {
            "mobile": "13120380476",
            "password": "b41cb62ec6767f2e41f9df7a2d161515",
            "type": "1"
        }
       # data = parse.urlencode(values).encode('utf-8')
        url = 'http://123.56.1.184:40000/swagger-ui.html#!/auth-controller/loginUsingPOST'
        getURL = url + "?"+urllib.parse.urlencode(values)
        # data = json.dumps(values)
        req = request.Request(getURL)
        response = urlopen(req)
        response_body = response.read()
        r = requests.post(getURL, data=json.dumps(values))
        if r.status_code == 200:
            xml = response_body.find('data')
            xml_str = Etree.fromstring(xml)
            if 'sessionId' in response_body:
                sessionId = xml_str.find("sessionId").text
            if 'token' in response_body:
                token = xml_str.find("token").text
            print(xml)
            print(r.text)
            return xml, sessionId, token
        else:
            print("######Login Failed!!!######")
            print(r.text)
            # print(response.read().decode('utf-8'))
            #  print(r.text)


if __name__ == "__main__":
        unittest.main()


