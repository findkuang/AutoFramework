
import pytest
import os
from Middle.QueryMiddle import get_query_compare_rst
from Middle.SubmitMiddle import submit_data_and_verify
import allure
from Utils.GetConfigInfo import USER_INFO
                        

@allure.feature('档案管理')
@allure.story('个人档案')
@allure.title('个人档案新增')
def test_gerendanganxinzeng():
    uri = '/app-publichealth/personal/addNewBaseInfo'
    body = {'formJsonStr': '{"liveAddress":{"city":"216449","county":"218534","province":"191019","town":"218535","village":"218536","deep":0,"value":"218536","label":"妙山社区","code":"331023001040","detailAddress":"现住址1"},"residenceAddress":{"city":"216449","county":"218534","province":"191019","town":"218837","village":"218844","deep":0,"value":"218844","label":"下洋潘村委会","code":"331023105206","detailAddress":"户籍地址1"},"mgrOrgCode":"1","docOrgCode":"1","inputOrgCode":"1","inputOrgName":"浙江大学医学院附属第一医院","responsibleDoctorId":"10165","archivingDoctorId":"10165","archivingDate":"2002-05-15","inputDoctorId":"10165","inputDoctorName":"VV","inputDate":"2002-05-15","nation":"GB/T3304.01","gender":"GB/T2261.1.1","isHouseholderReg":"1","hasOperations":["0"],"hasTraumatisms":["0"],"hasTransfusions":["0"],"allergySource":[{"value":0,"isReserveState":true}],"exposureHistory":[{"value":0,"isReserveState":true}],"diseases":[{"value":"FH0369.01","isReserveState":true,"diagnosisTime":""}],"fatherDiseases":[{"value":"FH0369.01","isReserveState":true}],"motherDiseases":[{"value":"FH0369.01","isReserveState":true}],"childrenDiseases":[{"value":"FH0369.01","isReserveState":true}],"siblingDiseases":[{"value":"FH0369.01","isReserveState":true}],"geneticDiseases":[{"value":0,"isReserveState":true}],"disabilityDiseases":[{"value":"FH0370.01","isReserveState":true}],"lifeEnvKitchenVentList":[{"value":0}],"lifeEnvFuelTypeList":[{"value":0}],"lifeEnvWaterList":[{"value":0}],"lifeEnvWcList":[{"value":0}],"lifeEnvAnimalList":[{"value":0}],"gridId":"3310","educationLevel":"FH0388.02","aboBloodType":"CV04.50.005.01","rhBloodType":"CV04.50.020.02","maritalStatus":"GB/T2261.2.10","careerCate":"FH0386.05","hisPayFeeType":"FH0368.02","recordDetailCategory":"addNew","name":"李健","birthday":"1990-03-07","idcardNumber":"431102194007044370","phone":"15886680271","workplace":"工作单位1","contactsName":"李健","contactsPhone":"15886680271","idcardType":"FH0066.01","qcResult":[]}'}
    conditions = {'idcard_number': '431102194007044370'}
    send_method = 'POST'
    sql_path = r'D:\AutoTestFiles\SQL\个人档案新增.sql'
    yml_path = r''
    expected_rst = '{"IdcardNb":"431102194007044370"}'
    submit_data_and_verify(USER_INFO['xtest01']['username'], USER_INFO['xtest01']['password'], uri, body, expected_rst, sql_path, yml_path, send_method,setUp=None,query=conditions)
                