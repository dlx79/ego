SECRET_KEY="DKNJSKD79890SDS"

# 配置数据库信息
HOSTNAME="localhost"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456789"
DATABASE = "flask_ego"
DB_URI= f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

SQLALCHEMY_DATABASE_URI=DB_URI


