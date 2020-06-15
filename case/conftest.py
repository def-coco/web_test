#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 5:22
# @Author  : CMF
# @File    : conftest.py
from selenium import webdriver
from pages.login_page import LoginPage
import pytest

@pytest.fixture(scope="session")
def login_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    return driver