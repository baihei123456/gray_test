# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
import unittest
class EtcLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("E:\study\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://uat-www.etc-parts.com/#/login")
        #time.sleep(2)
    def tearDown(self):
        self.driver.quit()
    def test_etclogin(self):
        self.driver.find_element_by_name("loginName").send_keys("18888888123")
        self.driver.find_element_by_name("password").send_keys("Aa123456")
        self.driver.find_element_by_css_selector('.el-button.login-in.el-button--primary').click()
        member_info=self.driver.find_element_by_css_selector('.name.beyond-ellipsis-show').text
        time.sleep(5)
        #print(member_info)
        try:
            self.assertIn('宁波',member_info)
        except AssertionError as e:
                print(f"登录失败")
                self.driver.get_screenshot_as_file("%s.png" % nowTime)
                raise

"""    def test_etclogin_error(self):
        pass

    def test_etclogin_error(self):
        pass

    def test_etclogin_error(self):
        pass

    def test_etclogin_error(self):
        pass"""