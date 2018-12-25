#coding=utf-8

#coding=utf-8
import re,datetime,threadpool,arrow,redis,execjs
import random
import requests
import time
import collections
from pymongo import MongoClient
from ceshi2 import id_deal
client1 = MongoClient('mongodb://172.16.0.135:20000,172.16.6.228:20000,172.16.5.168:20000')
db_auth = client1.zhangchen_5
db_auth.authenticate('zhangchen', 'zhangchen')
db1 = client1.zhangchen_5
account = db1.civilReason_0
account1 = db1.wenshu_com
account2 = db1.wenshu
def getNoHtmlBody(content):
    body = None
    try:
        dr = re.compile(r'<[^>]+>', re.S)
        body = dr.sub('', content)
    except Exception, ex:
        print (ex.message)
    return body


import sys,json
reload(sys)
sys.setdefaultencoding('utf-8')



from IpProxyInterface import IpProxy
# def vl5x_deal(cookie):
#     with PyV8.JSLocker():
#         ctxt = PyV8.JSContext()
#         ctxt.enter()
#         with open(r'C:\Users\zhangchen\Desktop\js-code\wenshu2.js') as f:
#             js_read = f.read()
#             ctxt.eval(js_read)
#             get_key = ctxt.locals.getKey
#             vl5x = get_key(cookie)
#             #print vl5x
#             ctxt.leave()
#     return vl5x
def vl5x_deal(cookie):

    with open('wenshu2.js') as f:
        js_read = f.read()
        ctx = execjs.compile(js_read)
        vl5x = ctx.call("getKey",cookie)
        #print vl5x
        # ctxt.leave()
    return vl5x




redis_info = {
    'host': '172.16.0.135',      #建立连接redis数据库
    'port': 6379,
    'db':1,                     #选择需要连接的酷名
}

def conncet_redis():
    pool = redis.ConnectionPool(**redis_info)
    try:
        r1 = redis.Redis(connection_pool=pool)
    except Exception as err:
        raise err
    return r1

r1 = conncet_redis()
ipProxy = IpProxy()
def spider(data_anyou):
    anYou1 = data_anyou["reason"]
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTime1 = nowTime.split('-')
    n = nowTime1[2]
    nowTime2 = nowTime.replace(n,str(int(n)+1))
    year_list = []
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "240",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "wenshu.court.gov.cn",
        "Origin": "http://wenshu.court.gov.cn",
        "Referer": "http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_gscu_2116842793=3423241913u5j419; _gscbrs_2116842793=1; ASP.NET_SessionId=nfp1zaxutuz04m3li0giefmz; Hm_lvt_d2caefee2de09b8a6ea438d74fd98db2=1534734086,1534757972,1534758023,1534906178; vjkl5=76ede9aff7b600801e9185a5dcc1bb28ea9b2455; _gscs_2116842793=t34921746kmu2mg73|pv:6; Hm_lpvt_d2caefee2de09b8a6ea438d74fd98db2=1534922612",
        "Host": "wenshu.court.gov.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    }
    a = hex(int((random.random() + 1) * 0x10000))[3:] + hex(int((random.random() + 1) * 0x10000))[3:] + '-' + hex(
        int((random.random() + 1) * 0x10000))[3:] + '-' + hex(int((random.random() + 1) * 0x10000))[3:] + hex(
        int((random.random() + 1) * 0x10000))[3:] + '-' + hex(int((random.random() + 1) * 0x10000))[3:] + hex(
        int((random.random() + 1) * 0x10000))[3:] + hex(int((random.random() + 1) * 0x10000))[3:]
    data = {
        "guid": a,
    }
    s = requests.session()
    ip1 = json.dumps(ipProxy.getRandomIP())
    ip = str(ip1).replace('"', '')
    proxies = {
        "http": "http://%s" % (ip),
        "https": "https://%s" % (ip),
    }
    number_result = s.post(url='http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6',headers=headers, data=data,proxies=proxies,timeout=20)
    b = requests.utils.dict_from_cookiejar(number_result.cookies)
    ip1 = json.dumps(ipProxy.getRandomIP())
    ip = str(ip1).replace('"', '')
    proxies = {
        "http": "http://%s" % (ip),
        "https": "https://%s" % (ip),
    }
    cont = s.post(url='http://wenshu.court.gov.cn/ValiCode/GetCode', data=data, proxies=proxies,headers=headers,timeout=18)
    num = cont.content
    vjk = b["vjkl5"]

    vl5x = vl5x_deal(vjk)
    data1 = {
        "Param": "上传日期:%s TO %s,案由:%s"%(nowTime,nowTime2,anYou1),
        "Index":"1",
        "Page":"10",
        "Order":"法院层级",
        "Direction":"asc",
        "vl5x":"%s"%(vl5x),
        "number":"%s"%(num),
        "guid":"%s"%(a),
    }
    ip1 = json.dumps(ipProxy.getRandomIP())
    ip = str(ip1).replace('"', '')
    proxies = {
        "http": "http://%s" % (ip),
        "https": "https://%s" % (ip),
    }
    zhuye = s.post(url='http://wenshu.court.gov.cn/List/ListContent',data=data1,headers=headers, proxies=proxies,timeout=15)
    zhuye1 = zhuye.content
    if zhuye.status_code == 200 and zhuye1!='"remind key"':
        code = re.findall('Count":"(.*?)"}',zhuye1.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\',''))
        if code[0]!='0':
            RunEval1 = re.findall('RunEval":"(.*?)","Count', zhuye1.replace('\\', ''))
            RunEval = RunEval1[0]
            wenshu_id = re.findall('裁判日期":"(.*?)",(.*?)"文书ID":"(.*?)",', zhuye1.replace('\\', ''))
            for id in wenshu_id:
                wenshu_id1 = id_deal(id[2], RunEval)
                detail_url = 'http://wenshu.court.gov.cn/CreateContentJS/CreateContentJS.aspx?DocID={}'.format(wenshu_id1)
                ip1 = json.dumps(ipProxy.getRandomIP())
                ip = str(ip1).replace('"', '')
                proxies = {
                    "http": "http://%s" % (ip),
                    "https": "https://%s" % (ip),
                }
                con_1 = s.get(url=detail_url, headers=headers1, proxies=proxies,timeout=15)
                k = 1
                dangShiRen = re.findall('当事人", key: "(.*?)", value: "(.*?)"(.*?),', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))

                try:
                    dangShiRen_list = []
                    people = dangShiRen[0][1]
                    people_list = people.split(',')
                    for info in people_list:
                        dangShiRen1 = collections.OrderedDict()
                        dangShiRen1["caseRole"] = info
                        dangShiRen_list.append(dangShiRen1)

                except:
                    pass
                try:
                    anHao = re.findall('案号":"(.*?)",',con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                    anHao1 = anHao[0]
                except:
                    print con_1.content
                if anHao1 != None:
                    c = r1.sismember('FalvSuSong_com', anHao1)
                    if c != True:
                        r1.sadd('FalvSuSong_com', anHao1)
                        if len(dangShiRen_list)>0:
                            for com in dangShiRen_list:
                                if len(str(com["caseRole"]).decode('utf-8'))>5:
                                    k = 2
                        if k== 2:
                            for com in dangShiRen_list:
                                if len(str(com["caseRole"]).decode('utf-8')) > 5:
                                    data2 = collections.OrderedDict()
                                    FalvSuSong_list = []
                                    data2["FalvSuSong"] = FalvSuSong_list
                                    FalvSuSong = collections.OrderedDict()
                                    FalvSuSong["companyName"] = com["caseRole"]
                                    try:
                                        FalvSuSong["time"] = (arrow.get(id[0], 'YYYY-MM-DD',tzinfo='local').timestamp) * 1000
                                    except:
                                        FalvSuSong["time"] = None

                                    #anHao = re.findall('案号":"(.*?)",',con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    faYuan = re.findall('法院名称":"(.*?)",', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    try:
                                        submitDate = (arrow.get(str(nowTime), 'YYYY-MM-DD',tzinfo='local').timestamp) * 1000
                                    except:
                                        submitDate = None
                                    wenShuName = re.findall('案件名称":"(.*?)",', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    anYou = re.findall('案由", key: "(.*?)", value: "(.*?)"(.*?),',con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    zhuangTai = re.findall('审判程序":"(.*?)",', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    anHao = re.findall('案号":"(.*?)",', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                                    wenShuUrl = re.findall('Title\\":\\"(.*?)var jsonData', con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))


                                    try:
                                        FalvSuSong["anHao"] = anHao[0]
                                    except:
                                        FalvSuSong["anHao"] = None
                                    try:
                                        FalvSuSong["faYuan"] = faYuan[0]
                                    except:
                                        FalvSuSong["faYuan"] = None
                                    try:
                                        FalvSuSong["submitDate"] = submitDate
                                    except:
                                        FalvSuSong["submitDate"] = None

                                    try:
                                        FalvSuSong["wenShuName"] = wenShuName[0]
                                    except:
                                        FalvSuSong["wenShuName"] = None

                                    try:
                                        FalvSuSong["anYou"] = anYou[0][1]
                                    except:
                                        FalvSuSong["anYou"] = None

                                    try:
                                        FalvSuSong["zhuangTai"] = zhuangTai[0]
                                    except:
                                        FalvSuSong["zhuangTai"] = None
                                    FalvSuSong["dangShiRen"] = dangShiRen_list
                                    try:
                                        FalvSuSong["anHao"] = anHao[0]
                                    except:
                                        FalvSuSong["anHao"] = None

                                    try:
                                        content = wenShuUrl[0]
                                        content_list = re.findall('<div(.*?)</div>',content)
                                        x_list = []
                                        for key in content_list:
                                            key1 = getNoHtmlBody(key)
                                            key2 = key1.split('>')
                                            key3 = key2[1]
                                            x_list.append(key3)
                                        wenshu_content = '&&'.join(x_list)
                                        FalvSuSong["wenShuUrl"] = wenshu_content
                                    except:
                                        FalvSuSong["wenShuUrl"] = None


                                    FalvSuSong_list.append(FalvSuSong)
                                    if FalvSuSong["wenShuUrl"]!=None:
                                        b = json.dumps(data2, ensure_ascii=False)
                                        requests.post(url='http://58.246.234.62:8090/Web/data/realTimeStream',data=bytes(b))
                                        print '公司;%s,时间:%s' % (FalvSuSong["companyName"],datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                        account1.insert(data2)

                                    else:
                                        print FalvSuSong["anHao"]
                        elif k == 1:
                            data2 = collections.OrderedDict()
                            FalvSuSong_list = []
                            data2["FalvSuSong"] = FalvSuSong_list
                            FalvSuSong = collections.OrderedDict()
                            try:
                                FalvSuSong["time"] = (arrow.get(id[0], 'YYYY-MM-DD', tzinfo='local').timestamp) * 1000
                            except:
                                FalvSuSong["time"] = None

                            # anHao = re.findall('案号":"(.*?)",',con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\', ''))
                            faYuan = re.findall('法院名称":"(.*?)",',
                                                con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace(
                                                    '\\', ''))
                            try:
                                submitDate = (arrow.get(str(nowTime), 'YYYY-MM-DD', tzinfo='local').timestamp) * 1000
                            except:
                                submitDate = None
                            wenShuName = re.findall('案件名称":"(.*?)",',
                                                    con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace(
                                                        '\\', ''))
                            anYou = re.findall('案由", key: "(.*?)", value: "(.*?)"(.*?),',
                                               con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\',
                                                                                                                           ''))
                            zhuangTai = re.findall('审判程序":"(.*?)",',
                                                   con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace(
                                                       '\\', ''))
                            anHao = re.findall('案号":"(.*?)",',
                                               con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace('\\',
                                                                                                                           ''))
                            wenShuUrl = re.findall('Title\\":\\"(.*?)var jsonData',
                                                   con_1.content.replace('\r', '').replace('\t', '').replace('\n', '').replace(
                                                       '\\', ''))

                            try:
                                FalvSuSong["anHao"] = anHao[0]
                            except:
                                FalvSuSong["anHao"] = None
                            try:
                                FalvSuSong["faYuan"] = faYuan[0]
                            except:
                                FalvSuSong["faYuan"] = None
                            try:
                                FalvSuSong["submitDate"] = submitDate
                            except:
                                FalvSuSong["submitDate"] = None

                            try:
                                FalvSuSong["wenShuName"] = wenShuName[0]
                            except:
                                FalvSuSong["wenShuName"] = None

                            try:
                                FalvSuSong["anYou"] = anYou[0][1]
                            except:
                                FalvSuSong["anYou"] = None

                            try:
                                FalvSuSong["zhuangTai"] = zhuangTai[0]
                            except:
                                FalvSuSong["zhuangTai"] = None
                            FalvSuSong["dangShiRen"] = dangShiRen_list
                            try:
                                FalvSuSong["anHao"] = anHao[0]
                            except:
                                FalvSuSong["anHao"] = None

                            try:
                                content = wenShuUrl[0]
                                content_list = re.findall('<div(.*?)</div>', content)
                                x_list = []
                                for key in content_list:
                                    key1 = getNoHtmlBody(key)
                                    key2 = key1.split('>')
                                    key3 = key2[1]
                                    x_list.append(key3)
                                wenshu_content = '&&'.join(x_list)
                                FalvSuSong["wenShuUrl"] = wenshu_content
                            except:
                                FalvSuSong["wenShuUrl"] = None

                            FalvSuSong_list.append(FalvSuSong)
                            if FalvSuSong["wenShuUrl"] != None:
                                print '案号;%s,时间:%s' % (FalvSuSong["anHao"], datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                                account2.insert(data2)

                        else:
                            pass

                    else:
                        print '%s,已存在'%(anHao1)
        else:
            print '暂无此案由'

def pool(name_list):
    # start_time = time.time()
    pool = threadpool.ThreadPool(10)
    request = threadpool.makeRequests(spider, name_list)
    [pool.putRequest(req) for req in request]
    pool.wait()
    # print '%d second' % (time.time() - start_time)


if __name__ == "__main__":
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
    print(nowTime)
    x_list = []
    while True:
        for conn in account.find(no_cursor_timeout=True).batch_size(5000):

            x_list.append({"reason":conn["reason"]})
            if len(x_list) == 500:
                pool(x_list)
                x_list = []
        if x_list != []:
            pool(x_list)

             