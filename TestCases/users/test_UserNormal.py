#-*- coding: UTF-8 -*-
'''
Created on 2020-7-12
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

@allure.feature('接口User测试用例')
class TestUserApi(object):
    '''
    接口User正常测试用例
     '''
    @pytest.fixture()
    @allure.step('准备测试数据')
    def preparedata(self):
        #读取xml文件
        dataread=DataOperations('users/test_UserNormal.xml')
        logopr=LogOperations()
        apiopr=ApiOperations()
        return (dataread,logopr,apiopr)
     
    @allure.story('接口User正常请求')
    def test_GetUsers(self,preparedata):
        '''
        使用pytest请求user接口
        '''
        method=preparedata[0].readxml("userdata", "method")
        apiurl=preparedata[0].readxml("userdata", "apiurl")
        getparams={preparedata[0].readxml("userdata", "param1"):preparedata[0].readxml("userdata", "value")}
        postparams=""
        #获取读取的页码
        pagenum=preparedata[0].readxml("userdata", "value")
        
        #1,请求接口   
        apires=preparedata[2].apicall(method,apiurl,getparams,postparams)
        #2，判断接口请求状态
        if(apires.status_code==200):
            caldata=preparedata[2].chrestojson(apires)
            #接口数据读取
            print ("\nfirstname:"+caldata["data"][0]["first_name"])
            #判断返回结果
            if(len(caldata['data'])>0):
                with allure.step("判断请求结果："):
                    allure.attach('符合请求的页码')
                assert caldata['page']==int(pagenum)
            else:
                preparedata[1].setError('接口'+apiurl+'请求返回为空！')
                with allure.step("接口请求为空"):
                    allure.attach("接口"+apiurl+"请求第"+pagenum+"数据为空")
                assert 1==0
        else:
            preparedata[1].setError("接口"+apiurl+"请求结果错误！")
            assert   apires.status_code==200
        
        
        
 
if __name__ == '__main__':
        pytest.main(['-s','test_UserNormal.py'])