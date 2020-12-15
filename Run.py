#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 23:41
# @Author  : kuangxiaojiang
# @File    : Run.py
# @Function: 自动化测试框架运行入口
import pytest
import os
from DataDriven.ExcelCollect import excel_collect


if __name__ == '__main__':
    file_path = r'D:\AutoTestFiles\场景\场景_高危人群_糖尿病高危.xlsx'
    file_list = excel_collect(file_path)
    print(file_list)
    pytest.main(file_list)
    # pytest.main(['Cases\danganguanli\Test_gerendangan.py'])
    os.system('allure serve ./Temp  ./Report')
    # # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ./Temp -o ./Report --clean-alluredir')
    # os.system('pytest .\Cases\danganguanli\Test_gerendangan.py --alluredir C:\Windows\System32\config\systemprofile\AppData\Local\Jenkins\.jenkins\workspace\自动化测试Job\\allure-results --clean-alluredir')

