#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import os
import time
import datetime
import codecs
import multiprocessing as mp
from os import makedirs
from os.path import exists
from selenium import webdriver
import selenium
from selenium.webdriver.common.proxy import *


site = 'https://www.baidu.com/'


class Login(unittest.TestCase):
    def setUp(self):
        self.url = 'http://123.56.1.184:40000/swagger-ui.html'
        print("开始")

    def test_login(self):
        driver = webdriver.Firefox()
        # chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        # os.environ['webdriver.chrome.driver'] = chromedriver
        # driver = webdriver.Chrome(chromedriver)
        driver.get(site)
        driver.maximize_window()  # 将浏览器最大化显示
        time.sleep(5)  # 控制间隔时间，等待浏览器反映

        #driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/div/h2/a').click()
        #time.sleep(1)
        #driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/ul/li[4]/ul/li/div[1]/h3/span[2]/a').click()
        #time.sleep(1)
        driver.find_element_by_id('kw').send_keys('firefox selenium')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        time.sleep(2)
        #driver.find_element_by_id('mtype0.8745219796481122').send_keys('1')
        #driver.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[1]/ul/li[4]/ul/li/div[2]/form/div[2]/input').click()
        #time.sleep(5)
        driver.close()

    def tearDown(self):
        print("结束")


if __name__ == "__main__":
        unittest.main()