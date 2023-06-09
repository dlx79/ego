from wtforms import Form,StringField,validators
from exts import db
from  models import UserModel

# Form：主要就是用来验证前端提交的数据是否符合要求

class RegisterForm(Form):
    username=StringField('username',[validators.Length(min=3,max=20,message="用户名长度不对")])
    password=StringField('password',[validators.Length(min=4,max=20,message='密码格式不对')])
    comfirm_pwd=StringField([validators.Length(min=4,max=20),validators.EqualTo("password",message="两次密码不一样")])
    email=StringField('email',[validators.Length(min=3,max=30,message="邮箱格式不对")])
    # 自定义验证：
    # 1.邮箱是否已经被注册

    # def validate_email(self,field):
    #     email=field.data
    #     email=UserModel.query.filter_by(email=email).first()
    #     if email:
    #         raise validators.ValidationError(message="该邮箱已经被注册")

    # def validate_username(self,field):
    #     user = field.data
    #     user = UserModel.query.filter_by(username=user).first()
    #     if user:
    #         raise validators.ValidationError(message="用户名已存在")


