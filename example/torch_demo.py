#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/30 11:01
# @Author  : Abner
# @File    : torch_demo.py
# @describe:
"""
"""


import requests

img_paht = "E:/project/server_app/res/hymenoptera_data/hymenoptera_data/val/bees/215512424_687e1e0821.jpg"
resp = requests.post("http://localhost:8866/api/predict",
                     files={"file": open(img_paht,'rb')})

print(resp.text)