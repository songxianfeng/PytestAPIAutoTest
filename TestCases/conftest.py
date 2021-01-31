#-*- coding: UTF-8 -*-
'''
Created on 2020-8-22

@author: DragonKing0318
'''
import pytest
from CommonFunctions.ApiOperations import ApiOperations

@pytest.fixture(scope='session')
def testSession():
    #实例化类
    apiopr=ApiOperations()
    getparams=""
    postparams={"email":"eve.holt@reqres.in","password":"1123444"}
    apires=apiopr.apicall("POST","https://reqres.in/api/login", getparams, postparams)
    apidata=apiopr.chrestojson(apires)
    return apidata["token"]
    