#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 17:26
# @Author  : Abner
# @File    : post_request.py
# @describe:
"""
"""
import requests

token = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MjM5ODQwOSwiZXhwIjoxNTcyMzk5MDA5fQ.eyJpZCI6MX0.WFBOMyZ6_YFceHedaIMwin3crUSMg31R4mjFPxUSZQnYqshXHjn9rb5gHKwEV1-5bqQftLKZ6iD0PhjONHCMSw"

headers = {
        "token": token
}

data = {'mobile':'1851174****'}
url2 = "http://localhost:8866/api/index"
#初始化post请求对象（需要传入url、提交的数据、header）
s = requests.get(url2,headers=headers,auth=(token,""))
#打印返回结果
print(s.text)
