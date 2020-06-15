#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 4:58
# @Author  : CMF
# @File    : test_say_word.py
from pages.say_word import SayWord
import allure
import pytest
import os
from common.read_yml import read_ymldata


cur_path = os.path.dirname(os.path.realpath(__file__))
data = os.path.join(cur_path, "test_data.yml")
a = read_ymldata(data)
test_data = a["test_say_word"]

@allure.story("用例1：测试说句话功能")
@allure.title("{title}")
@pytest.mark.parametrize("test_input, expect_text, expected, title",
                         test_data)
def test_say_word(login_fixture, test_input, expect_text, expected, title):
    '''用例描述：
    1.点击“说句话”
    2.输入说句话的内容
    3.点击发布
    '''
    # test_input = "web测试项目"
    driver = login_fixture
    say_word = SayWord(driver)
    with allure.step("1.点击“说句话”"):
        say_word.select_say_word()
    with allure.step("2.输入说句话的内容"):
        say_word.input_word(test_input)
    with allure.step("3.点击发布"):
        say_word.submit_word()
    with allure.step("查看是否发布成功"):
        result = say_word.is_submit_success(expect_text)
        print(result)
    with allure.step("断言：判断是否发布成功"):
        assert result == expected
