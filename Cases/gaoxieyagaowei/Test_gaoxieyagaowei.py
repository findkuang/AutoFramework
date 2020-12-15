
import pytest
import os
import allure
from Utils.GetConfigInfo import USER_INFO
from Middle.SceneMiddle import scene_middle_verify
from DataDriven.ExcelSenceOpt import scene_all
                            

@allure.feature('高血压高危')
@allure.story('高血压高危')
@allure.title('高血压高危档案新增')
def test_gaoxieyagaoweidanganxinzeng(add_user_base_info):
    scene_data = scene_all['高血压高危档案新增']
    scene_middle_verify(USER_INFO['vivi']['username'], USER_INFO['vivi']['password'], scene_data, setUp=add_user_base_info)
        