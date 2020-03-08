#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''工具模块 '''
import os
import csv
import hashlib
import json
import sqlite3
from typing import Iterable, Tuple ,List
import config as cf

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
        filename =os.path.join( os.path.dirname(__file__) ,cf.CHECK_SAVE_FILE) 
        flag = path_fixed(filename)
        self.csvf = open(filename,"a+",encoding="utf-8",newline='\n')
        self.writer = csv.writer(self.csvf, delimiter=',')
        #在文件的开头写入列名称
        if flag:
            self.writer.writerow(["时间","结果判定","序列号","操作员"])

    def make(self, x:Iterable):
        self.writer.writerow(x)
        self.csvf.flush()
        # print("日志正在写入:",x)
    
    def repeat_check(self,x:str) ->(bool,str):
        # current = self.csvf.tell()
        self.csvf.seek(0)
        for rows in csv.reader(self.csvf,delimiter=','):
            if row[2] == x:
                return False,"条码 "
        return True,""

# class Log():
#     """记录校验记录的类"""
#     def __init__(self):
#         cfg = config.ACCOUNT_SETTING
#         if  cfg.get("type") not in "sqlite,csv".split(","):
#             raise Exception("log配置文件参数有问题")
#         filename =os.path.join( os.path.dirname(__file__) ,cfg.get("path_name") ) 

#         flag = path_fixed(filename)
#         self.mode = cfg.get("type")
#         # print(filename)
#         if cfg.get("type") == "sqlite":
#             self.conn = sqlite3.connect(filename)
#             self.c = self.conn.cursor()
#             self.c.execute("create table if not exists account(time text,result text,sn text,job_name text)")
#         if cfg.get("type") == "csv":
#             self.csvf = open(filename,"a+",encoding="utf-8",newline='\n')
#             self.writer = csv.writer(self.csvf, delimiter=',')
#             #在文件的开头写入列名称
#             if flag:
#                 self.writer.writerow(["时间","结果判定","序列号","操作员"])

#     def __del__(self):
#         if self.mode == "sqlite":
#             self.c.close()
#             self.conn.close()
#         if self.mode =="csv":
#             self.f.close()

#     def make(self, x:Iterable):
#         if self.mode == "csv":
#             self.writer.writerow(x)
#             self.csvf.flush()
#             # print("日志正在写入:",x)
#         if self.mode == "sqlite":
#             self.c.execute("insert into account values(?,?,?,?)",x)
#             self.c.fetchone()
    
#     def repeat_check(self,x:str) ->(bool,str):
#         # current = self.csvf.tell()
#         if self.mode == "csv":
#             self.csvf.seek(0)
#             for rows in csv.reader(self.csvf,delimiter=','):
#                 if row[2] == x:
#                     return False,"条码重复"
#             return True,""

#         if self.mode == "sqlite":
#             self.c.execute("select sn from account where sn ==?",x)
#             self.conn.commit()
#             n = self.c.fetchone()
#             if n:
#                 return True,""
#             else:
#                 return False,"条码重复"


class AccountManager():
    """建立帐号管理的模块"""
    ACCOUNT = {}
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance    

    def __init__(self,*args, **kwargs):
        filename =os.path.join( os.path.dirname(__file__) ,cf.ACCOUNT_CFG) 
        flag = path_fixed(filename)
        if flag:
            self.f =open(filename,"w+",encoding="utf-8")
        else:
            #读取json文件中的内容
            self.f =open(filename,"r+",encoding="utf-8")
            result = self.f.read()
            if len(result) >0:
                self.__class__.ACCOUNT = json.loads(result)

    def __del__(self):
        # self.update_data() 
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
            self.f.seek(0)
            self.f.truncate()
            json.dump(self.__class__.ACCOUNT,self.f,ensure_ascii=False)
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
        
class Config:
    policy_cfg ={}
    code_data = {}
    policy_cate=("FixRule","RegRule","DateRule","FlowRule")  

    def __init__(self):   
        filename =os.path.join( os.path.dirname(__file__) ,cf.POLICY_CFG) 
        flag = path_fixed(filename)     
        if flag:
            self.f =open(filename,"w+",encoding="utf-8")
        else:
            self.f =open(filename,"r+",encoding="utf-8")
            result = self.f.read()
            if len(result) >0:
                #print(len(result))
                self.__class__.policy_cfg , self.__class__.code_data = json.loads(result)

    def __del__(self):
        self.f.close()
        # print("__del__,")

    def remove_policy(self, name:str) -> bool:
        if name in self.policy_cfg:
            del  self.__class__.policy_cfg[name]
            #把配置信息policy_cfg写上文件中                     
            return True
        self.update_data() 
        return False

    def edit_policy(self,policy_name ,content, model:bool=True) -> bool:
        '''model 为True是修改否则新增'''
        if not model and  policy_name in self.policy_cfg:
                return False
        self.policy_cfg[policy_name] = content
        self.update_data()        
        return True

    def remove_item(self,tmp:Tuple[str]) -> bool:
        cls = self.__class__
        # print("rm",tmp)
        if len(tmp) == 2 :
            cls.code_data[tmp[0]].pop(tmp[1])
        if len(tmp) == 3:
            cls.code_data[tmp[0]][tmp[1]].pop(tmp[2])
        if len(tmp) == 4 and tmp[3] in  cls.code_data[tmp[0]][tmp[1]][tmp[2]]:
            cls.code_data[tmp[0]][tmp[1]][tmp[2]].remove(tmp[3])    
        self.update_data()

    def add_item(self,ll:List[str]):
        cls = self.__class__
        '''tmp为 规则/机型/品名/料号组成的字符串列表'''
        # print("ll列表内容:",ll)
        policy,module,name,pn = ll
        # print("xxx",ll)
        tmp = cls.code_data.setdefault(policy,{}) #避免in操作报错
        # print("tmp",tmp)
        if module not in tmp:
            tmp.update({module:{name:[pn]}})
        if name not in tmp[module]:
            tmp[module].update({name:[pn]})
        if pn not in tmp[module][name]:
            tmp[module][name].append(pn)
        self.update_data()

        # print(cls.code_data)
    def update_data(self):
        self.f.seek(0,0)#从文件开头进行
        self.f.truncate()
        json.dump([self.policy_cfg, self.code_data], self.f,ensure_ascii=False)
        self.f.flush()
        
if __name__ == '__main__':
    l =Log()
    l.make("sfsf")
    del l
    # os.remove(os.path.join(os.getcwd(),"log/log.csv"))
    # os.removedirs(os.path.join(os.getcwd(),"log"))
    # a = AccountManager()
    # a.add_account(("huliang","1233","","",""))
    # policy_cfg ={
    #     "ECS":"FixRule:2,cs;FixRule:8,?,del|-",
    #     "WST":"FixRule:4,4444",
    #     }
    # code_data = {
    #     "ECS":{
    #         "11":{
    #             "面板":["33-44-55-66",],
    #             "jike":["55-55-55-55",]
    #         },
    #         "22":{
    #             "面板2":["2333-4555-5",],
    #         },
    #     },
    #     "WST":{
    #         "33":{
    #             "面板3":["93333-4555-5",],
    #         },
    #         "44":{
    #             "面板4":["84333-4555-5",],
    #         },
    #     },
    # }