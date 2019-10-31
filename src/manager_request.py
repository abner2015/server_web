#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 16:25
# @Author  : Abner
# @File    : manager_request.py
# @describe:
"""
"""
from flask import Flask,jsonify,g,abort,url_for,request
from src.config import Config
from flask_httpauth import HTTPBasicAuth
from src.app.data import User
from flask_sqlalchemy import SQLAlchemy

import io
import torchvision.transforms as transforms
from PIL import Image
import json
from torchvision import models
auth = HTTPBasicAuth()
import torch



app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SECRET_KEY'])
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:nhy67ujm@sh-cdb-mitdwgrg.sql.tencentcdb.com:63995/bl_children?charset=utf8'

app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


def transform_image(image_bytes):


    my_trainsforms = transforms.Compose(
        [
            transforms.Resize(255),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485,0.456,0.406],
                [0.229,0.224,0.225]
            )
        ]
    )
    image = Image.open(io.BytesIO(image_bytes))
    return my_trainsforms(image).unsqueeze(0)
class_index_json = "E:/project/server_app/res/my_class_index.json"
imagenet_class_index = json.load(open(class_index_json))
# model = models.densenet121(pretrained=True)
model = torch.load("E:/project/server_app/src/dnn/model.pkl")
model.eval()

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _,y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())

    return imagenet_class_index[predicted_idx]



@app.route("/",methods=["GET"])
def index():
    return "Hello World"


@auth.verify_password
def verify_password(username_or_token,password):
    print("username_or_token ",username_or_token,password)
    user = User.verify_auth_token(username_or_token)
    print("user token",user)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        print("user ", user)
        # user=User.query.filter_by(username='admin').first()
        print(not user)
        if not user or not user.verify_password(password):
            print("return False")
            return False
    g.user=user
    return True

@app.route('/api/resouce')
@auth.login_required
def get_resource():
    return jsonify({'data':'Hello, %s '%g.user.username})

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token':token.decode('ascii')})

@app.route('/api/index',methods=['GET'])
@auth.login_required
def index_view():
    return jsonify("welcome to happycoding")

@app.route('/api/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            file = request.files['file']
            img_bytes = file.read()
            class_id, class_name = get_prediction(image_bytes=img_bytes)
        result = {"code":200,"msg":"success","data":[{'class_id': class_id, 'class_name': class_name}]}
        return jsonify(result)
    except Exception as e:
        result = {"code": 400, "msg": "server failed"}
        return jsonify(result)



