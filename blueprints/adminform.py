from wtforms import Form,validators,StringField
from models import UserModel


class updateUserForm(Form):
    username=StringField('username',[validators.Length(min=10,max=100,message="用户名长度不对")])
    email=StringField('eamil',[validators.Length(mix=10,max=100,message="邮箱长度不对")])

    # 自定义验证
    def validate_username(self,field):
        user=field.date
        user_name=UserModel.query.filter_by(username=user).first()
        if not user_name:
            raise validators.ValidationError(message="该用户名不存在")


