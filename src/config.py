#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 16:43
# @Author  : Abner
# @File    : config.py
# @describe:
"""
"""
class Config():
    SECRET_KEY = "abi8jke98eretcc"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:63995/flaskblog?charset=utf8'


    SQLALCHEMY_TRACK_MODIFICATIONS = False
