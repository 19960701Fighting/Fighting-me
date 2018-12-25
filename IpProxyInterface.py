#coding=utf-8
import random
from pymongo import MongoClient

mongoIps = 'mongodb://172.16.0.135:20000,172.16.6.228:20000'
user = 'xujiakai'
pwd = 'xujiakai123'
dbName = 'xujiakai_1'


# col = 'testIpProxy'


class IpProxy:

    def __init__(self, tableName='testIpProxy'):
        # 连接需要存储数据库
        self.client = MongoClient(mongoIps)
        self.db_auth = self.client[dbName]
        self.db_auth.authenticate(user, pwd)
        self.db = self.client[dbName]
        self.account = self.db[tableName]

    def getRandomIP(self):
        ip_list = []
        for x in self.account.find({"isValid": 1}, {"_id": 0, "isValid": 0, "count": 0}):
            ip_list.append(x['ip'])
        try:
            ip_lenth = len(ip_list)
        except:
            return "可用ip不足！！！！"
        if ip_lenth == 0:
            return "可用ip不足！！！！"
        return ip_list[random.randint(0, ip_lenth - 1)]

    def getAllIp(self):
        ip_list = []
        for x in self.account.find({"isValid": 1}, {"_id": 0, "isValid": 0, "count": 0}):
            ip_list.append(x['ip'])
        try:
            ip_lenth = len(ip_list)
        except:
            return "可用ip不足！！！！"
        if ip_lenth == 0:
            return "可用ip不足！！！！"
        return ip_list
