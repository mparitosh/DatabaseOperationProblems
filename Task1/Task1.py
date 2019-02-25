import json
def dict_generator(indict, pre=None):
    amount=193
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, [key] + pre):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, [key] + pre):
                        yield d
            else:
                if(key=='quantity'):
                    h=value
                    value=(h/100)*amount
                yield pre + [key, value]
    else:
        yield indict


            
with open('data.json') as f:
   myjson = json.load(f)
   

value=dict_generator(myjson)
for i in value:
    print i
