#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 22:08
# @Author  : CMF
# @File    : say_word.py

from common.base import Base
from pages.login_page import LoginPage
from selenium import webdriver


class SayWord(Base):
    loc1 = ("xpath", '//*[@id="db-isay"]/form/ul/li[1]/a')
    loc2 = ("xpath", '//*[@id="isay-cont"]')
    loc3 = ("id", "isay-submit")
    loc4 = ("xpath", '//*[@id="statuses"]/div[2]/div/div/div/div[2]/div[1]/blockquote/p')

    def select_say_word(self):
        self.click(self.loc1)

    def input_word(self, text="web测试项目"):
        self.send(self.loc2, text)

    def submit_word(self):
        self.click(self.loc3)

    def is_submit_success(self, expect_text="web测试"):
        text = self.get_text(self.loc4)
        print("获取到的内容是：%s"%text)
        return expect_text in text

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()

    say_word = SayWord(driver)
    say_word.select_say_word()
    say_word.input_word(text="web测试项目")
    say_word.submit_word()
    say_word.is_submit_success()
    driver.quit()
