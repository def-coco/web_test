# 项目说明

web自动化项目

# 环境准备

- windows
- python3.6
- pytest4.5.1
- allure

# 依赖包安装

使用pip安装依赖包
>pip install -r requirements.txt

# 运行用例

生成的用例报告放在report目录

>pytest --alluredir ./report

# 生成报告

>allure serve ./report