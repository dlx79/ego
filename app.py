from flask import Flask
import config
from exts import db
from flask_migrate import Migrate
from flask_cors import CORS
from blueprints.auth import bp as auth_bp
from blueprints.product import bp_prod as pro_bp


app = Flask(__name__)

# r'/*'是通配符 让本服务器所有的URL都允许跨域请求
CORS(app,resource=r'/*')

# 绑定配置文件
app.config.from_object(config)
db.init_app(app)

migrate=Migrate(app,db)
# 登陆和注册
app.register_blueprint(auth_bp)
# 新增商品
app.register_blueprint(pro_bp)




if __name__ == '__main__':
    app.run()
