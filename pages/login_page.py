#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 23:46
# @Author  : CMF
# @File    : login_page.py

from common.base import Base
from selenium import webdriver


url = "https://www.douban.com/"
class LoginPage(Base):
    loc1 = ('xpath', '//*[@id="anony-reg-new"]/div/div[1]/iframe')
    loc2 = ("xpath", '/html/body/div[1]/div[1]/ul[1]/li[2]')
    loc3 = ("id", "username")
    loc4 = ("id", "password")
    loc5 = ("xpath", '/html/body/div[1]/div[2]/div[1]/div[5]/a')
    loc6 = ('xpath', '//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]')

    def select_pswd_login(self):
        self.switch_iframe(self.loc1)
        self.click(self.loc2)

    def input_username(self, text):
        self.send(self.loc3, text)

    def input_pswd(self, text):
        self.send(self.loc4, text)

    def click_button(self):
        self.click(self.loc5)

    def login(self, user="13813082339", pswd="cmf19960116"):
        self.driver.get(url)
        self.select_pswd_login()
        self.input_username(user)
        self.input_pswd(pswd)
        self.click_button()

    def is_login_success(self, except_text="妄言如初"):
        text = self.get_text(self.loc6)
        print("获取到的文本内容：%s"%text)
        return except_text in text


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    web.is_login_success()
    driver.quit()




