import hashlib
import time
import json

#
def result(code,d={},message=''):
    data=dict()
    data['status']=code,
    data['data']=d,
    data['msg']=message
    return json.dumps(data,ensure_ascii=False)

def md5(m):
    return hashlib.md5(m.encode()).hexdigest()

def getNowDateTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def getTimeStamp():
    return time.time()

def getOrderNum():
    orderNum=str(getTimeStamp()).replace('.','')
    return orderNum

