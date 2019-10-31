#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 17:26
# @Author  : Abner
# @File    : forms.py
# @describe:
"""
"""

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = String
