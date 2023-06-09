import json
from datetime import datetime

class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,tuple):
            return tuple(obj)
        elif isinstance(obj,bytes):
            return str(obj,encoding='utf-8')
        elif isinstance(obj,int):
            return int(obj)
        elif isinstance(obj,float):
            return float(obj)
        else:
            return super(MyEncoder,self).default(obj)

