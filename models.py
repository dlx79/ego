import datetime

from exts import db

# 用户表
class UserModel(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(100),nullable=True)
    create_time=db.Column(db.DateTime,default=datetime.datetime.now)
    update_time=db.Column(db.DateTime,default=datetime.datetime.now,onupdate=datetime.datetime.now)


# 商品表
class ProjectModel(db.Model):
    __tablename__="project"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    title=db.Column(db.String(100),nullable=False)
    image=db.Column(db.String(100),nullable=True)
    sellPoint=db.Column(db.String(100),nullable=False)
    price=db.Column(db.String(100),nullable=False)
    cid=db.Column(db.String(100),nullable=False)
    num=db.Column(db.String(100),nullable=False)
    barcode=db.Column(db.String(100),nullable=True)
    status=db.Column(db.String(100),nullable=True)
    created=db.Column(db.String(100),nullable=True)
    updated=db.Column(db.String(100),nullable=True)
    descs=db.Column(db.String(100),nullable=True)







