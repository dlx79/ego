
from flask import Blueprint,request,jsonify,make_response,session
from exts import  db
from models import ProjectModel
from sqlalchemy import or_,text
import json
from product_utils import response
import logging
from  MyEncoder import MyEncoder

bp_prod=Blueprint('pro',__name__,url_prefix="/")

# 商品规格查询 分页
@bp_prod.route('api/backend/item/selectTbItemAllByPage',methods=['GET','POST'])
def selectItemParamAll():
    if request.method== 'POST':
        return jsonify({"status":500,"message":"请求方法不对"})
    else:
        # 分页
        # project_list=session.query(ProjectModel).order_by(ProjectModel.id.desc()).offset(5).limit(3).all()
        # res=json.loads(request.get_data())
        # print('res=',res)
        page= int(request.values.get('page'))

        project_list=ProjectModel.query.order_by(ProjectModel.id.desc()).offset((page-1)*10).limit(10).all()
        logging.info('project_list=',project_list)
        data = dict()
        data['data'] = []
        for prod in project_list:
            dic=prod.__dict__
            del dic['_sa_instance_state']
            data['data'].append(dic)

        return response(200,data)

# 商品新增
@bp_prod.route('api/backend/item/insertTbItem',methods=['GET','POST'])
def insertTbItem():
    if request.method == 'GET':
        return jsonify({"status":401,"message":"请求方法不对"})
    else:
        form=request.form
        print(form)
        title=request.values.get("title")
        cid=request.values.get("cid")
        sellPoint=request.values.get("sellPoint")
        price=request.values.get("price")
        num=request.values.get("num")
        image=request.values.get("image")
        descs=request.values.get("descs")
        barcode=request.values.get("barcode")
        created=request.values.get("created")
        updated=request.values.get("updated")
        print('title=',title)
        # 查询该数据是否存在
        query_title=ProjectModel.query.filter_by(title=title).first()

        if query_title:
            return json.dumps({"status":401,"msg":"该数据已存在"},ensure_ascii=False)
        else:
            if title or cid is not None:
                prod=ProjectModel(title=title,cid=cid,sellPoint=sellPoint,price=price,num=num,
                              image=image,descs=descs,barcode=barcode,created=created,updated=updated)
                if prod:
                    db.session.add(prod)
                    db.session.commit()
                    return response(200,'商品新增成功')
                else:
                    return jsonify({"status":500,"msg":"商品新增失败"})
            else:
                return jsonify({"status":400,"msg":"没有获取到新增数据！！"})


# 商品总数
@bp_prod.route('api/total',methods=['GET'])

def total():
    if request.method=='GET':
        # 计数
        total_num=ProjectModel.query.count()
        if total_num:
            return response(200,total_num)
        else:
            return make_response({"status":500,"msg":"暂无数据"})
    else:
        return make_response({"status": 500,'msg':"请求方法错误" })

# 模糊查询
@bp_prod.route('api/search',methods=['GET'])
def search():
    if request.method=='GET':
        content=request.args.get('search')
        # ilike不区分大小写
        search=ProjectModel.query.filter(
            or_(ProjectModel.title.ilike(f"%{content}%") if content is not None else text(""),
            ProjectModel.sellPoint.ilike(f"%{content}%") if content is not None else text(""),
            ProjectModel.id.like(f"%{content}%") if content is not None else text("")
            )
        )
        if search:
            search_list=dict()
            search_list['datas']=[]
            for s in search:
                dic=s.__dict__
                del dic['_sa_instance_state']
                search_list['datas'].append(dic)
            return response(200,search_list)
        else:
            return jsonify({"status":500,"msg":"没有数据"})
    else:
        return jsonify({"status":400,"msg":"请用get方法"})

# 删除接口
@bp_prod.route('api/backend/item/deleteTbItem',methods=['GET'])
def delete():
    if request.method =='GET':
        id=request.args.get('id')
        delete_id=ProjectModel.query.filter_by(id=id).first()
        db.session.delete(delete_id)
        db.session.commit()
        if delete_id:
            return response(200,f'数据{id}删除成功')
        else:
            return response(401,f'数据{id}删除失败')
    else:
        return response(500,'请求方法不对')



