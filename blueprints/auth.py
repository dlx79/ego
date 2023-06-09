import json

from flask import Blueprint,request,jsonify,g,session
from models import  UserModel
from exts import db
from blueprints.forms import RegisterForm
from  werkzeug.security import check_password_hash,generate_password_hash


bp=Blueprint("api",__name__,url_prefix="/api")

# 注册
@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return jsonify({"status":"请使用post方法"})
    else:
        # 验证用户提交的邮箱和验证码是否正确
        # 表单验证用 flask-wtf
        # print(f'request.form=={request.form}')
        form = RegisterForm(request.form)
        print('form.data=',form.data)
        if form.validate():
            username=form.username.data
            password=form.password.data
            email=form.email.data
            _user_=UserModel.query.filter_by(username=username).first()
            if _user_:
                print('该用户已经注册过，请重新输入')
                return jsonify({"status":401,"message":"该用户已经注册过，请重新输入"})
            userM=UserModel(username=username,password=generate_password_hash(password),email=email)
            db.session.add(userM)
            db.session.commit()
            res={"status":200,"message":"恭喜注册成功"}
            return json.dumps(res,ensure_ascii=False)
        else:
            return jsonify({"status":401,"message":"没有获取到注册数据"})

# 登陆
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username=request.values.get("username")
        password=request.values.get("password")

        user=UserModel.query.filter_by(username=username).first()
        if user:
            # 前一个是获取库里的密码，后面一个是传入的密码
            if check_password_hash(user.password,password=password):
                print("登陆成功")
                session['user_id']=user.id
                result = {"status": 200, "message": "登陆成功"}
                return json.dumps(result,ensure_ascii=False)
            else:
                return json.dumps({"status":400,"msg":"密码不对"}, ensure_ascii=False)

        else:
            result={"status":401,"message":"用户名不对"}
            return json.dumps(result,ensure_ascii=False)
    else:
        return '方法错误'



