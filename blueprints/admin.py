# import json
#
# from flask import request, jsonify, Blueprint
# from models import UserModel
# from forms import RegisterForm
# from werkzeug.security import generate_password_hash, check_password_hash
# import datetime
# from exts import db
# from adminform import updateUserForm
# from utils import result,getOrderNum,getTimeStamp,getNowDateTime
#
# # todo
# bp = Blueprint("admin", __name__, url_prefix="/admin")
#
#
# @bp.route("/userlist", methods=['GET', 'POST'])
# def userList():
#     if request.method == 'POST':
#         userList = UserModel.query.filter().all()  # 返回user列表
#         for user in userList:
#             print(user.username)
#         print(json.dumps(userList))
#         if userList:
#             return jsonify({"status": 200, "list": json.dumps(userList), "message": "列表返回成功"})
#         else:
#             return jsonify({"status": 404, "message": "返回列表失败"})
#     else:
#         return jsonify({"请求方法不对"})
#
#
# @bp.route("/addUser", methods=['GET', 'POST'])
# def addUser():
#     ''''在管理员中添加user与注册user逻辑一样'''
#     if request.method == 'GET':
#         return jsonify({"status": 404, "msg": "请求方法不对"})
#     else:
#         form = RegisterForm(request.form)
#         if form.validate():
#             print("验证成功")
#             username = form.username.data
#             password = form.password.data
#             print(username, password)
#             #           密码加密
#             hash_password = generate_password_hash(password=password)
#             create_time = datetime.now()
#             #           通过username查询 验证
#             user_model = UserModel.query.filter_by(username=username).first()
#             if user_model:
#                 return jsonify({"status": 401, "msg": "该用户已被注册"})
#             user = UserModel(username=username, password=hash_password, create_time=create_time)
#             db.session.add(user)
#             db.session.commit()
#             return jsonify({"status": 200, "msg": "添加成功"})
#         else:
#             return jsonify({"status": 401, "msg": "添加失败"})
#
#
# @bp.route("/updateUser/<int:user_id >", methods=['POST'])
# def updateUser(user_id):
#     '''
#     更新用户信息：
#     1.通过前端用户穿过来的id查询
#     2.若用户存在
#         更新信息
#     3.用户不存在
#         返回用户不存在
#     :param user_id:
#     :return:
#     '''
#     user_update = UserModel.query.filter_by(id=user_id).first()
#     if user_update:
#
#         form = updateUserForm(request.form)
#         if form.validate:
#             username = form.username.data
#             email = form.email.date
#             user_update.username = username
#             user_update.email = email
#             #           更新数据
#             db.session.commit()
#             return jsonify({"status": 200, "msg": "更新成功"})
#         else:
#             return jsonify({"status": 401, "msg": "请输入合法更新数据"})
#     else:
#         return jsonify({"status": 404, "msg": "待更新数据不存在"})
#
#
# # 用户删除
# @bp.route('/deleteUser/<int:user_id>', methods=['POST'])
# def deleteUser(user_id):
#     delete_id = UserModel.query.filter_by(id=user_id)
#     if delete_id:
#         delete_id.delete()
#         return jsonify({"status": 200, "msg": "删除用户成功"})
#     else:
#         return jsonify({"status": 401, "msg": "用户信息删除失败"})
#
#
# # 商品信息列表
# @bp.route('/goodsList')
# def goodsList():
#     # todo 待建Goods表
#     goodsList = Goods.query.filter().all  # 返回good列表
#     for good in goodsList:
#         print(good.name)
#     if good:
#         return jsonify({"status": 200, "msg": "返回商品列表成功"})
#     else:
#         return jsonify({"status": 400, "msg": "返回商品列表失败"})
#
#
# # 商品新增
# @bp.route('/addGoods', methods=['POST'])
# def addGoods():
#     if request.method == 'POST':
#         form = request.form
#         #       todo image
#         data = {
#             "name": form["name"],
#             "goodsType_id": form["goodsType"],
#             "originPrice": form["originPrice"],
#             "sellPrice": form["sellPrice"],
#             "contains": form["contains"],
#             "productTime": form["productTime"],
#             "expireTime": form["expireTime"],
#             "createTime": getNowDateTime(),
#             "create_Address_id": form["createAddress"]
#         }
#         goods = Goods(**data)
#         db.session.add(goods)
#         db.session.commit()
#         return jsonify({"status": 200, "msg": "goods新增成功"})
#     else:
#         return jsonify({"status": 401, "msg": "请用post方法"})
#
#
# # 商品更新
# @bp.route("/updateGoods/<int:goodId>", methods=['GET', 'POST'])
# def updateGoods(goodId):
#     if request.method == "POST":
#         good_update = Goods.query.filter(id=goodId).first()
#         if good_update:
#             # todo AddGoodsForm 验证
#             form = AddGoodsForm(request.form)
#             if form.validate:
#                 name = form.username.date
#                 good_update.username = name
#                 db.session.commit()
#                 return jsonify({"status": 200, "msg": "goods更新成功"})
#             else:
#                 return jsonify({"status": 401, "msg": "goods信息有误"})
#         else:
#             return jsonify({"status": 402, "msg": "没有获取到goods信息"})
#     else:
#         return jsonify({"status": 401, "msg": "请用post方法"})
#
#
# # 商品删除
# @bp.route("/deleteGoods/int<goodId>", methods=['POST'])
# def deleteGoods(goodId):
#     Goods.query.filter(id=goodId).delete()
#     return jsonify({"status": 200, "msg": "goods删除成功"})
#
# # 商品分类添加
# @bp.route("/goods/type/add",methods=['POST'])
# def goods_type_add():
#     if request.method == 'POST':
#         name=request.form["name"]
#         _type=GoodsType(name=name)
#         db.session.add(_type)
#         db.session.commit()
#         return jsonify({"status":200,"msg":"商品分类添加成功"})
#     else:
#         jsonify({"status":500,"msg":"请求方法不对"})
#
# # 商品分类查询
# @bp.route("/goods/type/list",methods=['GET'])
# def goods_type_list():
#     if request.method == "GET":
#         typeList=GoodsType.query.all()
#         data=dict()
#         data['data']=[]
#         for type in typeList:
#             dic=type.__dict__
#             del dic["_sa_instance_state"]
#             data['data'].append(dic)
#             print(type.name)
#         return result(200,data)
# #     商品分类删除
# @bp.route("/deleteGoodsType/<int:typeId>",methods=['GET','POST'])
# def deleteGoodsType(typeId):
#     if request.method == 'POST':
#         GoodsType.query.filter(id=typeId).delete()
#         return result(200,message="删除商品分类成功")
# # 地址添加
# @bp.route("/address/add",methods=['POST'])
# def addressAdd():
#     if request.method == 'POST':
#         form=request.form
#         data={
#             "province":form['province'],
#             "town":form['town'],
#             "country":form["country"],
#             "detail":form["detail"]
#         }
#         address=Address(**data)
#         db.session.add(address)
#         db.session.commit()
#         return result(200,message="地址添加成功")
#
#
#
