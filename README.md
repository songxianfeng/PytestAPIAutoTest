# PytestAPIAutoTest
Pytest接口自动化测试项目

### 项目说明
本项目是通过python3+pytest+requests+allure实现的接口自动化测试项目。

### 业务逻辑封装
1，CommonFunctions包

（1）ApiOperations类，接口请求操作类，requests的get,post请求；

（2）DataOperations类，python读取xml数据文件操作类；

（3）LogOperation类，日志操作类函数；

2，TestCases文件夹

存放具体测试用例的文件夹

3，TestData文件夹

存放与测试用例一一对应该的测试数据xml文件

4，Reports文件夹

存放生成allure测试数据及测试报告的文件夹

5，Logs 日志类文件夹

### 项目环境
1，python3

2,Requests模块

3，Pytest开发环境以依赖包

4，Allure测试报告生成环境

项目所需环境安装完成后，下载代码即可使用！
