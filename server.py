#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 16:20
# @Author  : Abner
# @File    : server.py
# @describe:
"""
"""
from src.manager_request import app

if __name__ == "__main__":
    # app.config['SERVER_NAME'] = 'happycoding.fun:8866'
    app.run(host="0.0.0.0",port=8866,debug=True)