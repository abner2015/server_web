#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 10:39
# @Author  : Abner
# @File    : data.py
# @describe:
"""
"""
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,BadSignature,SignatureExpired)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from passlib.apps import custom_app_context as pwd_context
# from ..config import Config
from flask import Flask
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nhy67ujm@sh-cdb-mitdwgrg.sql.tencentcdb.com:63995/bl_children?charset=utf8'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = 'the quick brown fox jumps over the lazy dog'
db = SQLAlchemy(app)



class User(db.Model):
    __tablename__='user'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    password_hash = db.Column(db.String(120))

    # def __init__(self,username,password):
    #     self.username = username
    #     self.password_hash = password

    def hash_password(self,password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self,password):
        # self.password = password

        return pwd_context.verify(password,self.password_hash)

    def generate_auth_token(self,expiration=600):
        s = Serializer(app.config["SECRET_KEY"],expires_in=expiration)
        print("generate ",s)
        self.ttt = s.dumps({'id':self.id})

        print("ttt  ",s.dumps({'id':self.id}))
        return s.dumps({'id':self.id})

    @staticmethod
    def verify_auth_token(token):
        print("token23 ",token)
        s = Serializer(app.config["SECRET_KEY"])

        print("sss",s)
        try:
            data = s.loads(token)
            print("tryyyyyyyyyy")
        except SignatureExpired:
            print("signaturezException")
            return None
        except BadSignature as e:
            print("BadSigneException",e)
            return None
        print("id",data['id'])
        user = User.query.get(data['id'])
        # user = User.query.get(1)
        return user
    def __repr__(self):
        return '<User %r>' %self.username


if __name__== '__main__':
    print("main ")
    db.create_all()


    user = User(username="admin")
    user.hash_password("123123")
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(username='admin').first()
    print(user)

    # hash = pwd_context.encrypt("123456")
    # print(hash)

    # is_hash = pwd_context.verify("123456",hash)
    # print(is_hash)