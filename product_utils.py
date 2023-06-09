#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : product_utils.py
# @Author: 理想
# @Date  : 2023/6/4 15:01
# @IDE  : PyCharm
from flask import jsonify
import json

def response(code,msg):
    data=dict()
    data['status']=code
    data['msg']=msg
    return json.dumps(data,ensure_ascii=False)
