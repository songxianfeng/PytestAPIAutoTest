#-*- coding: UTF-8 -*-
'''
Created on 2020-8-22
@author: DragonKing0318
'''
import json
import requests

class ApiOperations(object):
    '''
    接口操作函数
    '''
    def apicall(self,method,url,getparams,postparams):
        '''
        使用requests请求接口
        @param method: GET  or POST
        @param url:接口请求地址
        @param getparams:Get请求参数
        @param postparams:Post请求参数
        @return: 返回接口请求   
        '''
        result=''    
        if method=='GET':
            if getparams!='':
                result=requests.get(url,getparams)
            else:
                result=requests.get(url)
        if method=='POST':
            if postparams!='':
                result=requests.post(url,postparams)
        return result
    
    def chrestojson(self,result):
        '''
        将接口请求结果转化成json
        '''
        jsdata=json.loads(result.text)       
        return jsdata


if __name__ == "__main__":
        apo = ApiOperations()
        getparams={"q":"python"}
        postparams=""
        data=apo.apicall('GET','https://suggest.taobao.com/sug', getparams, postparams)
        print (data.status_code)
        print (apo.chrestojson(data))
            