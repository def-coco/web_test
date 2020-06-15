#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 2:22
# @Author  : CMF
# @File    : read_yml.py
import os
import yaml

def read_ymldata(yml_path):
    with open(yml_path, "r", encoding="utf-8") as f:
        a = yaml.load(f)
        return a

if __name__ == '__main__':
    curpath = os.path.dirname(os.path.realpath(__file__))
    print(curpath)
    yml_path = os.path.join(curpath, "update_info.yml")
    print(yml_path)
    b = read_ymldata(yml_path)
    print(b)
