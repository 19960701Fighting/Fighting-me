#coding=utf-8
# import PyV8
# def id_deal(id, keyword):
#     with PyV8.JSLocker():
#         ctxt = PyV8.JSContext()
#         ctxt.enter()
#         with open(r'C:\Users\zhangchen\Desktop\js-code\total.js') as f:
#             js_read = f.read()
#             ctxt.eval(js_read)
#             get_key = ctxt.locals.navi
#             vl5x = get_key(id, keyword)
#             #print vl5x
#             ctxt.leave()
#     return vl5x



import execjs
def id_deal(id, keyword):
    with open('total.js') as f:
        js_read = f.read()
        ctx = execjs.compile(js_read)
        vl5x =  ctx.call("navi",id,keyword)
        #print vl5x
    return vl5x