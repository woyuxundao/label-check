#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''工具模块 '''
import os
import csv
import hashlib
import json
from typing import Iterable, Tuple

def path_fixed(filename:str) ->bool:
    #处理文件路径的问题
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename)) 
    if os.path.exists(filename):
        return False
    else:
        return True

class Log():
    """记录校验记录的类"""
    def __init__(self):
        filename =os.path.join( os.path.dirname(__file__) ,"log","log.csv") 
        flag = path_fixed(filename)
        self.csvf = open(filename,"a+",encoding="utf-8",newline='\n')
        self.writer = csv.writer(self.csvf, delimiter=',')

        if flag:
            self.writer.writerow(["时间","结果判定","序列号","操作员"])

    def make(self, x:Iterable):
        self.writer.writerow(x)
        self.csvf.flush()
        # print("日志正在写入:",x)

ACCOUNT_CFG ="account.json"

class AccountManager():
    """建立帐号管理的模块"""
    ACCOUNT = {}
    def __init__(self):
        filename =os.path.join( os.path.dirname(__file__) ,ACCOUNT_CFG) 
        if not os.path.exists(filename):
            self.f =open(filename,"w+",encoding="utf-8")
        else:
            self.f =open(filename,"r+",encoding="utf-8")
            self.__class__.ACCOUNT = json.load(self.f)

    def __del__(self):
        #把配置信息policy_cfg写上文件中
        self.f.seek(0,0)#从文件开头进行
        self.f.truncate()
        json.dump(self.ACCOUNT, self.f,ensure_ascii=False)
        self.f.close()
        # print("__del__,")

    def add_account(self,arg:Tuple[str]) -> bool:
        #如果添加成功则返回True
        # print("arg",arg)
        account , passwd,department,job,email = arg
        if account in self.ACCOUNT:
            return
        else:
            m = hashlib.sha256()
            m.update(passwd.encode())
            new_passwd = m.hexdigest()
            self.__class__.ACCOUNT[account] = (new_passwd,department,job,email)
            return True

    def validate(self,user:str ,password:str) ->bool:
        # print(user,password)
        if user in self.ACCOUNT:
            m = hashlib.sha256()
            m.update(password.encode())
            new_passwd = m.hexdigest()
            # print(new_passwd,self.ACCOUNT[user])
            return new_passwd == self.ACCOUNT[user][0]
        return False

    def del_account(self,account:str):
        return self.__class__.ACCOUNT.pop(cls)     

if __name__ == '__main__':
    # l =Log()
    # l.make("sfsfs")
    # del l
    # os.remove(os.path.join(os.getcwd(),"log/log.csv"))
    # os.removedirs(os.path.join(os.getcwd(),"log"))
    a = AccountManager()
    a.add_account(("huliang","1233","","",""))