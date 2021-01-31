#-*- coding: UTF-8 -*-
'''
Created on 2020-8-22
@author: DragonKing0318
'''
from  CommonFunctions.DataOperations import DataOperations
from CommonFunctions.ApiOperations import ApiOperations
from CommonFunctions.LogOperations import LogOperations
import pytest,os
import allure

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)

@allure.feature('接口Login测试用例')
class TestLoginApiFail(object):
    '''
    接口Login正常测试用例
     '''
    @pytest.fixture()
    @allure.step('准备测试数据')
    def preparedata(self):
        #读取xml文件
        dataread=DataOperations('Login/test_LoginFail.xml')
        logopr=LogOperations()
        apiopr=ApiOperations()
        return (dataread,logopr,apiopr)
     
    @allure.story('接口Login错误密码请求')
    def test_LoginApiFail(self,preparedata):
        '''
        使用pytest请求login接口
        '''
        method=preparedata[0].readxml("logindata", "method")
        apiurl=preparedata[0].readxml("logindata", "apiurl")
        postparams={preparedata[0].readxml("logindata", "param1"):preparedata[0].readxml("logindata", "value1"),preparedata[0].readxml("logindata", "param2"):preparedata[0].readxml("logindata", "value2")}
        getparams=""
        #1,请求接口   
        apires=preparedata[2].apicall(method,apiurl,getparams,postparams)
        caldata=preparedata[2].chrestojson(apires)
        #2，判断接口请求状态
        if(len(caldata)>0):
            assert apires.status_code==400
            assert caldata["error"]=="user not found"
            preparedata[1].setInfo("接口"+apiurl+" 返回值是"+apires.text)
        else:
            preparedata[1].setError("接口"+apiurl+"请求失败,没有返回信息")
            assert apires.status_code==200
            
    @allure.story('接口使用登录token')
    def test_LoginApiUseSession(self,testSession):
        print ("\n接口token:"+testSession)
        assert len(testSession)>0
        
 
 
if __name__ == '__main__':
        pytest.main(['-s','test_LoginFail.py'])