
import pytest
import os
import allure
from Utils.GetConfigInfo import USER_INFO
from Middle.SceneMiddle import scene_middle_verify
from DataDriven.ExcelSenceOpt import scene_all
                            

@allure.feature('糖尿病高危')
@allure.story('糖尿病高危')
@allure.title('糖尿病高危档案新增')
def test_tangniaobinggaoweidanganxinzeng(add_user_base_info):
    scene_data = scene_all['糖尿病高危档案新增']
    scene_middle_verify(USER_INFO['vivi']['username'], USER_INFO['vivi']['password'], scene_data, setUp=add_user_base_info)
        