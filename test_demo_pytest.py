#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:xiaxiwei
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

#引入pytest

class TestDemo:
    #数据初始化
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "xiaomi8"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"]=True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        #隐士等待
        self.driver.implicitly_wait(15)

    #测试用例
    def test_demo(self):
        WebDriverWait(self.driver,15).until(lambda x:self.driver.find_element_by_id())

        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        #TouchAction(driver).long_press().move_to().release().perform()
        #driver.swipe()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")

    def teardown(self):
        self.driver.quit()


1111
