from functools import wraps
from flask import g,jsonify

def login_required(func):
    # 保留func信息
    def decorated_function(*args,**kwargs):
        if g.user:

            return func(*args,**kwargs)
        else:
            return jsonify({"status":400,"msg":"没有获取到登陆信息"})


    return decorated_function